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

    for _, _, name, operation in tooling.iter_named_operations():
        params = tooling.extract_params(operation)
        path_params = [parameter for parameter in params if parameter.location == "path"]
        query_params = [parameter for parameter in params if parameter.location == "query"]
        body_schema = tooling.resolver.extract_body_schema(operation) if tooling.has_body(operation) else None
        tools.append(
            ToolInfo(
                name=name,
                description=tooling.build_description(operation, path_params, query_params, body_schema),
                func=getattr(mems_api, name),
                parameters=tooling.build_tool_parameters(operation, path_params, query_params, body_schema),
            )
        )

    return tools
