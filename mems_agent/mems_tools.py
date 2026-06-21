from __future__ import annotations

from typing import Any

from openapi_shared import ToolInfo, OpenAPITooling, load_openapi_spec


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
        params = tooling.extract_params(operation)
        path_params = [parameter for parameter in params if parameter.location == "path"]
        query_params = [parameter for parameter in params if parameter.location == "query"]
        body_schema = tooling.resolver.extract_body_schema(operation) if tooling.has_body(operation) else None
        tools.append(
            ToolInfo(
                name=name,
                description=tooling.build_description(operation, path_params, query_params, body_schema, method, path),
                func=getattr(mems_api, name),
                parameters=tooling.build_tool_parameters(operation, path_params, query_params, body_schema),
            )
        )

    if missing_methods:
        raise RuntimeError(
            "OpenAPI 工具与 MemsAPI 方法不一致，以下接口在 mems_api.py 中缺少对应方法："
            + "、".join(missing_methods)
            + "。请运行 generate_from_openapi.py 重新生成 mems_api.py。"
        )

    return tools
