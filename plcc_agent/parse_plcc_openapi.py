
import json

def resolve_schema_ref(schema, components):
    if not isinstance(schema, dict):
        return schema
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref.startswith("#/components/schemas/"):
            schema_name = ref.split("/")[-1]
            if schema_name in components.get("schemas", {}):
                return components["schemas"][schema_name]
    return schema

def parse_schema(schema, components, depth=0):
    if depth > 10:
        return {"type": "object", "description": "Recursive structure"}
    
    if not isinstance(schema, dict):
        return schema
    
    schema = resolve_schema_ref(schema, components)
    
    result = {}
    
    if "type" in schema:
        result["type"] = schema["type"]
    
    if "description" in schema:
        result["description"] = schema["description"]
    
    if "format" in schema:
        result["format"] = schema["format"]
    
    if "properties" in schema:
        result["properties"] = {}
        for prop_name, prop_schema in schema["properties"].items():
            result["properties"][prop_name] = parse_schema(prop_schema, components, depth + 1)
    
    if "items" in schema:
        result["items"] = parse_schema(schema["items"], components, depth + 1)
    
    if "required" in schema:
        result["required"] = schema["required"]
    
    if "oneOf" in schema:
        result["oneOf"] = [parse_schema(s, components, depth + 1) for s in schema["oneOf"]]
    
    if "additionalProperties" in schema:
        if isinstance(schema["additionalProperties"], dict):
            result["additionalProperties"] = parse_schema(schema["additionalProperties"], components, depth + 1)
        else:
            result["additionalProperties"] = schema["additionalProperties"]
    
    if "prefixItems" in schema:
        result["prefixItems"] = [parse_schema(s, components, depth + 1) for s in schema["prefixItems"]]
    
    if "minItems" in schema:
        result["minItems"] = schema["minItems"]
    
    if "maxItems" in schema:
        result["maxItems"] = schema["maxItems"]
    
    if "minimum" in schema:
        result["minimum"] = schema["minimum"]
    
    if "maximum" in schema:
        result["maximum"] = schema["maximum"]
    
    return result

def parse_parameters(parameters, components):
    result = []
    for param in parameters:
        param_info = {
            "name": param.get("name"),
            "in": param.get("in"),
            "description": param.get("description", ""),
            "required": param.get("required", False)
        }
        if "schema" in param:
            param_info["schema"] = parse_schema(param["schema"], components)
        result.append(param_info)
    return result

def parse_request_body(request_body, components):
    if "content" in request_body:
        for content_type, content_info in request_body["content"].items():
            if "schema" in content_info:
                return {
                    "contentType": content_type,
                    "description": request_body.get("description", ""),
                    "required": request_body.get("required", False),
                    "schema": parse_schema(content_info["schema"], components)
                }
    return None

def parse_responses(responses, components):
    result = {}
    for status_code, response_info in responses.items():
        response_data = {
            "description": response_info.get("description", "")
        }
        if "content" in response_info:
            content_list = []
            for content_type, content_info in response_info["content"].items():
                content_data = {
                    "contentType": content_type
                }
                if "schema" in content_info:
                    content_data["schema"] = parse_schema(content_info["schema"], components)
                content_list.append(content_data)
            response_data["content"] = content_list
        result[status_code] = response_data
    return result

def main():
    with open('plcc_agent/openapi.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    components = data.get("components", {})
    
    print('Title:', data["info"]["title"])
    print('Version:', data["info"]["version"])
    print('Paths count:', len(data["paths"]))
    print('\nAvailable paths:')
    
    apis = []
    for path, methods in data["paths"].items():
        for method, operation in methods.items():
            print('  ', method.upper(), path)
            
            api_info = {
                "method": method,
                "path": path,
                "summary": operation.get("summary", ""),
                "operationId": operation.get("operationId", ""),
                "tags": operation.get("tags", [])
            }
            
            if "parameters" in operation:
                api_info["parameters"] = parse_parameters(operation["parameters"], components)
                print('    Parameters:', len(api_info["parameters"]))
            
            if "requestBody" in operation:
                api_info["requestBody"] = parse_request_body(operation["requestBody"], components)
                print('    Has Request Body: True')
            
            if "responses" in operation:
                api_info["responses"] = parse_responses(operation["responses"], components)
                print('    Responses:', list(api_info["responses"].keys()))
            
            apis.append(api_info)
    
    print('\nTotal APIs:', len(apis))
    
    with open('plcc_agent/api_list.json', 'w', encoding='utf-8') as f:
        json.dump(apis, f, ensure_ascii=False, indent=2)
    
    print('API list saved to plcc_agent/api_list.json')

if __name__ == '__main__':
    main()

