import re

with open('c:/Users/tangk/Documents/trae_projects/plcc-agent/apidoc_mems/docs/assets/main.bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 解码Unicode转义字符
def decode_unicode_escape(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '\\' and i + 1 < len(s) and s[i+1] == 'u':
            if i + 5 <= len(s):
                hex_str = s[i+2:i+6]
                try:
                    code_point = int(hex_str, 16)
                    result.append(chr(code_point))
                    i += 6
                    continue
                except ValueError:
                    pass
        result.append(s[i])
        i += 1
    return ''.join(result)

content = decode_unicode_escape(content)

# 提取字段值
def extract_field(s, field_name):
    pattern = r'(?<![a-zA-Z])' + re.escape(field_name) + r':"([^"]+)"'
    match = re.search(pattern, s)
    if match:
        return match.group(1)
    return None

# 解析字段信息（允许 type 字段缺失）
def parse_fields(field_str):
    fields = []
    field_obj_pattern = r'\{([^}]+)\}'
    field_objs = re.findall(field_obj_pattern, field_str)
    
    for obj_content in field_objs:
        group_match = re.search(r'group:"([^"]+)"', obj_content)
        type_match = re.search(r'type:"([^"]+)"', obj_content)
        optional_match = re.search(r'optional:(!?\d)', obj_content)
        field_match = re.search(r'field:"([^"]+)"', obj_content)
        desc_match = re.search(r'description:"([^"]+)"', obj_content)
        
        # 只要求 group 和 field 字段必须存在，其他字段可选
        if group_match and field_match:
            fields.append({
                'name': field_match.group(1),
                'type': type_match.group(1) if type_match else '',
                'description': desc_match.group(1) if desc_match else '',
                'optional': optional_match.group(1) == '!0' if optional_match else False
            })
    return fields

# 使用括号匹配找到数组内容
def extract_array_content(s, start_marker):
    start_pos = s.find(start_marker)
    if start_pos == -1:
        return None
    
    array_start = s.find('[', start_pos + len(start_marker))
    if array_start == -1:
        return None
    
    depth = 1
    i = array_start + 1
    while i < len(s) and depth > 0:
        if s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
        elif s[i] == '"':
            i += 1
            while i < len(s) and s[i] != '"':
                if s[i] == '\\':
                    i += 2
                else:
                    i += 1
        i += 1
    
    array_end = i - 1
    return s[array_start+1:array_end]

# 使用括号匹配找到完整的API对象
def find_api_end(s, start_pos):
    if s[start_pos] != '{':
        brace_start = s.find('{', start_pos)
        if brace_start == -1:
            return len(s)
        start_pos = brace_start
    
    depth = 1
    i = start_pos + 1
    while i < len(s) and depth > 0:
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
        elif s[i] == '"':
            i += 1
            while i < len(s) and s[i] != '"':
                if s[i] == '\\':
                    i += 2
                else:
                    i += 1
        i += 1
    
    return i

# ============== 提取API接口 ==============
api_pattern = r'\{type:"(\w+)",url:"/api/v1/[^"]+"'
api_matches = list(re.finditer(api_pattern, content))

apis = []
for match in api_matches:
    start_pos = match.start()
    end_pos = find_api_end(content, start_pos)
    
    api_str = content[start_pos:end_pos]
    method = extract_field(api_str, 'type')
    url = extract_field(api_str, 'url')
    title = extract_field(api_str, 'title')
    
    if method and url and url.startswith('/api/v1/'):
        params = []
        body = []
        success = []
        
        # 路径参数
        param_pattern = r'parameter:\{fields:\{Parameter:\[([^\]]+)\]\}\}'
        param_match = re.search(param_pattern, api_str)
        if param_match:
            params = parse_fields(param_match.group(1))
        
        # 查询参数
        query_content = extract_array_content(api_str, 'query:')
        if query_content:
            query_fields = parse_fields(query_content)
            params.extend(query_fields)
        
        # 请求体
        body_content = extract_array_content(api_str, 'body:')
        if body_content:
            body = parse_fields(body_content)
        
        # 成功响应
        success_start = api_str.find('success:{')
        if success_start != -1:
            fields_start = api_str.find('fields:{', success_start)
            if fields_start != -1:
                success_content = extract_array_content(api_str[fields_start:], '')
                if success_content:
                    success = parse_fields(success_content)
        
        apis.append({
            'method': method,
            'url': url,
            'title': title,
            'params': params,
            'body': body,
            'success': success
        })

# ============== 提取枚举类型 ==============
enum_pattern = r'\{type:"([^"]*枚举[^"]*)",url:"/([^"]+)"'
enum_matches = list(re.finditer(enum_pattern, content))

enums = []
seen_enum_urls = set()

for match in enum_matches:
    type_name = match.group(1)
    url = match.group(2)
    
    if url in seen_enum_urls:
        continue
    seen_enum_urls.add(url)
    
    start_pos = match.start()
    end_pos = find_api_end(content, start_pos)
    
    enum_str = content[start_pos:end_pos]
    title = extract_field(enum_str, 'title')
    
    success_start = enum_str.find('success:{')
    fields = []
    if success_start != -1:
        fields_start = enum_str.find('fields:{', success_start)
        if fields_start != -1:
            success_content = extract_array_content(enum_str[fields_start:], '')
            if success_content:
                fields = parse_fields(success_content)
    
    enums.append({
        'name': type_name,
        'url': url,
        'title': title,
        'fields': fields
    })

# ============== 提取对象类型 ==============
object_pattern = r'\{type:"([^"]+)",url:"/([^"]+)"'
object_matches = list(re.finditer(object_pattern, content))

objects = []
seen_obj_urls = set()

for match in object_matches:
    type_name = match.group(1)
    url = match.group(2)
    
    if type_name in ['get', 'post', 'put', 'delete']:
        continue
    if '枚举' in type_name:
        continue
    if url.startswith('api/v1/'):
        continue
    if url in seen_obj_urls:
        continue
    
    seen_obj_urls.add(url)
    
    start_pos = match.start()
    end_pos = find_api_end(content, start_pos)
    
    obj_str = content[start_pos:end_pos]
    title = extract_field(obj_str, 'title')
    
    success_start = obj_str.find('success:{')
    fields = []
    if success_start != -1:
        fields_start = obj_str.find('fields:{', success_start)
        if fields_start != -1:
            success_content = extract_array_content(obj_str[fields_start:], '')
            if success_content:
                fields = parse_fields(success_content)
    
    objects.append({
        'name': type_name,
        'url': url,
        'title': title,
        'fields': fields
    })

# ============== 生成文档 ==============
output = "# MEMS API 文档\n"
output += "\n***\n\n"
output += "## 概述\n\n"
output += "本文档描述了MEMS应用的RESTful API接口和数据类型定义，方便AI Agent调用。\n\n"
output += "### 基础信息\n\n"
output += "- **基础URL**: `http://ip:port/api/v1/`\n"
output += "- **认证方式**: Access-Token（在请求头中携带）\n"
output += "- **Content-Type**: `application/json`\n\n"
output += "### 认证说明\n\n"
output += "所有API请求（除登录接口外）需要在请求头中携带Access-Token：\n\n"
output += "```http\n"
output += "Access-Token: <your_token>\n"
output += "```\n\n"
output += "### 调用示例\n\n"
output += "使用Python requests库调用示例：\n\n"
output += "```python\n"
output += "import requests\n\n"
output += "base_url = 'http://ip:port/api/v1'\n"
output += "headers = {'Access-Token': 'your_token'}\n\n"
output += "# 获取所有用户\n"
output += "response = requests.get(f'{base_url}/auth/users', headers=headers)\n"
output += "print(response.json())\n"
output += "```\n\n"

# API概览
output += "## API 概览\n\n"
output += f"共 **{len(apis)}** 个API接口，分为以下模块：\n\n"

modules = {
    'auth': [], 'alarm': [], 'aoes': [], 'points': [], 'devices': [],
    'lcc': [], 'pscpu': [], 'graphs': [], 'plans': [], 'scripts': [],
    'webplugins': [], 'flows': [], 'ems': [], 'controls': [], 'tags': [],
    'result': [], 'common': []
}

for api in apis:
    url = api['url']
    if '/measures' in url or '/commands' in url or '/soes' in url:
        modules['result'].append(api)
        continue
    matched = False
    for module_name, module_apis in modules.items():
        if module_name == 'result':
            continue
        if f'/{module_name}/' in url or url.startswith(f'/api/v1/{module_name}'):
            module_apis.append(api)
            matched = True
            break
    if not matched:
        modules['common'].append(api)

for module_name, module_apis in modules.items():
    if module_apis:
        output += f"- **{module_name}**: {len(module_apis)} 个接口\n"

output += "\n## 数据类型概览\n\n"
output += f"- **枚举类型**: {len(enums)} 个\n"
output += f"- **对象类型**: {len(objects)} 个\n\n"

output += "***\n\n"

# API详细文档
for module_name, module_apis in modules.items():
    if not module_apis:
        continue
    
    output += f"## {module_name.capitalize()} 模块\n\n"
    output += f"共 {len(module_apis)} 个接口\n\n"
    
    for i, api in enumerate(module_apis, 1):
        output += f"### {i}. {api['title']}\n\n"
        output += f"- **方法**: `{api['method'].upper()}`\n"
        output += f"- **路径**: `{api['url']}`\n"
        
        if api['params']:
            output += "\n**查询参数**:\n\n"
            output += "| 参数名 | 类型 | 必填 | 说明 |\n"
            output += "| --- | --- | --- | --- |\n"
            for param in api['params']:
                required = "否" if param['optional'] else "是"
                desc = param['description'].replace('<p>', '').replace('</p>', '')
                output += f"| {param['name']} | {param['type']} | {required} | {desc} |\n"
        
        if api['body']:
            output += "\n**请求体**:\n\n"
            output += "| 字段名 | 类型 | 必填 | 说明 |\n"
            output += "| --- | --- | --- | --- |\n"
            for field in api['body']:
                required = "否" if field['optional'] else "是"
                desc = field['description'].replace('<p>', '').replace('</p>', '')
                output += f"| {field['name']} | {field['type']} | {required} | {desc} |\n"
        
        if api['success']:
            output += "\n**成功响应**:\n\n"
            output += "| 字段名 | 类型 | 说明 |\n"
            output += "| --- | --- | --- |\n"
            for field in api['success']:
                desc = field['description'].replace('<p>', '').replace('</p>', '')
                output += f"| {field['name']} | {field['type']} | {desc} |\n"
        
        output += "\n"

# 枚举类型定义
output += "## 枚举类型定义\n\n"
output += f"共 {len(enums)} 个枚举类型\n\n"

for i, enum in enumerate(enums, 1):
    output += f"### {i}. {enum['name']}\n\n"
    if enum['title']:
        output += f"- **描述**: {enum['title']}\n"
    output += f"- **引用**: `/{enum['url']}`\n\n"
    
    if enum['fields']:
        output += "**字段**:\n\n"
        output += "| 字段名 | 类型 | 必填 | 说明 |\n"
        output += "| --- | --- | --- | --- |\n"
        for field in enum['fields']:
            required = "否" if field['optional'] else "是"
            desc = field['description'].replace('<p>', '').replace('</p>', '')
            desc = desc.replace('&quot;', '"')
            output += f"| {field['name']} | {field['type']} | {required} | {desc} |\n"
    
    output += "\n"

# 对象类型定义
output += "## 对象类型定义\n\n"
output += f"共 {len(objects)} 个对象类型\n\n"

for i, obj in enumerate(objects, 1):
    output += f"### {i}. {obj['name']}\n\n"
    if obj['title']:
        output += f"- **描述**: {obj['title']}\n"
    output += f"- **引用**: `/{obj['url']}`\n\n"
    
    if obj['fields']:
        output += "**字段**:\n\n"
        output += "| 字段名 | 类型 | 必填 | 说明 |\n"
        output += "| --- | --- | --- | --- |\n"
        for field in obj['fields']:
            required = "否" if field['optional'] else "是"
            desc = field['description'].replace('<p>', '').replace('</p>', '')
            desc = desc.replace('&quot;', '"')
            output += f"| {field['name']} | {field['type']} | {required} | {desc} |\n"
    
    output += "\n"

with open('mems_api_docs.md', 'w', encoding='utf-8') as f:
    f.write(output)

# 统计信息
apis_without_params = [api for api in apis if not api['params'] and not api['body']]
apis_without_success = [api for api in apis if not api['success']]
print(f"API文档已保存到 mems_api_docs.md")
print(f"- API接口: {len(apis)} 个")
print(f"- 没有请求参数的API: {len(apis_without_params)} 个")
print(f"- 没有成功响应的API: {len(apis_without_success)} 个")
print(f"- 枚举类型: {len(enums)} 个")
print(f"- 对象类型: {len(objects)} 个")
