import requests
import hmac
import hashlib
import base64

base_url = 'http://localhost:80/api/v1'
username = 'admin'
password = 'easy2021'

print('=== MEMS 登录测试 ===')
print(f'服务地址: {base_url}')
print(f'用户名: {username}')
print(f'密码: {password}')
print()


print('尝试使用密码进行HmacSHA256加密...')
try:
    secret_key = b'zju-plcc'
    encrypted_password = hmac.new(secret_key, password.encode('utf-8'), hashlib.sha256).digest()
    base64_password = base64.b64encode(encrypted_password).decode('utf-8')
    print(f'   加密后的密码: {base64_password}')
    
    login_data = [username, base64_password]
    response = requests.post(f'{base_url}/auth/login', json=login_data, timeout=5)
    print(f'   状态码: {response.status_code}')
    print(f'   响应: {response.text}')
except Exception as e:
    print(f'   请求失败: {e}')

print()
