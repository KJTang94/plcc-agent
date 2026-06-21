import json
import os
import requests
import hmac
import hashlib
import base64
from config import (
    get_mems_api_config,
    get_prop_def_file_path,
    get_cns_file_path,
    get_rsr_def_file_path,
    get_resources_file_path,
    get_meas_def_file_path,
    get_points_models_file_path,
    get_flows_models_file_path,
    get_aoes_models_file_path,
)


class MemsAPI:
    def __init__(self, base_url: str = None, username: str = None, password: str = None, secret_key: str = None):
        mems_config = get_mems_api_config()
        self.base_url = base_url or mems_config.get("base_url", "http://localhost:80/api/v1")
        self.token = None
        self.username = username or mems_config.get("username", "admin")
        self.password = password or mems_config.get("password", "")
        self.secret_key = (secret_key or mems_config.get("secret_key", "")).encode("utf-8")
    
    def _send(self, method: str, url: str, params: dict = None, data: dict = None, files: dict = None):
        headers = {'Access-Token': self.token}
        if method == 'GET':
            return requests.get(url, headers=headers, params=params, timeout=10)
        elif method == 'POST':
            if files:
                # 文件上传方式（multipart/form-data）
                return requests.post(url, headers=headers, files=files, timeout=30)
            # JSON方式
            return requests.post(url, headers=headers, json=data, timeout=10)
        elif method == 'PUT':
            return requests.put(url, headers=headers, json=data, timeout=10)
        elif method == 'DELETE':
            return requests.delete(url, headers=headers, params=params, timeout=10)
        return None

    def _request(self, method: str, path: str, params: dict = None, data: dict = None, files: dict = None) -> str:
        # token 为空时尝试自动登录，凭据已在配置中无需向用户索要
        if not self.token:
            login_result = json.loads(self.login())
            if not login_result.get("success"):
                return json.dumps({"success": False, "message": "尚未登录且自动登录失败：" + login_result.get("message", "")}, ensure_ascii=False)

        url = f'{self.base_url}{path}'

        try:
            response = self._send(method, url, params=params, data=data, files=files)
            if response is None:
                return json.dumps({"success": False, "message": "不支持的HTTP方法"}, ensure_ascii=False)

            # token 失效（401/403）时自动重登并重试一次
            if response.status_code in (401, 403):
                login_result = json.loads(self.login())
                if login_result.get("success"):
                    response = self._send(method, url, params=params, data=data, files=files)
                    if response is None:
                        return json.dumps({"success": False, "message": "不支持的HTTP方法"}, ensure_ascii=False)

            # 处理成功响应（200状态码）
            if response.status_code == 200:
                # 检查响应体是否为空
                if not response.text.strip():
                    return json.dumps({"success": True, "data": None}, ensure_ascii=False)
                
                # 尝试解析JSON，如果失败则返回原始文本
                try:
                    return json.dumps({"success": True, "data": response.json()}, ensure_ascii=False)
                except json.JSONDecodeError:
                    # API返回非JSON数据，不是错误，正常返回
                    return json.dumps({"success": True, "data": response.text}, ensure_ascii=False)
            
            # 处理失败响应
            print(f"[ERROR] HTTP状态码: {response.status_code}")
            print(f"[ERROR] 响应头: {dict(response.headers)}")
            print(f"[ERROR] 响应内容: {response.text[:1000]}")
            return json.dumps({"success": False, "message": f"请求失败 (状态码: {response.status_code}): {response.text}"}, ensure_ascii=False)
        except requests.exceptions.RequestException as e:
            # 只捕获网络相关异常
            return json.dumps({"success": False, "message": f"请求异常: {str(e)}"}, ensure_ascii=False)
        except Exception as e:
            # 其他异常
            return json.dumps({"success": False, "message": f"未知异常: {str(e)}"}, ensure_ascii=False)
    
    def login(self) -> str:
        if not self.username or not self.password or not self.secret_key:
            return json.dumps({
                "success": False,
                "message": "MEMS登录配置缺失，请检查 config.json 中 mems_api.username、mems_api.password、mems_api.secret_key 是否已正确配置"
            }, ensure_ascii=False)
        try:
            encrypted_password = hmac.new(self.secret_key, self.password.encode('utf-8'), hashlib.sha256).digest()
            base64_password = base64.b64encode(encrypted_password).decode('utf-8')
            login_data = [self.username, base64_password]
            response = requests.post(f'{self.base_url}/auth/login', json=login_data, timeout=10)
            if response.status_code == 200:
                data = response.json()
                self.token = data[0]
                return json.dumps({
                    "success": True,
                    "user_id": data[1],
                    "username": data[2],
                    "message": "登录成功"
                }, ensure_ascii=False)
            return json.dumps({
                "success": False,
                "message": "登录失败: " + response.text
            }, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "message": "登录异常: " + str(e)
            }, ensure_ascii=False)
    
    def get_alarm_config(self) -> str:
        return self._request('GET', f'/alarm/config')

    def add_alarm_config(self, data: dict = None) -> str:
        return self._request('POST', f'/alarm/config', data=data)

    def add_alarm_confirm_by_user(self, user_id: int, data: dict = None) -> str:
        return self._request('POST', f'/alarm/confirm/{user_id}', data=data)

    def get_alarm_confirm_status(self) -> str:
        return self._request('GET', f'/alarm/confirm_status')

    def get_alarm_count(self) -> str:
        return self._request('GET', f'/alarm/count')

    def add_alarm_define(self, data: dict = None) -> str:
        return self._request('POST', f'/alarm/define', data=data)

    def get_alarm_define_by(self, id: int) -> str:
        return self._request('GET', f'/alarm/define/{id}')

    def get_alarm_defines(self) -> str:
        return self._request('GET', f'/alarm/defines')

    def add_alarm_defines(self, data: dict = None) -> str:
        return self._request('POST', f'/alarm/defines', data=data)

    def delete_alarm_defines_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/alarm/defines/{ids}')

    def add_alarm_defines_file(self, data: dict = None) -> str:
        return self._request('POST', f'/alarm/defines_file', data=data)

    def get_alarm_unconfirmed_number(self) -> str:
        return self._request('GET', f'/alarm/unconfirmed_number')

    def get_alarms(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/alarms', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_alarms_unconfirmed(self) -> str:
        return self._request('GET', f'/alarms/unconfirmed')

    def get_aoe_results(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/aoe_results', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_aoes_models(self) -> str:
        return self._request('GET', f'/aoes/models')

    def add_aoes_models(self, data: dict = None) -> str:
        return self._request('POST', f'/aoes/models', data=data)

    def get_aoes_models_by_version_by_v(self, v: int) -> str:
        return self._request('GET', f'/aoes/models/by_version/{v}')

    def get_aoes_models_for_apply(self, version: int = None) -> str:
        return self._request('GET', f'/aoes/models/for_apply', params={"version": version})

    def delete_aoes_models_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/aoes/models/{ids}')

    def get_aoes_models_by(self, id: int, version: int = None) -> str:
        return self._request('GET', f'/aoes/models/{id}', params={"version": version})

    def add_aoes_models_file(self, data: dict = None) -> str:
        """
        新增AOE模型。
        如果未提供data参数，则从配置文件指定的Excel文件中读取数据，以PbFile格式上传。
        参数：data (dict, 可选) - AOE模型配置数据
        """
        # if data is None:
        # 未提供data时，从Excel文件读取数据，构建PbFile格式
        excel_path = get_aoes_models_file_path()
        try:
            import os

            # 检查文件是否存在
            if not os.path.exists(excel_path):
                raise FileNotFoundError(f"AOE模型Excel文件不存在：{excel_path}")

            # 读取文件内容为字节数组
            with open(excel_path, 'rb') as f:
                file_content = list(f.read())  # 转换为整数数组

            # 构建PbFile格式数据
            data = {
                "fileContent": file_content,
                "fileName": os.path.basename(excel_path),
                "is_zip": False,
                "op": None
            }

            print(f"[DEBUG] 准备上传AOE模型文件: {data['fileName']}, 大小: {len(file_content)} bytes")
        except Exception as e:
            return json.dumps({"success": False, "message": str(e)}, ensure_ascii=False)

        return self._request('POST', '/aoes/models_file', data=data)

    def add_aoes_models_file2(self, data: dict = None) -> str:
        return self._request('POST', f'/aoes/models_file2', data=data)

    def add_multi_import_files(self, data: dict = None) -> str:
        """
        多文件导入所有模型（PbFiles格式）。
        如果未提供data参数，则从配置文件指定的Excel文件中读取数据。
        需要读取以下文件：
        - 属性定义: prop_def_
        - 模型定义: rsr_def_
        - 量测定义: meas_def_
        - 资源: resources_
        - 拓扑: cns_
        
        PbFiles格式：{
            "files": [
                {
                    "fileName": "prop_def_xxx.xlsx",
                    "fileContent": [80, 75, 3, 4, ...],
                    "is_zip": false,
                    "op": null
                },
                ...
            ]
        }
        
        参数：data (dict, 可选) - 请求体数据
        """
        # if data is None:
        try:
            import os
            
            # 定义文件映射（文件名前缀 -> 配置路径函数）
            file_mappings = {
                'prop_def_': get_prop_def_file_path(),
                'rsr_def_': get_rsr_def_file_path(),
                'meas_def_': get_meas_def_file_path(),
                'resources_': get_resources_file_path(),
                'cns_': get_cns_file_path(),
            }
            
            # 构建PbFiles格式的文件列表
            files_list = []
            for prefix, excel_path in file_mappings.items():
                if excel_path and os.path.exists(excel_path):
                    with open(excel_path, 'rb') as f:
                        file_content = list(f.read())  # 转换为整数数组
                    
                    # 使用前缀+原文件名
                    original_name = os.path.basename(excel_path)
                    file_name = f'{prefix}{original_name}'
                    
                    # 构建单个PbFile对象
                    # op字段是必需的，可选值: UPDATE, DELETE, RENAME
                    pb_file = {
                        "fileName": file_name,
                        "fileContent": file_content,
                        "is_zip": False,
                        "op": None
                    }
                    files_list.append(pb_file)
                    
                else:
                    print(f"[WARNING] 文件不存在或路径为空: {excel_path}")
            
            # 构建PbFiles格式数据
            data = {
                "files": files_list
            }
        except Exception as e:
            return json.dumps({"success": False, "message": str(e)}, ensure_ascii=False)
        
        # 使用 _request 方法调用API
        return self._request('POST', '/multi_import_files', data=data)

    def get_aoes_version(self) -> str:
        return self._request('GET', f'/aoes/version')

    def add_aoes_version(self, data: dict = None) -> str:
        return self._request('POST', f'/aoes/version', data=data)

    def delete_aoes_version_by_v(self, v: int) -> str:
        return self._request('DELETE', f'/aoes/version/{v}')

    def get_auth_auths(self) -> str:
        return self._request('GET', f'/auth/auths')

    def add_auth_auths(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/auths', data=data)

    def get_auth_auths_by_role(self, id: int) -> str:
        return self._request('GET', f'/auth/auths/by_role/{id}')

    def delete_auth_auths_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/auths/{ids}')

    def add_auth_login(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/login', data=data)

    def get_auth_menus(self) -> str:
        return self._request('GET', f'/auth/menus')

    def add_auth_menus(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/menus', data=data)

    def get_auth_menus_by_role(self, id: int) -> str:
        return self._request('GET', f'/auth/menus/by_role/{id}')

    def get_auth_menus_by_user(self, id: int) -> str:
        return self._request('GET', f'/auth/menus/by_user/{id}')

    def delete_auth_menus_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/menus/{ids}')

    def add_auth_register(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/register', data=data)

    def get_auth_roles(self) -> str:
        return self._request('GET', f'/auth/roles')

    def add_auth_roles(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/roles', data=data)

    def update_auth_roles(self, data: dict = None) -> str:
        return self._request('PUT', f'/auth/roles', data=data)

    def get_auth_roles_by_s(self, ids: str) -> str:
        return self._request('GET', f'/auth/roles/{ids}')

    def delete_auth_roles_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/roles/{ids}')

    def get_auth_user_groups(self) -> str:
        return self._request('GET', f'/auth/user_groups')

    def add_auth_user_groups(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/user_groups', data=data)

    def update_auth_user_groups(self, data: dict = None) -> str:
        return self._request('PUT', f'/auth/user_groups', data=data)

    def delete_auth_user_groups_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/user_groups/{ids}')

    def get_auth_user_groups_by(self, id: int) -> str:
        return self._request('GET', f'/auth/user_groups/{id}')

    def get_auth_users(self) -> str:
        return self._request('GET', f'/auth/users')

    def add_auth_users(self, data: dict = None) -> str:
        return self._request('POST', f'/auth/users', data=data)

    def update_auth_users(self, data: dict = None) -> str:
        return self._request('PUT', f'/auth/users', data=data)

    def get_auth_users_by_user_group(self, id: int) -> str:
        return self._request('GET', f'/auth/users/by_user_group/{id}')

    def update_auth_users_password_by(self, id: int, data: dict = None) -> str:
        return self._request('PUT', f'/auth/users/password/{id}', data=data)

    def update_auth_users_reset_password_by(self, id: int) -> str:
        return self._request('PUT', f'/auth/users/reset_password/{id}')

    def update_auth_users_roles_by(self, id: int, data: dict = None) -> str:
        return self._request('PUT', f'/auth/users/roles/{id}', data=data)

    def delete_auth_users_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/users/{ids}')

    def get_auth_users_by(self, id: int) -> str:
        return self._request('GET', f'/auth/users/{id}')

    def get_commands(self, sender_id: int = None, point_id: int = None, start: int = None, end: int = None, date: str = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/commands', params={"sender_id": sender_id, "point_id": point_id, "start": start, "end": end, "date": date, "reverse_order": reverse_order})

    def add_common_map(self, data: dict = None) -> str:
        return self._request('POST', f'/common_map', data=data)

    def get_config(self) -> str:
        return self._request('GET', f'/config')

    def add_config(self, data: dict = None) -> str:
        return self._request('POST', f'/config', data=data)

    def add_controls_aoes(self, data: dict = None) -> str:
        return self._request('POST', f'/controls/aoes', data=data)

    def add_controls_points(self, data: dict = None) -> str:
        return self._request('POST', f'/controls/points', data=data)

    def add_controls_points_by_alias(self, data: dict = None) -> str:
        return self._request('POST', f'/controls/points_by_alias', data=data)

    def add_controls_points_by_expr(self, data: dict = None) -> str:
        return self._request('POST', f'/controls/points_by_expr', data=data)

    def add_controls_points_with_source_by_source(self, source: int, data: dict = None) -> str:
        return self._request('POST', f'/controls/points_with_source/{source}', data=data)

    def get_devices_cns(self, version: int = None) -> str:
        return self._request('GET', f'/devices/cns', params={"version": version})

    def add_devices_cns(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/cns', data=data)

    def get_devices_defines(self) -> str:
        return self._request('GET', f'/devices/defines')

    def add_devices_defines(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/defines', data=data)

    def update_devices_defines(self, data: dict = None) -> str:
        return self._request('PUT', f'/devices/defines', data=data)

    def delete_devices_defines_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/defines/{ids}')

    def get_devices_defines_by(self, id: int) -> str:
        return self._request('GET', f'/devices/defines/{id}')

    def get_devices_devs(self, version: int = None) -> str:
        return self._request('GET', f'/devices/devs', params={"version": version})

    def add_devices_devs(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/devs', data=data)

    def update_devices_devs(self, data: dict = None) -> str:
        return self._request('PUT', f'/devices/devs', data=data)

    def delete_devices_devs_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/devs/{ids}')

    def get_devices_devs_by(self, id: int, version: int = None) -> str:
        return self._request('GET', f'/devices/devs/{id}', params={"version": version})

    def get_devices_islands(self, version: int = None) -> str:
        return self._request('GET', f'/devices/islands', params={"version": version})

    def add_devices_islands(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/islands', data=data)

    def get_devices_measure_defs(self, version: int = None) -> str:
        return self._request('GET', f'/devices/measure_defs', params={"version": version})

    def add_devices_measure_defs(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/measure_defs', data=data)

    def update_devices_measure_defs(self, data: dict = None) -> str:
        return self._request('PUT', f'/devices/measure_defs', data=data)

    def delete_devices_measure_defs(self, data: dict = None) -> str:
        return self._request('DELETE', f'/devices/measure_defs', data=data)

    def get_devices_point_tree(self, version: int = None) -> str:
        return self._request('GET', f'/devices/point_tree', params={"version": version})

    def get_devices_prop_defines(self) -> str:
        return self._request('GET', f'/devices/prop_defines')

    def add_devices_prop_defines(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/prop_defines', data=data)

    def update_devices_prop_defines(self, data: dict = None) -> str:
        return self._request('PUT', f'/devices/prop_defines', data=data)

    def delete_devices_prop_defines_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/prop_defines/{ids}')

    def get_devices_prop_groups(self, version: int = None) -> str:
        return self._request('GET', f'/devices/prop_groups', params={"version": version})

    def add_devices_prop_groups(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/prop_groups', data=data)

    def update_devices_prop_groups(self, data: dict = None) -> str:
        return self._request('PUT', f'/devices/prop_groups', data=data)

    def get_devices_prop_groups_by_s(self, ids: str, version: int = None) -> str:
        return self._request('GET', f'/devices/prop_groups/{ids}', params={"version": version})

    def delete_devices_prop_groups_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/prop_groups/{ids}')

    def delete_devices_resources_clear(self) -> str:
        return self._request('DELETE', f'/devices/resources_clear')

    def get_devices_version(self) -> str:
        return self._request('GET', f'/devices/version')

    def add_devices_version(self, data: dict = None) -> str:
        return self._request('POST', f'/devices/version', data=data)

    def delete_devices_version_by(self, id: int) -> str:
        return self._request('DELETE', f'/devices/version/{id}')

    def add_ems_request_by_ems(self, ems_id: str, data: dict = None) -> str:
        return self._request('POST', f'/ems/request/{ems_id}', data=data)

    def get_ems_by(self, id: str) -> str:
        return self._request('GET', f'/ems/{id}')

    def get_ems_list(self) -> str:
        return self._request('GET', f'/ems_list')

    def add_file_tree(self, data: dict = None) -> str:
        return self._request('POST', f'/file_tree', data=data)

    def add_file_tree_by(self, id: str, data: dict = None) -> str:
        return self._request('POST', f'/file_tree/{id}', data=data)

    def add_file_tree_version(self, data: dict = None) -> str:
        return self._request('POST', f'/file_tree_version', data=data)

    def get_flows_brief_results(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/flows/brief_results', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def add_flows_controls(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/controls', data=data)

    def add_flows_debug(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/debug', data=data)

    def get_flows_models(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/flows/models', params={"id": id, "ids": ids})

    def add_flows_models(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/models', data=data)

    def update_flows_models(self, data: dict = None) -> str:
        return self._request('PUT', f'/flows/models', data=data)

    def delete_flows_models_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/flows/models/{ids}')

    def add_flows_models_file2(self, data: dict = None) -> str:
        """
        新增报表模型（多文件形式）。
        如果未提供data参数，则从配置文件指定的Excel文件中读取数据，以UploadForm格式上传。
        参数：data (dict, 可选) - 报表模型配置数据
        """
        # if data is None:
        # 从Excel文件读取数据，构建UploadForm格式（multipart/form-data）
        excel_path = get_flows_models_file_path()
        try:
            import os
            
            # 检查文件是否存在
            if not os.path.exists(excel_path):
                raise FileNotFoundError(f"报表配置Excel文件不存在：{excel_path}")
            
            print(f"[DEBUG] 报表文件路径: {excel_path}")
            print(f"[DEBUG] 绝对路径: {os.path.abspath(excel_path)}")
            
            # 读取文件内容
            with open(excel_path, 'rb') as f:
                file_content = f.read()
            
            # 构建UploadForm格式数据（multipart/form-data）
            # 根据API文档，UploadForm要求files是数组类型
            # 使用requests库的列表格式确保数组结构
            files_data = [
                ('file', (os.path.basename(excel_path), file_content, 'application/octet-stream'))
            ]
            
            print(f"[DEBUG] 准备上传报表文件: {os.path.basename(excel_path)}, 大小: {len(file_content)} bytes")
            
            # 使用统一的_request方法上传文件
            return self._request('POST', '/flows/models_file2', files=files_data)
        except Exception as e:
            return json.dumps({"success": False, "message": str(e)}, ensure_ascii=False)
        
        return self._request('POST', '/flows/models_file2', data=data)

    def get_flows_models_json(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/flows/models_json', params={"id": id, "ids": ids})

    def add_flows_prog_file2(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/prog_file2', data=data)

    def add_flows_reload_dff_by_flow(self, flow_id: str) -> str:
        return self._request('POST', f'/flows/reload_dff/{flow_id}')

    def get_flows_result_keys(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/flows/result_keys', params={"id": id, "ids": ids})

    def get_flows_results(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/flows/results', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def delete_flows_results(self, data: dict = None) -> str:
        return self._request('DELETE', f'/flows/results', data=data)

    def add_flows_results_rename(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/results/rename', data=data)

    def update_flows_results_by_by_key(self, id: str, key: str, data: dict = None) -> str:
        return self._request('PUT', f'/flows/results/{id}/{key}', data=data)

    def get_flows_results_by_by_key_by_view(self, id: str, key: str, view: str, data: dict = None) -> str:
        return self._request('GET', f'/flows/results/{id}/{key}/{view}', data=data)

    def get_flows_results_json(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/flows/results_json', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_flows_results_json_rows(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/flows/results_json_rows', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_flows_running(self) -> str:
        return self._request('GET', f'/flows/running')

    def get_flows_simple_models(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/flows/simple_models', params={"id": id, "ids": ids})

    def get_flows_unrun(self) -> str:
        return self._request('GET', f'/flows/unrun')

    def get_flows_view(self, id: str = None, flow_id: int = None) -> str:
        return self._request('GET', f'/flows/view', params={"id": id, "flow_id": flow_id})

    def add_flows_view(self, data: dict = None) -> str:
        return self._request('POST', f'/flows/view', data=data)

    def update_flows_view(self, data: dict = None) -> str:
        return self._request('PUT', f'/flows/view', data=data)

    def delete_flows_view_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/flows/view/{ids}')

    def add_graphs_apply_additional(self, data: dict = None) -> str:
        return self._request('POST', f'/graphs/apply/additional', data=data)

    def get_graphs_apply_models_by_path(self, path: str) -> str:
        return self._request('GET', f'/graphs/apply/models/{path}')

    def get_graphs_apply_paths(self) -> str:
        return self._request('GET', f'/graphs/apply/paths')

    def add_graphs_apply_version(self, data: dict = None) -> str:
        return self._request('POST', f'/graphs/apply/version', data=data)

    def add_graphs_models(self, data: dict = None) -> str:
        return self._request('POST', f'/graphs/models', data=data)

    def get_graphs_models_by_path(self, path: str, version: int = None) -> str:
        return self._request('GET', f'/graphs/models/{path}', params={"version": version})

    def delete_graphs_models_by_path(self, path: str) -> str:
        return self._request('DELETE', f'/graphs/models/{path}')

    def get_graphs_paths(self, version: int = None) -> str:
        return self._request('GET', f'/graphs/paths', params={"version": version})

    def get_graphs_version(self) -> str:
        return self._request('GET', f'/graphs/version')

    def add_graphs_version(self, data: dict = None) -> str:
        return self._request('POST', f'/graphs/version', data=data)

    def delete_graphs_version_by_v(self, v: int) -> str:
        return self._request('DELETE', f'/graphs/version/{v}')

    def get_lcc_alarm_config_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/config/{lcc_id}')

    def add_lcc_alarm_config_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/alarm/config/{lcc_id}', data=data)

    def add_lcc_alarm_confirm_by_lcc_by_user(self, lcc_id: str, user_id: int, data: dict = None) -> str:
        return self._request('POST', f'/lcc/alarm/confirm/{lcc_id}/{user_id}', data=data)

    def get_lcc_alarm_confirm_status_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/confirm_status/{lcc_id}')

    def get_lcc_alarm_count_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/count/{lcc_id}')

    def add_lcc_alarm_define_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/alarm/define/{lcc_id}', data=data)

    def get_lcc_alarm_define_by_lcc_by(self, lcc_id: str, id: int) -> str:
        return self._request('GET', f'/lcc/alarm/define/{lcc_id}/{id}')

    def get_lcc_alarm_defines_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/defines/{lcc_id}')

    def add_lcc_alarm_defines_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/alarm/defines/{lcc_id}', data=data)

    def delete_lcc_alarm_defines_by_lcc_by_s(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/alarm/defines/{lcc_id}/{ids}')

    def get_lcc_alarm_unconfirmed_number_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/unconfirmed_number/{lcc_id}')

    def get_lcc_alarms_unconfirmed_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarms/unconfirmed/{lcc_id}')

    def get_lcc_alarms_by_lcc(self, lcc_id: str, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/lcc/alarms/{lcc_id}', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_lcc_allmodels_bytes_by_lcc(self, lcc_id: str, lang: str) -> str:
        return self._request('GET', f'/lcc/allmodels_bytes/{lcc_id}', params={"lang": lang})

    def add_lcc_allmodels_bytes_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/allmodels_bytes/{lcc_id}', data=data)

    def get_lcc_aoe_results_by_lcc(self, lcc_id: str, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/lcc/aoe_results/{lcc_id}', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_lcc_aoes_models_by_lcc(self, lcc_id: str, id: str = None) -> str:
        return self._request('GET', f'/lcc/aoes/models/{lcc_id}', params={"id": id})

    def add_lcc_aoes_models_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/aoes/models/{lcc_id}', data=data)

    def delete_lcc_aoes_models_by_lcc_by_s(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/aoes/models/{lcc_id}/{ids}')

    def get_lcc_auth_users_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/auth/users/{lcc_id}')

    def get_lcc_commands_by_lcc(self, lcc_id: str, sender_id: int = None, point_id: int = None, start: int = None, end: int = None, date: str = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/lcc/commands/{lcc_id}', params={"sender_id": sender_id, "point_id": point_id, "start": start, "end": end, "date": date, "reverse_order": reverse_order})

    def add_lcc_common_map_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/common_map/{lcc_id}', data=data)

    def get_lcc_config_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/config/{lcc_id}')

    def add_lcc_config_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/config/{lcc_id}', data=data)

    def add_lcc_controls_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/controls/{lcc_id}', data=data)

    def get_lcc_logs_bytes_by_lcc(self, lcc_id: str, is_query_size: bool = None) -> str:
        return self._request('GET', f'/lcc/logs_bytes/{lcc_id}', params={"is_query_size": is_query_size})

    def get_lcc_measures_by_lcc(self, lcc_id: str, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/lcc/measures/{lcc_id}', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def add_lcc_points_import_str_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/points/import_str/{lcc_id}', data=data)

    def get_lcc_points_models_by_lcc(self, lcc_id: str, id: str = None, name: str = None, is_soe: bool = None) -> str:
        return self._request('GET', f'/lcc/points/models/{lcc_id}', params={"id": id, "name": name, "is_soe": is_soe})

    def add_lcc_points_models_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/points/models/{lcc_id}', data=data)

    def delete_lcc_points_models_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('DELETE', f'/lcc/points/models/{lcc_id}', data=data)

    def get_lcc_running_aoes_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/running_aoes/{lcc_id}')

    def get_lcc_soes_by_lcc(self, lcc_id: str, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/lcc/soes/{lcc_id}', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_lcc_tag_defines_by_lcc_by_group(self, lcc_id: str, group: int) -> str:
        return self._request('GET', f'/lcc/tag_defines/{lcc_id}/{group}')

    def add_lcc_tags_by_lcc_by_group(self, lcc_id: str, group: int, data: dict = None) -> str:
        return self._request('POST', f'/lcc/tags/{lcc_id}/{group}', data=data)

    def update_lcc_tags_by_lcc_by_group(self, lcc_id: str, group: int, data: dict = None) -> str:
        return self._request('PUT', f'/lcc/tags/{lcc_id}/{group}', data=data)

    def delete_lcc_tags_by_lcc_by_group(self, lcc_id: str, group: int, data: dict = None) -> str:
        return self._request('DELETE', f'/lcc/tags/{lcc_id}/{group}', data=data)

    def get_lcc_transports_models_by_lcc(self, lcc_id: str, id: str = None, transport_type: str = None) -> str:
        return self._request('GET', f'/lcc/transports/models/{lcc_id}', params={"id": id, "transport_type": transport_type})

    def add_lcc_transports_models_by_lcc(self, lcc_id: str, data: dict = None) -> str:
        return self._request('POST', f'/lcc/transports/models/{lcc_id}', data=data)

    def delete_lcc_transports_models_by_lcc_by_s(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/transports/models/{lcc_id}/{ids}')

    def get_lcc_unrun_aoes_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/unrun_aoes/{lcc_id}')

    def get_lcc_by(self, id: str) -> str:
        return self._request('GET', f'/lcc/{id}')

    def get_lcc_list(self) -> str:
        return self._request('GET', f'/lcc_list')

    def get_logs_bytes(self, is_query_size: bool = None) -> str:
        return self._request('GET', f'/logs_bytes', params={"is_query_size": is_query_size})

    def add_measureinits_by_day(self, day: int) -> str:
        return self._request('POST', f'/measureinits/{day}')

    def get_measures(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/measures', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def add_multi_import_bytes(self, data: dict = None) -> str:
        return self._request('POST', f'/multi_import_bytes', data=data)

    def add_north_dataframe_by_flow_by_node(self, flow: int, node: int, data: dict = None) -> str:
        return self._request('POST', f'/north/dataframe/{flow}/{node}', data=data)

    def add_north_restart(self) -> str:
        return self._request('POST', f'/north/restart')

    def get_ping(self) -> str:
        return self._request('GET', f'/ping')

    def get_plans_models(self) -> str:
        return self._request('GET', f'/plans/models')

    def add_plans_models(self, data: dict = None) -> str:
        return self._request('POST', f'/plans/models', data=data)

    def update_plans_models(self, data: dict = None) -> str:
        return self._request('PUT', f'/plans/models', data=data)

    def get_plans_models_by_ids(self, ids: str) -> str:
        return self._request('GET', f'/plans/models/by_ids/{ids}')

    def delete_plans_models_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/plans/models/{ids}')

    def get_plans_models_by(self, id: int) -> str:
        return self._request('GET', f'/plans/models/{id}')

    def get_plans_paths(self) -> str:
        return self._request('GET', f'/plans/paths')

    def add_plans_paths(self, data: dict = None) -> str:
        return self._request('POST', f'/plans/paths', data=data)

    def update_plans_paths(self, data: dict = None) -> str:
        return self._request('PUT', f'/plans/paths', data=data)

    def delete_plans_paths(self, data: dict = None) -> str:
        return self._request('DELETE', f'/plans/paths', data=data)

    def get_points_models(self) -> str:
        return self._request('GET', f'/points/models')

    def add_points_models(self, data: dict = None) -> str:
        return self._request('POST', f'/points/models', data=data)

    def delete_points_models(self, data: dict = None) -> str:
        return self._request('DELETE', f'/points/models', data=data)

    def get_points_models_for_apply(self, version: int = None) -> str:
        return self._request('GET', f'/points/models/for_apply', params={"version": version})

    def delete_points_models_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/points/models/{ids}')

    def add_points_models_file(self, data: dict = None) -> str:
        """
        新增测点模型。
        如果未提供data参数，则从配置文件指定的Excel文件中读取数据，以PbFile格式上传。
        参数：data (dict, 可选) - 测点模型配置数据
        """
        #if data is None:
        # 从Excel文件读取数据，构建PbFile格式
        excel_path = get_points_models_file_path()
        try:
            import os
            
            # 检查文件是否存在
            if not os.path.exists(excel_path):
                raise FileNotFoundError(f"测点模型Excel文件不存在：{excel_path}")
            
            # 读取文件内容为字节数组
            with open(excel_path, 'rb') as f:
                file_content = list(f.read())  # 转换为整数数组
            
            # 构建PbFile格式数据
            data = {
                "fileContent": file_content,
                "fileName": os.path.basename(excel_path),
                "is_zip": False,
                "op": None
            }
            
            print(f"[DEBUG] 准备上传测点模型文件: {data['fileName']}, 大小: {len(file_content)} bytes")
        except Exception as e:
            return json.dumps({"success": False, "message": str(e)}, ensure_ascii=False)
        
        return self._request('POST', '/points/models_file', data=data)

    def add_points_models_file2(self, data: dict = None) -> str:
        return self._request('POST', f'/points/models_file2', data=data)

    def get_points_remote(self) -> str:
        return self._request('GET', f'/points/remote')

    def add_points_remote(self, data: dict = None) -> str:
        return self._request('POST', f'/points/remote', data=data)

    def get_points_source(self) -> str:
        return self._request('GET', f'/points/source')

    def add_points_source(self, data: dict = None) -> str:
        return self._request('POST', f'/points/source', data=data)

    def get_points_version(self) -> str:
        return self._request('GET', f'/points/version')

    def add_points_version(self, data: dict = None) -> str:
        return self._request('POST', f'/points/version', data=data)

    def delete_points_version_by_v(self, v: int) -> str:
        return self._request('DELETE', f'/points/version/{v}')

    def add_pscpu_aoes(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/aoes', data=data)

    def get_pscpu_aoes_models(self) -> str:
        return self._request('GET', f'/pscpu/aoes/models')

    def get_pscpu_aoes_version(self) -> str:
        return self._request('GET', f'/pscpu/aoes/version')
    
    def add_pscpu_aoes_version(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/aoes/version', data=data)

    def get_pscpu_info(self) -> str:
        return self._request('GET', f'/pscpu/info')

    def add_pscpu_island(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/island', data=data)

    def get_pscpu_island_models(self) -> str:
        return self._request('GET', f'/pscpu/island/models')

    def get_pscpu_island_paths(self) -> str:
        return self._request('GET', f'/pscpu/island/paths')

    def get_pscpu_island_point_tree(self) -> str:
        return self._request('GET', f'/pscpu/island/point_tree')

    def get_pscpu_island_version(self) -> str:
        return self._request('GET', f'/pscpu/island/version')
    
    def add_pscpu_island_version(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/island/version', data=data)

    def add_pscpu_points(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/points', data=data)

    def get_pscpu_points_by_dev(self, dev_id: int) -> str:
        return self._request('GET', f'/pscpu/points/by_dev/{dev_id}')

    def get_pscpu_points_models(self, id: str = None, name: str = None, is_soe: bool = None) -> str:
        return self._request('GET', f'/pscpu/points/models', params={"id": id, "name": name, "is_soe": is_soe})

    def get_pscpu_points_values_by_src(self, src: int, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/pscpu/points/values/{src}', params={"id": id, "ids": ids})

    def get_pscpu_points_version(self) -> str:
        return self._request('GET', f'/pscpu/points/version')

    def add_pscpu_points_version(self, data: dict = None) -> str:
        return self._request('POST', f'/pscpu/points/version', data=data)
    
    def add_pscpu_reset(self) -> str:
        return self._request('POST', f'/pscpu/reset')

    def add_pscpu_start(self) -> str:
        return self._request('POST', f'/pscpu/start')

    def add_pscpu_stop(self) -> str:
        return self._request('POST', f'/pscpu/stop')

    def get_running_aoes(self) -> str:
        return self._request('GET', f'/running_aoes')

    def get_script_file_by_script(self, script_id: int) -> str:
        return self._request('GET', f'/script_file/{script_id}')

    def get_script_md5(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/script_md5', params={"id": id, "ids": ids})

    def get_script_results(self) -> str:
        return self._request('GET', f'/script_results')

    def add_script_results(self, data: dict = None) -> str:
        return self._request('POST', f'/script_results', data=data)

    def get_script_results_by(self, id: int) -> str:
        return self._request('GET', f'/script_results/{id}')

    def add_script_wasm(self, data: dict = None) -> str:
        return self._request('POST', f'/script_wasm', data=data)

    def get_scripts(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/scripts', params={"id": id, "ids": ids})

    def add_scripts(self, data: dict = None) -> str:
        return self._request('POST', f'/scripts', data=data)

    def delete_scripts_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/scripts/{ids}')

    def get_soes(self, id: str = None, start: int = None, end: int = None, date: str = None, source: int = None, last_only: bool = None, with_init: bool = None, reverse_order: bool = None) -> str:
        return self._request('GET', f'/soes', params={"id": id, "start": start, "end": end, "date": date, "source": source, "last_only": last_only, "with_init": with_init, "reverse_order": reverse_order})

    def get_tag_defines_by_group(self, id: int, group: int) -> str:
        return self._request('GET', f'/tag_defines/{group}')

    def update_tags_by_group(self, group: int, data: dict = None) -> str:
        return self._request('PUT', f'/tags/{group}', data=data)

    def delete_tags_by_group(self, group: int, data: dict = None) -> str:
        return self._request('DELETE', f'/tags/{group}', data=data)

    def add_tags_cbor_by_group(self, id: int, group: int, data: dict = None) -> str:
        return self._request('POST', f'/tags_cbor/{group}', data=data)

    def get_unrun_aoes(self) -> str:
        return self._request('GET', f'/unrun_aoes')

    def add_webplugin_file(self, data: dict = None) -> str:
        return self._request('POST', f'/webplugin_file', data=data)

    def get_webplugin_file_by_plugin(self, plugin_id: int) -> str:
        return self._request('GET', f'/webplugin_file/{plugin_id}')

    def get_webplugin_md5(self, id: int = None, ids: str = None) -> str:
        return self._request('GET', f'/webplugin_md5', params={"id": id, "ids": ids})

    def get_webplugins(self) -> str:
        return self._request('GET', f'/webplugins')

    def add_webplugins(self, data: dict = None) -> str:
        return self._request('POST', f'/webplugins', data=data)

    def delete_webplugins_by_s(self, ids: str) -> str:
        return self._request('DELETE', f'/webplugins/{ids}')

    def get_webplugins_by_plugin(self, plugin_id: int) -> str:
        return self._request('GET', f'/webplugins/{plugin_id}')
