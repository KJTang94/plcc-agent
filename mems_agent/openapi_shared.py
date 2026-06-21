from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

_OPENAPI_FILE = Path(__file__).parent / "openapi_mems.json"


class OpenAPIMediaType(BaseModel):
    model_config = ConfigDict(extra="allow")

    schema_: Optional["OpenAPISchema"] = Field(default=None, alias="schema")


class OpenAPIRequestBody(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: str = ""
    content: dict[str, OpenAPIMediaType] = Field(default_factory=dict)
    required: bool = False


class OpenAPIParameter(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    location: str = Field(alias="in")
    description: str = ""
    required: bool = False
    schema_: Optional["OpenAPISchema"] = Field(default=None, alias="schema")


class OpenAPISchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ref: Optional[str] = Field(default=None, alias="$ref")
    type: Optional[str | list[str]] = None
    description: str = ""
    properties: dict[str, "OpenAPISchema"] = Field(default_factory=dict)
    items: Optional["OpenAPISchema | bool"] = None
    required: list[str] = Field(default_factory=list)
    one_of: list["OpenAPISchema"] = Field(default_factory=list, alias="oneOf")
    any_of: list["OpenAPISchema"] = Field(default_factory=list, alias="anyOf")
    all_of: list["OpenAPISchema"] = Field(default_factory=list, alias="allOf")
    additional_properties: Optional["OpenAPISchema | bool"] = Field(default=None, alias="additionalProperties")
    title: str = ""
    format: str = ""
    default: Any = None
    enum: list[Any] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def _normalize_nested_schema(cls, value: Any) -> Any:
        if not isinstance(value, dict):
            return value

        normalized = dict(value)
        for key in ("properties",):
            if isinstance(normalized.get(key), dict):
                normalized[key] = {
                    name: schema if isinstance(schema, dict) else schema
                    for name, schema in normalized[key].items()
                }
        return normalized

    @property
    def nullable(self) -> bool:
        if isinstance(self.type, list):
            return "null" in self.type
        return False


class OpenAPIOperation(BaseModel):
    model_config = ConfigDict(extra="allow")

    summary: str = ""
    operation_id: str = Field(default="", alias="operationId")
    parameters: list[OpenAPIParameter] = Field(default_factory=list)
    request_body: Optional[OpenAPIRequestBody] = Field(default=None, alias="requestBody")


class OpenAPIComponents(BaseModel):
    model_config = ConfigDict(extra="allow")

    schemas: dict[str, OpenAPISchema] = Field(default_factory=dict)


class OpenAPIPathItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    get: Optional[OpenAPIOperation] = None
    post: Optional[OpenAPIOperation] = None
    put: Optional[OpenAPIOperation] = None
    delete: Optional[OpenAPIOperation] = None

    def iter_operations(self) -> list[tuple[str, OpenAPIOperation]]:
        operations: list[tuple[str, OpenAPIOperation]] = []
        for method in ("get", "post", "put", "delete"):
            operation = getattr(self, method)
            if operation is not None:
                operations.append((method, operation))
        return operations


class OpenAPISpec(BaseModel):
    model_config = ConfigDict(extra="allow")

    openapi: str = ""
    paths: dict[str, OpenAPIPathItem] = Field(default_factory=dict)
    components: OpenAPIComponents = Field(default_factory=OpenAPIComponents)


class ParameterInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    type: str
    required: bool
    description: str = ""
    children: list["ParameterInfo"] = Field(default_factory=list)
    enum: list[Any] = Field(default_factory=list)
    format: str = ""
    default: Any = None
    nullable: bool = False
    additional_properties: Optional[str] = None
    one_of_types: list[str] = Field(default_factory=list)

    def to_legacy_dict(self) -> dict[str, Any]:
        data = {
            "name": self.name,
            "type": self.type,
            "required": self.required,
            "description": self.description,
        }
        if self.children:
            data["children"] = [child.to_legacy_dict() for child in self.children]
        if self.enum:
            data["enum"] = self.enum
        if self.format:
            data["format"] = self.format
        if self.default is not None:
            data["default"] = self.default
        if self.nullable:
            data["nullable"] = self.nullable
        if self.additional_properties is not None:
            data["additional_properties"] = self.additional_properties
        if self.one_of_types:
            data["one_of_types"] = self.one_of_types
        return data


class ToolInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    description: str
    func: Callable[..., Any]
    parameters: list[dict[str, Any]] = Field(default_factory=list)


class OpenAPIResolver:
    def __init__(self, spec: OpenAPISpec):
        self.spec = spec

    def normalize_type(self, value: Any) -> str:
        if isinstance(value, list):
            non_null = [item for item in value if item != "null"]
            return str(non_null[0]) if non_null else "string"
        if isinstance(value, str) and value:
            return value
        return "string"

    def schema_type_name(self, schema: Optional[OpenAPISchema]) -> str:
        if schema is None:
            return "any"
        if schema.ref:
            return schema.ref.split("/")[-1]
        one_of_types = self.collect_one_of_types(schema)
        if one_of_types:
            return "oneOf[" + " | ".join(one_of_types) + "]"
        schema_type = self.normalize_type(schema.type)
        if schema_type == "array":
            item_schema = schema.items if isinstance(schema.items, OpenAPISchema) else None
            return f"array[{self.schema_type_name(item_schema)}]"
        if schema_type == "object":
            if isinstance(schema.additional_properties, OpenAPISchema):
                return f"object[string, {self.schema_type_name(schema.additional_properties)}]"
            if schema.additional_properties is True:
                return "object[string, any]"
            return "object"
        return schema_type

    def resolve_schema(self, schema: Optional[OpenAPISchema], seen_refs: Optional[set[str]] = None) -> Optional[OpenAPISchema]:
        if schema is None:
            return None
        if seen_refs is None:
            seen_refs = set()

        if schema.ref:
            ref = schema.ref
            if ref in seen_refs:
                return schema
            seen_refs.add(ref)
            if ref.startswith("#/components/schemas/"):
                ref_name = ref.split("/")[-1]
                target = self.spec.components.schemas.get(ref_name)
                if target is not None:
                    return self.resolve_schema(target, seen_refs)
            return schema

        if schema.all_of:
            merged_description = schema.description
            merged_required: list[str] = []
            merged_properties: dict[str, OpenAPISchema] = {}
            merged_enum: list[Any] = []
            merged_format = schema.format
            merged_default = schema.default
            merged_nullable = schema.nullable
            merged_additional_properties = schema.additional_properties
            merged_one_of: list[OpenAPISchema] = []
            merged_any_of: list[OpenAPISchema] = []
            for item in schema.all_of:
                resolved = self.resolve_schema(item, seen_refs.copy())
                if resolved is None:
                    continue
                merged_properties.update(resolved.properties)
                merged_required.extend(resolved.required)
                if not merged_description and resolved.description:
                    merged_description = resolved.description
                if resolved.enum:
                    merged_enum.extend(resolved.enum)
                if not merged_format and resolved.format:
                    merged_format = resolved.format
                if merged_default is None and resolved.default is not None:
                    merged_default = resolved.default
                merged_nullable = merged_nullable or resolved.nullable
                if merged_additional_properties is None:
                    merged_additional_properties = resolved.additional_properties
                merged_one_of.extend(resolved.one_of)
                merged_any_of.extend(resolved.any_of)
            merged_type = schema.type or "object"
            if merged_nullable and isinstance(merged_type, str):
                merged_type = [merged_type, "null"]
            return OpenAPISchema(
                type=merged_type,
                description=merged_description,
                properties=merged_properties,
                required=list(dict.fromkeys(merged_required)),
                enum=list(dict.fromkeys(merged_enum)),
                format=merged_format,
                default=merged_default,
                additionalProperties=merged_additional_properties,
                oneOf=merged_one_of,
                anyOf=merged_any_of,
            )

        return schema

    def resolve_union_candidates(self, schema: Optional[OpenAPISchema], seen_refs: Optional[set[str]] = None) -> list[OpenAPISchema]:
        schema = self.resolve_schema(schema, seen_refs)
        if schema is None:
            return []

        candidates: list[OpenAPISchema] = []
        for choices in (schema.one_of, schema.any_of):
            for item in choices:
                resolved = self.resolve_schema(item, (seen_refs or set()).copy())
                if resolved is not None and self.normalize_type(resolved.type) != "null":
                    candidates.append(resolved)
        return candidates

    def collect_one_of_types(self, schema: Optional[OpenAPISchema]) -> list[str]:
        candidates = self.resolve_union_candidates(schema)
        if not candidates:
            return []

        seen: list[str] = []
        for candidate in candidates:
            candidate_type = self.normalize_type(candidate.type)
            if candidate_type == "object" and candidate.properties:
                prop_names = list(candidate.properties.keys())[:3]
                label = "object{" + ", ".join(prop_names) + (", ..." if len(candidate.properties) > 3 else "") + "}"
            elif candidate_type == "array":
                item_schema = candidate.items if isinstance(candidate.items, OpenAPISchema) else None
                label = f"array[{self.schema_type_name(item_schema)}]"
            else:
                label = self.schema_type_name(candidate)
            if label not in seen:
                seen.append(label)
        return seen

    def merge_enum_values(self, schema: Optional[OpenAPISchema]) -> list[Any]:
        schema = self.resolve_schema(schema)
        if schema is None:
            return []

        values: list[Any] = list(schema.enum)
        for candidate in self.resolve_union_candidates(schema):
            values.extend(candidate.enum)
        return list(dict.fromkeys(values))

    def extract_body_schema(self, operation: OpenAPIOperation) -> Optional[OpenAPISchema]:
        request_body = operation.request_body
        if request_body is None:
            return None
        for content_type in ("application/json", "application/octet-stream", "multipart/form-data"):
            media = request_body.content.get(content_type)
            if media and media.schema_ is not None:
                return self.resolve_schema(media.schema_)
        for media in request_body.content.values():
            if media.schema_ is not None:
                return self.resolve_schema(media.schema_)
        return None

    def build_schema_metadata(self, schema: Optional[OpenAPISchema]) -> list[str]:
        schema = self.resolve_schema(schema)
        if schema is None:
            return []

        metadata: list[str] = []
        enum_values = self.merge_enum_values(schema)
        one_of_types = self.collect_one_of_types(schema)
        if schema.format:
            metadata.append(f"format={schema.format}")
        if enum_values:
            metadata.append("enum=" + "/".join(str(item) for item in enum_values))
        if schema.default is not None:
            metadata.append(f"default={schema.default}")
        if schema.nullable:
            metadata.append("nullable=true")
        if one_of_types:
            metadata.append("oneOf=" + " | ".join(one_of_types))
        if isinstance(schema.additional_properties, OpenAPISchema):
            metadata.append(f"additionalProperties={self.schema_type_name(schema.additional_properties)}")
        elif schema.additional_properties is True:
            metadata.append("additionalProperties=any")
        elif schema.additional_properties is False:
            metadata.append("additionalProperties=false")
        return metadata

    def describe_schema_fields(
        self,
        schema: Optional[OpenAPISchema],
        prefix: str = "",
        depth: int = 0,
        max_depth: int = 2,
    ) -> list[str]:
        schema = self.resolve_schema(schema)
        if schema is None or depth > max_depth:
            return []

        candidates = self.resolve_union_candidates(schema)
        if candidates:
            results: list[str] = []
            type_summary = " | ".join(self.collect_one_of_types(schema))
            results.append(f"{prefix} (oneOf[{type_summary}])")
            for index, candidate in enumerate(candidates, start=1):
                branch_prefix = f"{prefix}.oneOf[{index}]" if prefix else f"oneOf[{index}]"
                results.extend(self.describe_schema_fields(candidate, prefix=branch_prefix, depth=depth + 1, max_depth=max_depth))
            return results

        schema_type = self.schema_type_name(schema)
        results: list[str] = []

        if schema_type.startswith("array["):
            item_schema = self.resolve_schema(schema.items) if isinstance(schema.items, OpenAPISchema) else None
            item_type = self.schema_type_name(item_schema)
            item_desc = schema.description or (item_schema.description if item_schema else "")
            text = f"{prefix} ({schema_type})"
            metadata = self.build_schema_metadata(schema)
            if metadata:
                text += f" [{', '.join(metadata)}]"
            if item_desc:
                text += f" - {item_desc}"
            results.append(text)
            if item_type == "object" or item_type.startswith("object[") or item_type.startswith("oneOf["):
                results.extend(
                    self.describe_schema_fields(
                        item_schema,
                        prefix=f"{prefix}[]",
                        depth=depth + 1,
                        max_depth=max_depth,
                    )
                )
            return results

        if not (schema_type == "object" or schema_type.startswith("object[")):
            text = f"{prefix} ({schema_type})"
            metadata = self.build_schema_metadata(schema)
            if metadata:
                text += f" [{', '.join(metadata)}]"
            if schema.description:
                text += f" - {schema.description}"
            results.append(text)
            return results

        required_fields = set(schema.required)
        for prop_name, prop_schema in schema.properties.items():
            resolved_prop = self.resolve_schema(prop_schema) or prop_schema
            prop_type = self.schema_type_name(resolved_prop)
            required = "必填" if prop_name in required_fields else "可选"
            full_name = f"{prefix}.{prop_name}" if prefix else prop_name
            desc = resolved_prop.description or prop_schema.description
            text = f"{full_name} ({prop_type}, {required})"
            metadata = self.build_schema_metadata(resolved_prop)
            if metadata:
                text += f" [{', '.join(metadata)}]"
            if desc:
                text += f" - {desc}"
            results.append(text)
            if depth < max_depth and (prop_type == "object" or prop_type.startswith("object[") or prop_type.startswith("oneOf[")):
                results.extend(
                    self.describe_schema_fields(
                        resolved_prop,
                        prefix=full_name,
                        depth=depth + 1,
                        max_depth=max_depth,
                    )
                )
            elif depth < max_depth and prop_type.startswith("array["):
                item_schema = self.resolve_schema(resolved_prop.items) if isinstance(resolved_prop.items, OpenAPISchema) else None
                item_type = self.schema_type_name(item_schema)
                if item_type == "object" or item_type.startswith("object[") or item_type.startswith("oneOf["):
                    results.extend(
                        self.describe_schema_fields(
                            item_schema,
                            prefix=f"{full_name}[]",
                            depth=depth + 1,
                            max_depth=max_depth,
                        )
                    )
        return results

    def additional_properties_label(self, schema: Optional[OpenAPISchema]) -> Optional[str]:
        schema = self.resolve_schema(schema)
        if schema is None:
            return None
        if isinstance(schema.additional_properties, OpenAPISchema):
            return self.schema_type_name(schema.additional_properties)
        if schema.additional_properties is True:
            return "any"
        if schema.additional_properties is False:
            return "false"
        return None

    def parameter_info_from_schema(
        self,
        name: str,
        schema: Optional[OpenAPISchema],
        required: bool,
        description: str = "",
    ) -> ParameterInfo:
        resolved = self.resolve_schema(schema) or schema or OpenAPISchema()
        return ParameterInfo(
            name=name,
            type=self.schema_type_name(resolved),
            required=required,
            description=description or resolved.description,
            children=self.render_children(resolved),
            enum=self.merge_enum_values(resolved),
            format=resolved.format,
            default=resolved.default,
            nullable=resolved.nullable,
            additional_properties=self.additional_properties_label(resolved),
            one_of_types=self.collect_one_of_types(resolved),
        )

    def render_children(self, schema: Optional[OpenAPISchema]) -> list[ParameterInfo]:
        schema = self.resolve_schema(schema)
        if schema is None:
            return []

        candidates = self.resolve_union_candidates(schema)
        if candidates:
            children: list[ParameterInfo] = []
            for index, candidate in enumerate(candidates, start=1):
                children.append(
                    ParameterInfo(
                        name=f"oneOf[{index}]",
                        type=self.schema_type_name(candidate),
                        required=True,
                        description=candidate.description,
                        children=self.render_children(candidate),
                        enum=self.merge_enum_values(candidate),
                        format=candidate.format,
                        default=candidate.default,
                        nullable=candidate.nullable,
                        additional_properties=self.additional_properties_label(candidate),
                        one_of_types=self.collect_one_of_types(candidate),
                    )
                )
            return children

        schema_type = self.schema_type_name(schema)
        children: list[ParameterInfo] = []

        if schema_type == "object" or schema_type.startswith("object["):
            required_fields = set(schema.required)
            for prop_name, prop_schema in schema.properties.items():
                children.append(
                    self.parameter_info_from_schema(
                        name=prop_name,
                        schema=prop_schema,
                        required=prop_name in required_fields,
                        description=prop_schema.description,
                    )
                )
        elif schema_type.startswith("array["):
            item_schema = self.resolve_schema(schema.items) if isinstance(schema.items, OpenAPISchema) else None
            if item_schema is not None:
                item_type = self.schema_type_name(item_schema)
                item_children = self.render_children(item_schema)
                if item_children or self.merge_enum_values(item_schema) or item_schema.format or item_schema.default is not None or item_schema.nullable or self.additional_properties_label(item_schema) is not None or self.collect_one_of_types(item_schema):
                    children.append(
                        ParameterInfo(
                            name="[]",
                            type=item_type,
                            required=True,
                            description=item_schema.description or schema.description,
                            children=item_children,
                            enum=self.merge_enum_values(item_schema),
                            format=item_schema.format,
                            default=item_schema.default,
                            nullable=item_schema.nullable,
                            additional_properties=self.additional_properties_label(item_schema),
                            one_of_types=self.collect_one_of_types(item_schema),
                        )
                    )
        return children


class OpenAPITooling:
    def __init__(self, spec: OpenAPISpec):
        self.spec = spec
        self.resolver = OpenAPIResolver(spec)

    def clean_path(self, path: str) -> str:
        return re.sub(r"\}+", "}", path)

    def escape_str(self, value: str) -> str:
        value = value.replace("\\", "\\\\")
        value = value.replace('"', '\\"')
        value = value.replace("\n", " ")
        value = value.replace("\r", "")
        return value

    def path_to_method_name(self, method: str, path: str, summary: str) -> str:
        path_part = path.replace("/api/v1/", "").strip("/")
        parts = path_part.split("/") if path_part else []

        action_prefix = {
            "GET": "get",
            "POST": "add",
            "PUT": "update",
            "DELETE": "delete",
        }.get(method, method.lower())

        name_parts: list[str] = []
        skip_next = False
        for index, part in enumerate(parts):
            if skip_next:
                skip_next = False
                continue
            if part.startswith("{") and part.endswith("}"):
                param_name = part[1:-1]
                if index > 0 and parts[index - 1] not in ("by_role", "by_user", "by_user_group", "by_ids", "by_dev"):
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
        raw_name = re.sub(r"_+", "_", raw_name)
        return raw_name.strip("_")

    def extract_params(self, operation: OpenAPIOperation) -> list[OpenAPIParameter]:
        return [parameter for parameter in operation.parameters if parameter.location != "header"]

    def has_body(self, operation: OpenAPIOperation) -> bool:
        return operation.request_body is not None

    def iter_named_operations(self) -> list[tuple[str, str, str, OpenAPIOperation]]:
        operations: list[tuple[str, str, str, OpenAPIOperation]] = []
        seen_names: set[str] = set()
        counters: dict[str, int] = {}

        for raw_path, path_item in sorted(self.spec.paths.items()):
            api_path = self.clean_path(raw_path.replace("/api/v1", ""))
            for method, operation in path_item.iter_operations():
                name = self.path_to_method_name(method.upper(), api_path, operation.summary)
                if name in seen_names:
                    counters[name] = counters.get(name, 0) + 1
                    name = f"{name}_{counters[name]}"
                seen_names.add(name)
                operations.append((method.upper(), api_path, name, operation))
        return operations

    def build_description(
        self,
        operation: OpenAPIOperation,
        path_params: list[OpenAPIParameter],
        query_params: list[OpenAPIParameter],
        body_schema: Optional[OpenAPISchema],
        method: str = "",
        path: str = "",
    ) -> str:
        description_parts: list[str] = []
        for parameter in path_params + query_params:
            parameter_type = self.resolver.normalize_type(parameter.schema_.type if parameter.schema_ else "string")
            required = "必填" if parameter.required else "可选"
            text = f"{parameter.name} ({parameter_type}, {required})"
            metadata = self.resolver.build_schema_metadata(parameter.schema_)
            if metadata:
                text += f" [{', '.join(metadata)}]"
            if parameter.description:
                text += f" - {parameter.description}"
            description_parts.append(text)

        if body_schema is not None:
            body_type = self.resolver.schema_type_name(body_schema)
            body_desc = f"data ({body_type or 'dict'}) - 请求体数据"
            body_field_descs = self.resolver.describe_schema_fields(body_schema, prefix="data")
            if body_field_descs:
                body_desc += "，字段：" + "；".join(body_field_descs)
            description_parts.append(body_desc)

        description = operation.summary
        # 前置 HTTP 方法与路径，提升相似中文描述之间的可区分度（同时用于工具索引与模型选择）
        if method and path:
            prefix = f"[{method} {path}]"
            description = f"{prefix} {description}" if description else prefix
        if description_parts:
            description += "。参数：" + ", ".join(description_parts)
        return description

    def build_tool_parameters(
        self,
        operation: OpenAPIOperation,
        path_params: list[OpenAPIParameter],
        query_params: list[OpenAPIParameter],
        body_schema: Optional[OpenAPISchema],
    ) -> list[dict[str, Any]]:
        tool_params: list[dict[str, Any]] = []
        for parameter in path_params + query_params:
            tool_params.append(
                self.resolver.parameter_info_from_schema(
                    name=parameter.name,
                    schema=parameter.schema_,
                    required=parameter.required,
                    description=parameter.description,
                ).to_legacy_dict()
            )
        if body_schema is not None:
            body_description = "请求体数据"
            body_field_descs = self.resolver.describe_schema_fields(body_schema, prefix="data")
            if body_field_descs:
                body_description += "；字段：" + "；".join(body_field_descs)
            tool_params.append(
                self.resolver.parameter_info_from_schema(
                    name="data",
                    schema=body_schema,
                    required=operation.request_body.required if operation.request_body else True,
                    description=body_description,
                ).to_legacy_dict()
            )
        return tool_params

    def render_body_table(self, schema: Optional[OpenAPISchema]) -> str:
        rows = self.resolver.render_children(schema)
        if not rows:
            return ""
        output = "| 字段名 | 类型 | 必填 | 说明 |\n"
        output += "| --- | --- | --- | --- |\n"
        output_lines: list[str] = []

        def walk(items: list[ParameterInfo], prefix: str = "") -> None:
            for item in items:
                name = item.name
                child_prefix = f"{prefix}.{name}" if prefix and name != "[]" else (prefix if name == "[]" else name)
                if name == "[]":
                    child_prefix = f"{prefix}[]" if prefix else "[]"
                output_name = child_prefix
                req = "是" if item.required else "否"
                desc_parts: list[str] = []
                if item.description:
                    desc_parts.append(item.description)
                if item.enum:
                    desc_parts.append("可选值：" + "、".join(str(enum_item) for enum_item in item.enum))
                if item.one_of_types:
                    desc_parts.append("可选结构：" + " | ".join(item.one_of_types))
                if item.format:
                    desc_parts.append(f"格式：{item.format}")
                if item.default is not None:
                    desc_parts.append(f"默认值：{item.default}")
                if item.nullable:
                    desc_parts.append("允许空值")
                if item.additional_properties is not None:
                    desc_parts.append(f"额外属性：{item.additional_properties}")
                desc = "；".join(desc_parts)
                output_lines.append(f"| {output_name} | {item.type} | {req} | {desc} |")
                if item.children:
                    walk(item.children, output_name)

        walk(rows)
        return output + "\n".join(output_lines) + "\n"


def load_openapi_spec(file_path: Path = _OPENAPI_FILE) -> OpenAPISpec:
    with open(file_path, "r", encoding="utf-8") as file:
        return OpenAPISpec.model_validate(json.load(file))
