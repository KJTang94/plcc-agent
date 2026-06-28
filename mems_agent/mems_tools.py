from __future__ import annotations

import inspect
from typing import Any

from openapi_shared import ToolInfo, OpenAPITooling, load_openapi_spec


def _inspect_method_body(func: Any) -> tuple[bool, bool]:
    """检查实际方法签名，返回 (是否接受 data 请求体, data 是否可选)。
    用于校正 OpenAPI 描述与方法真实行为的不一致：
    部分上传类方法虽在 spec 中声明必填二进制请求体，但实现里 data 可选，
    未提供时会自动从配置文件读取，无需 LLM 构造文件内容。"""
    try:
        sig = inspect.signature(func)
    except (TypeError, ValueError):
        return True, False
    data_param = sig.parameters.get("data")
    if data_param is None:
        return False, False
    return True, data_param.default is not inspect.Parameter.empty


def create_tools(mems_api: Any) -> list[ToolInfo]:
    spec = load_openapi_spec()
    tooling = OpenAPITooling(spec)

    tools = [
        ToolInfo(
            name="login",
            description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。",
            func=mems_api.login,
        )
    ]

    missing_methods: list[str] = []
    for method, path, name, operation in tooling.iter_named_operations():
        if not hasattr(mems_api, name):
            missing_methods.append(name)
            continue
        func = getattr(mems_api, name)
        params = tooling.extract_params(operation)
        path_params = [parameter for parameter in params if parameter.location == "path"]
        query_params = [parameter for parameter in params if parameter.location == "query"]
        body_schema = tooling.resolver.extract_body_schema(operation) if tooling.has_body(operation) else None

        # 用实际方法签名校正请求体描述，消除 spec 与实现的不一致
        accepts_body, body_optional = _inspect_method_body(func)
        description = tooling.build_description(operation, path_params, query_params, body_schema, method, path)
        tool_parameters = tooling.build_tool_parameters(operation, path_params, query_params, body_schema)

        if body_schema is not None and not accepts_body:
            # spec 声明了请求体但方法不接受 data：去掉 data 参数，明确告知无需请求体
            tool_parameters = [param for param in tool_parameters if param.get("name") != "data"]
            description += "。【调用说明】此接口无需提供请求体，直接调用即可（不要传 data 参数）。"
        elif body_schema is not None and body_optional:
            # 方法 data 可选：未提供时自动从配置文件读取，避免 LLM 因无法构造文件内容而拒绝执行
            for param in tool_parameters:
                if param.get("name") == "data":
                    param["required"] = False
            description += "。【调用说明】data 为可选请求体；若未提供，系统会自动从配置文件读取所需文件内容并构造请求体，因此即使用户未提供文件也可直接调用（无需向用户索要文件）。"

        existing_param_names = {param.get("name") for param in tool_parameters}
        try:
            sig = inspect.signature(func)
            for param_name, sig_param in sig.parameters.items():
                if param_name in existing_param_names or param_name in ("self", "data"):
                    continue
                if sig_param.default is inspect.Parameter.empty:
                    continue
                if param_name == "file_path":
                    tool_parameters.append({
                        "name": "file_path",
                        "type": "string",
                        "required": False,
                        "description": "用户指定的本地文件路径；未提供时使用配置文件中的默认文件路径。"
                    })
                    description += "。【文件说明】用户若指定单个本地文件路径，请通过 file_path 传入；未指定则使用默认配置文件。"
                elif param_name == "file_paths":
                    tool_parameters.append({
                        "name": "file_paths",
                        "type": "array[string]",
                        "required": False,
                        "description": "用户指定的本地文件路径列表，也可由多个路径组成；未提供时使用配置文件中的默认文件路径。"
                    })
                    description += "。【文件说明】用户若指定多个本地文件路径，请通过 file_paths 传入；未指定则使用默认配置文件。"
        except (TypeError, ValueError):
            pass

        tools.append(
            ToolInfo(
                name=name,
                description=description,
                func=func,
                parameters=tool_parameters,
            )
        )

    if missing_methods:
        raise RuntimeError(
            "OpenAPI 工具与 MemsAPI 方法不一致，以下接口在 mems_api.py 中缺少对应方法："
            + "、".join(missing_methods)
            + "。请运行 generate_from_openapi.py 重新生成 mems_api.py。"
        )

    return tools
