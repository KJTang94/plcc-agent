import requests
import hmac
import hashlib
import base64

base_url = 'http://localhost:80/api/v1'
username = 'admin'
password = 'easy2021'
secret_key = b'zju-plcc'

print('=== MEMS API 扩展测试 ===')
print(f'服务地址: {base_url}')
print()

# 登录获取token
print('登录获取Token...')
encrypted_password = hmac.new(secret_key, password.encode('utf-8'), hashlib.sha256).digest()
base64_password = base64.b64encode(encrypted_password).decode('utf-8')
login_data = [username, base64_password]
response = requests.post(f'{base_url}/auth/login', json=login_data, timeout=5)
token = response.json()[0]
headers = {'Access-Token': token}
print(f'   Token获取成功: {token[:20]}...')
print()

# 测试列表
apis_to_test = [
    ('GET', '/config', '系统配置'),
    ('GET', '/points/models', '测点列表'),
    ('GET', '/devices/cns', '设备拓扑'),
    ('GET', '/auth/roles', '角色列表'),
    ('GET', '/aoes/models', 'AOE模型列表'),
    ('GET', '/lcc/models', 'LCC模型列表'),
    ('GET', '/graphs/models', '图形模型列表'),
    ('GET', '/plans', '计划任务列表'),
    ('GET', '/scripts', '脚本列表'),
    ('GET', '/flows', '流程列表'),
]

for method, endpoint, description in apis_to_test:
    print(f'{method} /{endpoint.strip("/")} - {description}')
    try:
        if method == 'GET':
            response = requests.get(f'{base_url}{endpoint}', headers=headers, timeout=5)
        elif method == 'POST':
            response = requests.post(f'{base_url}{endpoint}', headers=headers, timeout=5)
        
        print(f'   状态码: {response.status_code}')
        
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, list):
                    print(f'   返回数量: {len(data)}')
                    if len(data) > 0 and isinstance(data[0], dict):
                        keys = list(data[0].keys())[:5]
                        print(f'   数据结构: {", ".join(keys)}...')
                elif isinstance(data, dict):
                    keys = list(data.keys())[:5]
                    print(f'   返回字段: {", ".join(keys)}...')
                else:
                    print(f'   返回类型: {type(data).__name__}')
            except:
                print(f'   响应内容: {response.text[:100]}...')
        else:
            print(f'   错误: {response.text[:100]}')
    except Exception as e:
        print(f'   请求失败: {e}')
    print()

print('=== 测试完成 ===')