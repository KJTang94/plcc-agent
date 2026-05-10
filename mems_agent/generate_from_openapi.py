import json
import re
from pathlib import Path

_OPENAPI_FILE = Path(__file__).parent / "mems_openapi.json"
_OUTPUT_DIR = Path(__file__).parent


def _clean_path(path: str) -> str:
    path = re.sub(r'\}+', '}', path)
    return path


def _escape_str(s: str) -> str:
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\n", " ")
    s = s.replace("\r", "")
    return s


def load_openapi():
    with open(_OPENAPI_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def path_to_method_name(method: str, path: str, summary: str) -> str:
    path_part = path.replace("/api/v1/", "").strip("/")
    parts = path_part.split("/")

    action_prefix = {"GET": "get", "POST": "add", "PUT": "update", "DELETE": "delete"}.get(method, method.lower())

    name_parts = []
    skip_next = False
    for i, part in enumerate(parts):
        if skip_next:
            skip_next = False
            continue
        if part.startswith("{") and part.endswith("}"):
            param_name = part[1:-1]
            if i > 0 and parts[i - 1] not in ("by_role", "by_user", "by_user_group", "by_ids", "by_dev"):
                name_parts.append("by_" + param_name.replace("_id", "").replace("id", ""))
            continue
        if part in ("by_role", "by_user", "by_user_group", "by_ids", "by_dev"):
            name_parts.append(part)
            skip_next = True
            continue
        name_parts.append(part)

    if method == "GET" and not name_parts:
        name_parts = ["query"]

    raw_name = action_prefix + "_" + "_".join(name_parts) if name_parts else action_prefix

    raw_name = re.sub(r'_+', '_', raw_name)
    raw_name = raw_name.strip("_")

    return raw_name


def _normalize_type(t) -> str:
    if isinstance(t, list):
        non_null = [x for x in t if x != "null"]
        return non_null[0] if non_null else "string"
    return t if isinstance(t, str) else "string"


def extract_params(spec: dict) -> list:
    params = []
    for p in spec.get("parameters", []):
        schema = p.get("schema", {})
        raw_type = schema.get("type", "string")
        param = {
            "name": p["name"],
            "in": p.get("in", "path"),
            "required": p.get("required", False),
            "type": _normalize_type(raw_type),
            "description": p.get("description", ""),
        }
        params.append(param)
    return params


def has_body(spec: dict) -> bool:
    return "requestBody" in spec


def generate_mems_api_methods(openapi: dict) -> str:
    lines = []
    seen_names = {}
    counter = {}

    for path, methods in sorted(openapi["paths"].items()):
        for method, spec in methods.items():
            if method not in ("get", "post", "put", "delete"):
                continue

            summary = spec.get("summary", "")
            params = extract_params(spec)
            body = has_body(spec)
            api_path = _clean_path(path.replace("/api/v1", ""))

            name = path_to_method_name(method.upper(), api_path, summary)

            if name in seen_names:
                counter[name] = counter.get(name, 0) + 1
                name = f"{name}_{counter[name]}"
            seen_names[name] = True

            path_params = [p for p in params if p["in"] == "path"]
            query_params = [p for p in params if p["in"] == "query"]

            func_params = []
            for p in path_params:
                type_map = {"integer": "int", "number": "float", "string": "str", "boolean": "bool"}
                py_type = type_map.get(p["type"], "str")
                func_params.append(f"{p['name']}: {py_type}")

            for p in query_params:
                type_map = {"integer": "int", "number": "float", "string": "str", "boolean": "bool"}
                py_type = type_map.get(p["type"], "str")
                if p["required"]:
                    func_params.append(f"{p['name']}: {py_type}")
                else:
                    func_params.append(f"{p['name']}: {py_type} = None")

            if body:
                func_params.append("data: dict = None")

            func_sig = "self" + (", " + ", ".join(func_params) if func_params else "")

            url_path = api_path
            for p in path_params:
                url_path = url_path.replace("{" + p["name"] + "}", "{" + p["name"] + "}")

            call_params = []
            if query_params:
                query_dict = ", ".join(
                    f'"{p["name"]}": {p["name"]}' for p in query_params
                )
                call_params.append(f"params={{{query_dict}}}")
            if body:
                call_params.append("data=data")

            call_str = ", ".join(call_params)

            lines.append(f"    def {name}({func_sig}) -> str:")
            lines.append(f'        return self._request(\'{method.upper()}\', f\'{url_path}\'{", " + call_str if call_str else ""})')
            lines.append("")

    return "\n".join(lines)


def generate_tools_code(openapi: dict) -> str:
    lines = [
        "from typing import List, Dict, Any, Optional, TypedDict",
        "",
        "",
        "class ParameterInfo(TypedDict):",
        "    name: str",
        "    type: str",
        "    required: bool",
        "    description: str",
        "",
        "",
        "class ToolInfo:",
        "    def __init__(self, name, description, func, parameters: Optional[List[ParameterInfo]] = None):",
        "        self.name = name",
        "        self.description = description",
        "        self.func = func",
        "        self.parameters = parameters or []",
        "",
        "",
        "def create_tools(mems_api) -> List[ToolInfo]:",
        "    tools = []",
        "",
    ]

    seen_names = {}
    counter = {}

    lines.append('    tools.append(ToolInfo(')
    lines.append('        name="login",')
    lines.append('        description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。",')
    lines.append('        func=mems_api.login')
    lines.append('    ))')
    lines.append("")

    for path, methods in sorted(openapi["paths"].items()):
        for method, spec in methods.items():
            if method not in ("get", "post", "put", "delete"):
                continue

            summary = spec.get("summary", "")
            params = extract_params(spec)
            body = has_body(spec)
            api_path = _clean_path(path.replace("/api/v1", ""))

            name = path_to_method_name(method.upper(), api_path, summary)

            if name in seen_names:
                counter[name] = counter.get(name, 0) + 1
                name = f"{name}_{counter[name]}"
            seen_names[name] = True

            path_params = [p for p in params if p["in"] == "path"]
            query_params = [p for p in params if p["in"] == "query"]

            desc = _escape_str(summary)
            param_descs = []
            for p in path_params + query_params:
                type_map = {"integer": "integer", "number": "number", "string": "string", "boolean": "boolean"}
                ptype = type_map.get(p["type"], "string")
                req_str = "必填" if p["required"] else "可选"
                param_descs.append(f"{p['name']} ({ptype}, {req_str}) - {_escape_str(p['description'])}")
            if body:
                param_descs.append("data (dict) - 请求体数据")
            if param_descs:
                desc += "。参数：" + ", ".join(param_descs)

            tool_params = []
            for p in path_params + query_params:
                type_map = {"integer": "integer", "number": "number", "string": "string", "boolean": "boolean"}
                ptype = type_map.get(p["type"], "string")
                tool_params.append({
                    "name": p["name"],
                    "type": ptype,
                    "required": p["required"],
                    "description": _escape_str(p["description"]),
                })
            if body:
                tool_params.append({
                    "name": "data",
                    "type": "dict",
                    "required": True,
                    "description": "请求体数据",
                })

            lines.append('    tools.append(ToolInfo(')
            lines.append(f'        name="{name}",')
            lines.append(f'        description="{desc}",')
            lines.append(f'        func=mems_api.{name},')
            if tool_params:
                lines.append('        parameters=[')
                for tp in tool_params:
                    lines.append(f'            {{"name": "{tp["name"]}", "type": "{tp["type"]}", "required": {tp["required"]}, "description": "{tp["description"]}"}},')
                lines.append('        ]')
            lines.append('    ))')
            lines.append("")

    lines.append("    return tools")
    lines.append("")
    return "\n".join(lines)


def generate_api_docs(openapi: dict) -> str:
    output = "# MEMS API 文档\n\n***\n\n"
    output += "## 概述\n\n"
    output += "本文档描述了MEMS应用的RESTful API接口和数据类型定义，方便AI Agent调用。\n\n"
    output += "### 基础信息\n\n"
    output += "- **基础URL**: `http://ip:port/api/v1/`\n"
    output += "- **认证方式**: Access-Token（在请求头中携带）\n"
    output += "- **Content-Type**: `application/json`\n\n"
    output += "### 认证说明\n\n"
    output += "所有API请求（除登录接口外）需要在请求头中携带Access-Token：\n\n"
    output += "```http\nAccess-Token: <your_token>\n```\n\n"

    modules = {}
    all_apis = []

    for path, methods in sorted(openapi["paths"].items()):
        for method, spec in methods.items():
            if method not in ("get", "post", "put", "delete"):
                continue
            summary = spec.get("summary", "")
            params = extract_params(spec)
            body = has_body(spec)
            api_path = _clean_path(path.replace("/api/v1", ""))
            name = path_to_method_name(method.upper(), api_path, summary)

            module = "other"
            path_parts = api_path.strip("/").split("/")
            if len(path_parts) >= 1:
                module = path_parts[0]
                _module_aliases = {
                    "alarms": "alarm",
                    "aoe_results": "aoes",
                    "ems_list": "ems",
                    "file_tree": "files",
                    "file_tree_version": "files",
                    "logs_bytes": "devices",
                    "measureinits": "measures",
                    "multi_import_bytes": "devices",
                    "running_aoes": "aoes",
                    "script_file": "scripts",
                    "script_md5": "scripts",
                    "script_results": "scripts",
                    "script_wasm": "scripts",
                    "soes": "measures",
                    "unrun_aoes": "aoes",
                    "webplugin_file": "webplugins",
                    "webplugin_md5": "webplugins",
                    "north": "flows",
                    "ping": "system",
                    "common_map": "system",
                    "config": "system",
                    "commands": "controls",
                    "allmodels_bytes": "devices",
                }
                if module.startswith("lcc"):
                    module = "lcc"
                elif module.startswith("pscpu"):
                    module = "pscpu"
                elif module in _module_aliases:
                    module = _module_aliases[module]

            all_apis.append({
                "method": method.upper(),
                "path": api_path,
                "summary": summary,
                "params": params,
                "body": body,
                "name": name,
                "module": module,
            })

            if module not in modules:
                modules[module] = []
            modules[module].append(all_apis[-1])

    output += "## API 概览\n\n"
    output += f"共 **{len(all_apis)}** 个API接口，分为以下模块：\n\n"
    for mod_name, mod_apis in sorted(modules.items()):
        output += f"- **{mod_name}**: {len(mod_apis)} 个接口\n"
    output += "\n***\n\n"

    for mod_name, mod_apis in sorted(modules.items()):
        output += f"## {mod_name.capitalize()} 模块\n\n"
        output += f"共 {len(mod_apis)} 个接口\n\n"

        for i, api in enumerate(mod_apis, 1):
            output += f"### {i}. {api['summary']}\n\n"
            output += f"- **方法**: `{api['method']}`\n"
            output += f"- **路径**: `{api['path']}`\n"
            output += f"- **函数名**: `{api['name']}`\n"

            path_params = [p for p in api["params"] if p["in"] == "path"]
            query_params = [p for p in api["params"] if p["in"] == "query"]

            if path_params:
                output += "\n**路径参数**:\n\n"
                output += "| 参数名 | 类型 | 必填 | 说明 |\n"
                output += "| --- | --- | --- | --- |\n"
                for p in path_params:
                    req = "是" if p["required"] else "否"
                    output += f"| {p['name']} | {p['type']} | {req} | {p['description']} |\n"

            if query_params:
                output += "\n**查询参数**:\n\n"
                output += "| 参数名 | 类型 | 必填 | 说明 |\n"
                output += "| --- | --- | --- | --- |\n"
                for p in query_params:
                    req = "是" if p["required"] else "否"
                    output += f"| {p['name']} | {p['type']} | {req} | {p['description']} |\n"

            if api["body"]:
                output += "\n**请求体**: JSON对象\n"

            output += "\n"

    schemas = openapi.get("components", {}).get("schemas", {})
    if schemas:
        enum_types = []
        object_types = []
        for name, schema in sorted(schemas.items()):
            if schema.get("enum"):
                enum_types.append((name, schema))
            elif schema.get("type") == "object" or schema.get("properties"):
                object_types.append((name, schema))

        if enum_types:
            output += "## 枚举类型定义\n\n"
            output += f"共 {len(enum_types)} 个枚举类型\n\n"
            for i, (name, schema) in enumerate(enum_types, 1):
                output += f"### {i}. {name}\n\n"
                desc = schema.get("description", "")
                if desc:
                    output += f"- **描述**: {desc}\n"
                values = schema.get("enum", [])
                if values:
                    output += f"- **可选值**: {', '.join(str(v) for v in values)}\n"
                output += "\n"

        if object_types:
            output += "## 对象类型定义\n\n"
            output += f"共 {len(object_types)} 个对象类型\n\n"
            for i, (name, schema) in enumerate(object_types, 1):
                output += f"### {i}. {name}\n\n"
                desc = schema.get("description", "")
                if desc:
                    output += f"- **描述**: {desc}\n"
                props = schema.get("properties", {})
                if props:
                    output += "\n**字段**:\n\n"
                    output += "| 字段名 | 类型 | 说明 |\n"
                    output += "| --- | --- | --- |\n"
                    required_fields = schema.get("required", [])
                    for prop_name, prop_schema in props.items():
                        prop_type = prop_schema.get("type", "any")
                        if prop_schema.get("$ref"):
                            ref = prop_schema["$ref"].split("/")[-1]
                            prop_type = ref
                        prop_desc = prop_schema.get("description", "")
                        req = "是" if prop_name in required_fields else "否"
                        output += f"| {prop_name} | {prop_type} | {prop_desc} |\n"
                output += "\n"

    return output


def update_mems_agent(openapi: dict):
    mems_agent_file = _OUTPUT_DIR / "mems_agent.py"
    with open(mems_agent_file, "r", encoding="utf-8") as f:
        content = f.read()

    methods_code = generate_mems_api_methods(openapi)

    class_start = content.find("class MemsAPI:")
    if class_start == -1:
        print("ERROR: Cannot find 'class MemsAPI:' in mems_agent.py")
        return

    next_class_start = content.find("\nclass ", class_start + 1)
    if next_class_start == -1:
        print("ERROR: Cannot find next class after MemsAPI")
        return

    init_end = content.find("\n    def ", class_start + 1)
    if init_end == -1 or init_end > next_class_start:
        init_end = next_class_start

    login_end = content.find("\n    def ", init_end + 1)
    if login_end == -1 or login_end > next_class_start:
        login_end = next_class_start

    request_method_end = content.find("\n    def ", login_end + 1)
    if request_method_end == -1 or request_method_end > next_class_start:
        request_method_end = next_class_start

    first_api_method = content.find("\n    def ", request_method_end + 1)
    if first_api_method == -1 or first_api_method > next_class_start:
        first_api_method = next_class_start

    new_content = content[:first_api_method] + "\n" + methods_code + content[next_class_start:]

    with open(mems_agent_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated MemsAPI class in {mems_agent_file}")


def update_tools(openapi: dict):
    tools_file = _OUTPUT_DIR / "mems_tools.py"
    code = generate_tools_code(openapi)
    with open(tools_file, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Updated {tools_file}")


def update_docs(openapi: dict):
    docs_file = _OUTPUT_DIR / "mems_api_docs.md"
    docs = generate_api_docs(openapi)
    with open(docs_file, "w", encoding="utf-8") as f:
        f.write(docs)
    print(f"Updated {docs_file}")


def main():
    openapi = load_openapi()
    print(f"Loaded OpenAPI spec with {len(openapi['paths'])} paths")

    update_mems_agent(openapi)
    update_tools(openapi)
    update_docs(openapi)

    print("\nDone! All files updated from mems_openapi.json")


if __name__ == "__main__":
    main()
