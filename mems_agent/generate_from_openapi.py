from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from openapi_shared import OpenAPIOperation, OpenAPITooling, load_openapi_spec

_OUTPUT_DIR = Path(__file__).parent


@dataclass
class ApiEntry:
    method: str
    path: str
    name: str
    summary: str
    module: str
    operation: OpenAPIOperation
    params: list[Any]
    body: bool
    body_schema: Any


class MemsAPIMethodGenerator:
    def __init__(self, tooling: OpenAPITooling):
        self.tooling = tooling

    def generate(self) -> str:
        lines: list[str] = []
        type_map = {"integer": "int", "number": "float", "string": "str", "boolean": "bool"}

        for method, api_path, name, operation in self.tooling.iter_named_operations():
            params = self.tooling.extract_params(operation)
            path_params = [parameter for parameter in params if parameter.location == "path"]
            query_params = [parameter for parameter in params if parameter.location == "query"]
            has_body = self.tooling.has_body(operation)

            func_params: list[str] = []
            for parameter in path_params:
                py_type = type_map.get(self.tooling.resolver.normalize_type(parameter.schema_.type if parameter.schema_ else "string"), "str")
                func_params.append(f"{parameter.name}: {py_type}")
            for parameter in query_params:
                py_type = type_map.get(self.tooling.resolver.normalize_type(parameter.schema_.type if parameter.schema_ else "string"), "str")
                if parameter.required:
                    func_params.append(f"{parameter.name}: {py_type}")
                else:
                    func_params.append(f"{parameter.name}: {py_type} = None")
            if has_body:
                func_params.append("data: dict = None")

            func_sig = "self" + (", " + ", ".join(func_params) if func_params else "")

            call_params: list[str] = []
            if query_params:
                query_dict = ", ".join(f'"{parameter.name}": {parameter.name}' for parameter in query_params)
                call_params.append(f"params={{{query_dict}}}")
            if has_body:
                call_params.append("data=data")
            call_str = ", ".join(call_params)

            lines.append(f"    def {name}({func_sig}) -> str:")
            lines.append(f"        return self._request('{method}', f'{api_path}'{', ' + call_str if call_str else ''})")
            lines.append("")

        return "\n".join(lines)


class MemsAPIDocGenerator:
    def __init__(self, tooling: OpenAPITooling):
        self.tooling = tooling

    def build_api_entries(self) -> list[ApiEntry]:
        entries: list[ApiEntry] = []
        for method, api_path, name, operation in self.tooling.iter_named_operations():
            params = self.tooling.extract_params(operation)
            body = self.tooling.has_body(operation)
            body_schema = self.tooling.resolver.extract_body_schema(operation) if body else None
            entries.append(
                ApiEntry(
                    method=method,
                    path=api_path,
                    name=name,
                    summary=operation.summary,
                    module=self.resolve_module(api_path),
                    operation=operation,
                    params=params,
                    body=body,
                    body_schema=body_schema,
                )
            )
        return entries

    def resolve_module(self, api_path: str) -> str:
        path_parts = api_path.strip("/").split("/") if api_path.strip("/") else []
        if not path_parts:
            return "other"

        module = path_parts[0]
        module_aliases = {
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
            return "lcc"
        if module.startswith("pscpu"):
            return "pscpu"
        return module_aliases.get(module, module)

    def render_header(self) -> str:
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
        return output

    def render_overview(self, entries: list[ApiEntry]) -> str:
        modules: dict[str, int] = {}
        for entry in entries:
            modules[entry.module] = modules.get(entry.module, 0) + 1

        output = "## API 概览\n\n"
        output += f"共 **{len(entries)}** 个API接口，分为以下模块：\n\n"
        for module, count in sorted(modules.items()):
            output += f"- **{module}**: {count} 个接口\n"
        output += "\n***\n\n"
        return output

    def render_enum_text(self, enum_values: list[Any]) -> str:
        if not enum_values:
            return ""
        return "可选值：" + "、".join(f"`{value}`" for value in enum_values)

    def render_one_of_text(self, one_of_types: list[str]) -> str:
        if not one_of_types:
            return ""
        return "可选结构：" + " | ".join(one_of_types)

    def render_param_line(self, parameter: Any) -> str:
        parameter_type = self.tooling.resolver.normalize_type(parameter.schema_.type if parameter.schema_ else "string")
        required = "必填" if parameter.required else "可选"
        line = f"  - `{parameter.name}` ({parameter.location}, {parameter_type}, {required})"

        details: list[str] = []
        metadata = self.tooling.resolver.build_schema_metadata(parameter.schema_)
        if metadata:
            details.append("元信息：" + ", ".join(metadata))

        schema = self.tooling.resolver.resolve_schema(parameter.schema_) or parameter.schema_
        enum_text = self.render_enum_text(self.tooling.resolver.merge_enum_values(schema))
        if enum_text:
            details.append(enum_text)
        one_of_text = self.render_one_of_text(self.tooling.resolver.collect_one_of_types(schema))
        if one_of_text:
            details.append(one_of_text)
        if parameter.description:
            details.insert(0, parameter.description)

        if details:
            line += ": " + "；".join(details)
        return line

    def render_module_sections(self, entries: list[ApiEntry]) -> str:
        grouped: dict[str, list[ApiEntry]] = {}
        for entry in entries:
            grouped.setdefault(entry.module, []).append(entry)

        output = ""
        for module, apis in sorted(grouped.items()):
            output += f"## {module.upper()} 模块\n\n"
            for api in apis:
                output += f"### {api.summary}\n\n"
                output += f"- **方法**: `{api.method}`\n"
                output += f"- **路径**: `{api.path}`\n"
                output += f"- **工具名**: `{api.name}`\n"
                if api.params:
                    output += "- **参数**:\n"
                    for parameter in api.params:
                        output += self.render_param_line(parameter) + "\n"
                if api.body:
                    output += "- **请求体**:\n\n"
                    table = self.tooling.render_body_table(api.body_schema)
                    output += table or "  - 无法解析请求体结构\n"
                    output += "\n"
                output += "\n"
            output += "***\n\n"
        return output

    def generate(self) -> str:
        entries = self.build_api_entries()
        return self.render_header() + self.render_overview(entries) + self.render_module_sections(entries)


class Generator:
    def __init__(self):
        self.spec = load_openapi_spec()
        self.tooling = OpenAPITooling(self.spec)
        self.method_generator = MemsAPIMethodGenerator(self.tooling)
        self.doc_generator = MemsAPIDocGenerator(self.tooling)

    def update_mems_agent(self) -> None:
        mems_agent_file = _OUTPUT_DIR / "mems_agent.py"
        with open(mems_agent_file, "r", encoding="utf-8") as file:
            content = file.read()

        methods_code = self.method_generator.generate()

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

        with open(mems_agent_file, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"Updated MemsAPI class in {mems_agent_file}")

    def update_docs(self) -> None:
        docs_file = _OUTPUT_DIR / "mems_api_docs.md"
        docs = self.doc_generator.generate()
        with open(docs_file, "w", encoding="utf-8") as file:
            file.write(docs)
        print(f"Updated {docs_file}")


def main() -> None:
    generator = Generator()
    print(f"Loaded OpenAPI spec with {len(generator.spec.paths)} paths")

    generator.update_mems_agent()
    generator.update_docs()

    print("\nDone! All files updated from openapi_mems.json")


if __name__ == "__main__":
    main()
