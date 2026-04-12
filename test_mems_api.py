import requests
import hmac
import hashlib
import base64

base_url = 'http://localhost:80/api/v1'
username = 'admin'
password = 'easy2021'
secret_key = b'zju-plcc'

print('=== MEMS API 测试 ===')
print(f'服务地址: {base_url}')
print()

# 1. 测试ping接口
print('1. /ping - 服务状态检查')
try:
    response = requests.get(f'{base_url}/ping', timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f'   状态码: {response.status_code}')
        print(f'   设备ID: {data.get("id", "N/A")}')
        print(f'   设备IP: {data.get("ip", "N/A")}')
    else:
        print(f'   状态码: {response.status_code}')
        print(f'   错误: {response.text}')
except Exception as e:
    print(f'   请求失败: {e}')

print()

# 2. 登录
print('2. /auth/login - 用户登录')
try:
    encrypted_password = hmac.new(secret_key, password.encode('utf-8'), hashlib.sha256).digest()
    base64_password = base64.b64encode(encrypted_password).decode('utf-8')
    
    login_data = [username, base64_password]
    response = requests.post(f'{base_url}/auth/login', json=login_data, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        print(f'   状态码: {response.status_code}')
        print(f'   用户ID: {data[1]}')
        print(f'   用户名: {data[2]}')
        
        if len(data) >= 2 and data[1] == 1:
            token = data[0]
            print(f'   Token: {token[:30]}...')
            
            headers = {'Access-Token': token}
            
            # 3. 获取用户列表
            print()
            print('3. /auth/users - 获取用户列表')
            try:
                response = requests.get(f'{base_url}/auth/users', headers=headers, timeout=5)
                if response.status_code == 200:
                    users = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   用户数量: {len(users)}')
                    for user in users:
                        print(f'   - {user.get("username", "N/A")} (ID: {user.get("id", "N/A")})')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
            
            # 4. 获取系统配置
            print()
            print('4. /config - 获取系统配置')
            try:
                response = requests.get(f'{base_url}/config', headers=headers, timeout=5)
                if response.status_code == 200:
                    config = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   配置项数量: {len(config)}')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
            
            # 5. 获取测点列表
            print()
            print('5. /points/models - 获取测点列表')
            try:
                response = requests.get(f'{base_url}/points/models', headers=headers, timeout=5)
                if response.status_code == 200:
                    points = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   测点数量: {len(points)}')
                    if points:
                        first_point = points[0]
                        print(f'   第一个测点: {first_point.get("name", "N/A")} (ID: {first_point.get("id", "N/A")})')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
            
            # 6. 获取告警列表
            print()
            print('6. /alarms - 获取告警列表')
            try:
                response = requests.get(f'{base_url}/alarms', headers=headers, timeout=5)
                if response.status_code == 200:
                    alarms = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   告警数量: {len(alarms)}')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
            
            # 7. 获取设备拓扑
            print()
            print('7. /devices/cns - 获取设备拓扑')
            try:
                response = requests.get(f'{base_url}/devices/cns', headers=headers, timeout=5)
                if response.status_code == 200:
                    cns = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   拓扑节点数量: {len(cns)}')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
            
            # 8. 获取角色列表
            print()
            print('8. /auth/roles - 获取角色列表')
            try:
                response = requests.get(f'{base_url}/auth/roles', headers=headers, timeout=5)
                if response.status_code == 200:
                    roles = response.json()
                    print(f'   状态码: {response.status_code}')
                    print(f'   角色数量: {len(roles)}')
                    for role in roles:
                        print(f'   - {role.get("name", "N/A")} (ID: {role.get("id", "N/A")})')
                else:
                    print(f'   状态码: {response.status_code}')
                    print(f'   错误: {response.text}')
            except Exception as e:
                print(f'   请求失败: {e}')
        
        else:
            print(f'   登录失败: {data}')
    else:
        print(f'   状态码: {response.status_code}')
        print(f'   错误: {response.text}')
except Exception as e:
    print(f'   请求失败: {e}')

print()
print('=== 测试完成 ===')