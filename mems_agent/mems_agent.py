import json
import requests
import hmac
import hashlib
import base64
import time
from typing import List, Dict, Any, Optional, TypedDict
from langgraph.graph import StateGraph, END
from openai import OpenAI
from mems_tools import create_tools, ToolInfo
from config import get_llm_config, get_mems_api_config
from langchain_text_splitters import MarkdownTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class ConversationHistory(TypedDict):
    user_input: str
    agent_response: str
    tool_results: List[Dict[str, Any]]
    timestamp: float

class AgentState(TypedDict):
    user_input: str
    agent_info: str
    tool_results: List[Dict[str, Any]]
    is_finished: bool
    final_answer: str
    token: Optional[str]
    base_url: str
    conversation_history: List[ConversationHistory]

class MemsAPI:
    def __init__(self, base_url: str = None, username: str = None, password: str = None, secret_key: str = None):
        mems_config = get_mems_api_config()
        self.base_url = base_url or mems_config.get("base_url", "http://localhost:80/api/v1")
        self.token = None
        self.username = username or mems_config.get("username", "admin")
        self.password = password or mems_config.get("password", "")
        self.secret_key = (secret_key or mems_config.get("secret_key", "")).encode("utf-8")
    
    def _request(self, method: str, path: str, params: dict = None, data: dict = None) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        url = f'{self.base_url}{path}'
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=10)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, params=params, timeout=10)
            else:
                return json.dumps({"success": False, "message": "不支持的HTTP方法"}, ensure_ascii=False)
            
            if response.status_code == 200:
                return json.dumps({"success": True, "data": response.json()}, ensure_ascii=False)
            return json.dumps({"success": False, "message": f"请求失败: {response.text}"}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"success": False, "message": f"请求异常: {str(e)}"}, ensure_ascii=False)
    
    def login(self) -> str:
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
    
    def get_users(self) -> str:
        return self._request('GET', '/auth/users')
    
    def get_user(self, user_id: int) -> str:
        return self._request('GET', f'/auth/users/{user_id}')
    
    def get_roles(self) -> str:
        return self._request('GET', '/auth/roles')
    
    def get_alarms(self) -> str:
        return self._request('GET', '/alarms')
    
    def get_alarm_count(self) -> str:
        return self._request('GET', '/alarm/count')
    
    def get_unconfirmed_alarm_count(self) -> str:
        return self._request('GET', '/alarm/unconfirmed_number')
    
    def get_points(self) -> str:
        return self._request('GET', '/points/models')
    
    def get_devices(self) -> str:
        return self._request('GET', '/devices/devs')
    
    def get_device_defines(self) -> str:
        return self._request('GET', '/devices/defines')
    
    def get_topology(self) -> str:
        return self._request('GET', '/devices/cns')
    
    def get_lcc_list(self) -> str:
        return self._request('GET', '/lcc_list')
    
    def get_config(self) -> str:
        return self._request('GET', '/config')
    
    def get_aoe_models(self) -> str:
        return self._request('GET', '/aoes/models')
    
    def delete_auths(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/auths/{ids}')
    
    def get_auths(self) -> str:
        return self._request('GET', '/auth/auths')
    
    def get_auths_by_role(self, role_id: int) -> str:
        return self._request('GET', f'/auth/auths/by_role/{role_id}')
    
    def add_auth(self, data: dict) -> str:
        return self._request('POST', '/auth/auths', data=data)
    
    def delete_menus(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/menus/{ids}')
    
    def get_menus(self) -> str:
        return self._request('GET', '/auth/menus')
    
    def get_menus_by_role(self, role_id: int) -> str:
        return self._request('GET', f'/auth/menus/by_role/{role_id}')
    
    def get_menus_by_user(self, user_id: int) -> str:
        return self._request('GET', f'/auth/menus/by_user/{user_id}')
    
    def add_menu(self, data: dict) -> str:
        return self._request('POST', '/auth/menus', data=data)
    
    def register(self, username: str, password: str) -> str:
        try:
            response = requests.post(f'{self.base_url}/auth/register', json=[username, password], timeout=10)
            if response.status_code == 200:
                return json.dumps({"success": True, "message": response.json()}, ensure_ascii=False)
            return json.dumps({"success": False, "message": "注册失败: " + response.text}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"success": False, "message": "注册异常: " + str(e)}, ensure_ascii=False)
    
    def delete_roles(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/roles/{ids}')
    
    def get_roles_by_ids(self, ids: str) -> str:
        return self._request('GET', f'/auth/roles/{ids}')
    
    def add_role(self, data: dict) -> str:
        return self._request('POST', '/auth/roles', data=data)
    
    def update_role(self, data: dict) -> str:
        return self._request('PUT', '/auth/roles', data=data)
    
    def delete_users(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/users/{ids}')
    
    def get_users_by_group(self, group_id: int) -> str:
        return self._request('GET', f'/auth/users/by_user_group/{group_id}')
    
    def delete_user_groups(self, ids: str) -> str:
        return self._request('DELETE', f'/auth/user_groups/{ids}')
    
    def get_user_groups(self) -> str:
        return self._request('GET', '/auth/user_groups')
    
    def get_user_group(self, group_id: int) -> str:
        return self._request('GET', f'/auth/user_groups/{group_id}')
    
    def add_user_group(self, data: dict) -> str:
        return self._request('POST', '/auth/user_groups', data=data)
    
    def update_user_group(self, data: dict) -> str:
        return self._request('PUT', '/auth/user_groups', data=data)
    
    def add_user(self, data: dict) -> str:
        return self._request('POST', '/auth/users', data=data)
    
    def update_user(self, data: dict) -> str:
        return self._request('PUT', '/auth/users', data=data)
    
    def change_password(self, user_id: int, data: dict) -> str:
        return self._request('PUT', f'/auth/users/password/{user_id}', data=data)
    
    def reset_password(self, user_id: int) -> str:
        return self._request('PUT', f'/auth/users/reset_password/{user_id}')
    
    def bind_user_roles(self, user_id: int, data: dict) -> str:
        return self._request('PUT', f'/auth/users/roles/{user_id}', data=data)
    
    def get_users_by_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/auth/users/{lcc_id}')
    
    def get_alarm_config(self) -> str:
        return self._request('GET', '/alarm/config')
    
    def set_alarm_config(self, data: dict) -> str:
        return self._request('POST', '/alarm/config', data=data)
    
    def get_confirmed_alarms(self) -> str:
        return self._request('GET', '/alarm/confirm_status')
    
    def confirm_alarm(self, user_id: int) -> str:
        return self._request('POST', f'/alarm/confirm/{user_id}')
    
    def delete_alarm_defines(self, ids: str) -> str:
        return self._request('DELETE', f'/alarm/defines/{ids}')
    
    def get_alarm_define(self, define_id: int) -> str:
        return self._request('GET', f'/alarm/define/{define_id}')
    
    def get_alarm_defines(self) -> str:
        return self._request('GET', '/alarm/defines')
    
    def add_alarm_define(self, data: dict) -> str:
        return self._request('POST', '/alarm/define', data=data)
    
    def add_alarm_defines(self, data: dict) -> str:
        return self._request('POST', '/alarm/defines', data=data)
    
    def delete_lcc_alarm_defines(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/alarm/defines/{lcc_id}/{ids}')
    
    def get_lcc_alarm_config(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/config/{lcc_id}')
    
    def get_lcc_confirmed_alarms(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/confirm_status/{lcc_id}')
    
    def get_lcc_alarm_count(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/count/{lcc_id}')
    
    def get_lcc_alarm_defines(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/defines/{lcc_id}')
    
    def get_lcc_alarm_define(self, lcc_id: str, define_id: int) -> str:
        return self._request('GET', f'/lcc/alarm/defines/{lcc_id}/{define_id}')
    
    def get_lcc_unconfirmed_alarm_count(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarm/unconfirmed_number/{lcc_id}')
    
    def set_lcc_alarm_config(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/alarm/config/{lcc_id}', data=data)
    
    def confirm_lcc_alarm(self, lcc_id: str, user_id: int) -> str:
        return self._request('POST', f'/lcc/alarm/confirm/{lcc_id}/{user_id}')
    
    def add_lcc_alarm_define(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/alarm/define/{lcc_id}', data=data)
    
    def add_lcc_alarm_defines(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/alarm/defines/{lcc_id}', data=data)
    
    def delete_aoe(self, ids: str) -> str:
        return self._request('DELETE', f'/aoes/models/{ids}')
    
    def delete_aoe_version(self, version_id: int) -> str:
        return self._request('DELETE', f'/aoes/version/{version_id}')
    
    def get_aoe(self, aoe_id: int) -> str:
        return self._request('GET', f'/aoes/models/{aoe_id}')
    
    def get_aoes_for_apply(self) -> str:
        return self._request('GET', '/aoes/models/for_apply')
    
    def get_aoe_by_version(self, version_id: int) -> str:
        return self._request('GET', f'/aoes/models_cbor/by_version/{version_id}')
    
    def get_aoe_versions(self) -> str:
        return self._request('GET', '/aoes/version')
    
    def add_aoe(self, data: dict) -> str:
        return self._request('POST', '/aoes/models', data=data)
    
    def add_aoe_version(self, data: dict) -> str:
        return self._request('POST', '/aoes/version', data=data)
    
    def delete_lcc_aoe(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/aoes/models/{lcc_id}/{ids}')
    
    def get_lcc_aoe(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/aoes/models/{lcc_id}')
    
    def add_lcc_aoe(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/aoes/models/{lcc_id}', data=data)
    
    def get_running_aoe(self) -> str:
        return self._request('GET', '/pscpu/aoes/models')
    
    def get_running_aoe_version(self) -> str:
        return self._request('GET', '/pscpu/aoes/version')
    
    def delete_point(self, ids: str) -> str:
        return self._request('DELETE', f'/points/models/{ids}')
    
    def delete_point_version(self, version_id: int) -> str:
        return self._request('DELETE', f'/points/version/{version_id}')
    
    def get_points_for_apply(self) -> str:
        return self._request('GET', '/points/models/for_apply')
    
    def get_points_remote(self) -> str:
        return self._request('GET', '/points/remote')
    
    def get_point_versions(self) -> str:
        return self._request('GET', '/points/version')
    
    def add_point(self, data: dict) -> str:
        return self._request('POST', '/points/models', data=data)
    
    def update_points_remote(self, data: dict) -> str:
        return self._request('POST', '/points/remote', data=data)
    
    def add_point_version(self, data: dict) -> str:
        return self._request('POST', '/points/version', data=data)
    
    def delete_lcc_point(self, lcc_id: str, point_id: int) -> str:
        return self._request('DELETE', f'/lcc/points/models/{lcc_id}/{point_id}')
    
    def get_lcc_points(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/points/models/{lcc_id}')
    
    def import_lcc_points(self, lcc_id: str) -> str:
        return self._request('POST', f'/lcc/points/import_str/{lcc_id}')
    
    def add_lcc_point(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/points/models/{lcc_id}', data=data)
    
    def get_points_by_dev(self, dev_id: int) -> str:
        return self._request('GET', f'/pscpu/points/by_dev/{dev_id}')
    
    def get_running_points(self) -> str:
        return self._request('GET', '/pscpu/points/models')
    
    def get_running_points_version(self) -> str:
        return self._request('GET', '/pscpu/points/version')
    
    def add_topology(self, data: dict) -> str:
        return self._request('POST', '/devices/cns', data=data)
    
    def delete_device_defines(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/defines/{ids}')
    
    def get_device_define(self, define_id: int) -> str:
        return self._request('GET', f'/devices/defines/{define_id}')
    
    def add_device_define(self, data: dict) -> str:
        return self._request('POST', '/devices/defines', data=data)
    
    def update_device_define(self, data: dict) -> str:
        return self._request('PUT', '/devices/defines', data=data)
    
    def delete_device(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/devs/{ids}')
    
    def clear_resources(self) -> str:
        return self._request('DELETE', '/devices/resources_clear')
    
    def get_device(self, device_id: int) -> str:
        return self._request('GET', f'/devices/devs/{device_id}')
    
    def get_islands(self) -> str:
        return self._request('GET', '/devices/islands')
    
    def add_device(self, data: dict) -> str:
        return self._request('POST', '/devices/devs', data=data)
    
    def apply_islands(self, data: dict) -> str:
        return self._request('POST', '/devices/islands/for_apply', data=data)
    
    def update_device(self, data: dict) -> str:
        return self._request('PUT', '/devices/devs', data=data)
    
    def delete_measure_defs(self) -> str:
        return self._request('DELETE', '/devices/measure_defs')
    
    def get_measure_defs(self) -> str:
        return self._request('GET', '/devices/measure_defs')
    
    def add_measure_def(self, data: dict) -> str:
        return self._request('POST', '/devices/measure_defs', data=data)
    
    def update_measure_def(self, data: dict) -> str:
        return self._request('PUT', '/devices/measure_defs', data=data)
    
    def delete_prop_defines(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/prop_defines/{ids}')
    
    def get_prop_defines(self) -> str:
        return self._request('GET', '/devices/prop_defines')
    
    def delete_prop_groups(self, ids: str) -> str:
        return self._request('DELETE', f'/devices/prop_groups/{ids}')
    
    def get_prop_groups(self) -> str:
        return self._request('GET', '/devices/prop_groups')
    
    def get_prop_groups_by_ids(self, ids: str) -> str:
        return self._request('GET', f'/devices/prop_groups/{ids}')
    
    def add_prop_group(self, data: dict) -> str:
        return self._request('POST', '/devices/prop_groups', data=data)
    
    def update_prop_group(self, data: dict) -> str:
        return self._request('PUT', '/devices/prop_groups', data=data)
    
    def add_prop_define(self, data: dict) -> str:
        return self._request('POST', '/devices/prop_defines', data=data)
    
    def update_prop_define(self, data: dict) -> str:
        return self._request('PUT', '/devices/prop_defines', data=data)
    
    def delete_island_version(self, version_id: int) -> str:
        return self._request('DELETE', f'/devices/version/{version_id}')
    
    def get_island_versions(self) -> str:
        return self._request('GET', '/devices/version')
    
    def add_island_version(self, data: dict) -> str:
        return self._request('POST', '/devices/version', data=data)
    
    def get_lcc(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/{lcc_id}')
    
    def get_lcc_running_aoes(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/running_aoes/{lcc_id}')
    
    def get_lcc_unrun_aoes(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/unrun_aoes/{lcc_id}')
    
    def get_lcc_alarms(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/alarms/{lcc_id}')
    
    def execute_lcc_map(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/common_map/{lcc_id}', data=data)
    
    def get_lcc_config(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/config/{lcc_id}')
    
    def set_lcc_config(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/config/{lcc_id}', data=data)
    
    def execute_lcc_control(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/controls/{lcc_id}', data=data)
    
    def get_lcc_logs(self, lcc_id: str) -> str:
        return self._request('POST', f'/lcc/logs_bytes/{lcc_id}')
    
    def export_lcc_models(self, lcc_id: str, lang: str) -> str:
        return self._request('GET', f'/lcc/allmodels_bytes/{lcc_id}', params={'lang': lang})
    
    def import_lcc_models(self, lcc_id: str, data: dict) -> str:
        return self._request('POST', f'/lcc/allmodels_bytes/{lcc_id}', data=data)
    
    def get_lcc_aoe_results(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/aoe_results/{lcc_id}')
    
    def get_lcc_tag_defines(self, lcc_id: str, group: int) -> str:
        return self._request('GET', f'/lcc/tag_defines/{lcc_id}/{group}')
    
    def get_lcc_tags(self, lcc_id: str, group: int) -> str:
        return self._request('POST', f'/lcc/tags/{lcc_id}/{group}')
    
    def update_lcc_tags(self, lcc_id: str, group: int, data: dict) -> str:
        return self._request('PUT', f'/lcc/tags/{lcc_id}/{group}', data=data)
    
    def delete_lcc_transport(self, lcc_id: str, ids: str) -> str:
        return self._request('DELETE', f'/lcc/transports/models/{lcc_id}/{ids}')
    
    def get_lcc_transport(self, lcc_id: str) -> str:
        return self._request('GET', f'/lcc/transports/models/{lcc_id}')
    
    def get_pscpu_running_aoes(self) -> str:
        return self._request('GET', '/pscpu/running_aoes')
    
    def get_pscpu_unrun_aoes(self) -> str:
        return self._request('GET', '/pscpu/unrun_aoes')
    
    def update_pscpu_aoes(self, data: dict) -> str:
        return self._request('POST', '/pscpu/aoes', data=data)
    
    def control_pscpu_aoes(self, data: dict) -> str:
        return self._request('POST', '/pscpu/controls/aoes', data=data)
    
    def reset_pscpu(self) -> str:
        return self._request('POST', '/pscpu/reset')
    
    def start_pscpu(self) -> str:
        return self._request('POST', '/pscpu/start')
    
    def stop_pscpu(self) -> str:
        return self._request('POST', '/pscpu/stop')
    
    def get_pscpu_info(self) -> str:
        return self._request('GET', '/pscpu/info')
    
    def get_pscpu_island(self) -> str:
        return self._request('GET', '/pscpu/island/models')
    
    def get_pscpu_island_paths(self) -> str:
        return self._request('GET', '/pscpu/island/paths')
    
    def get_pscpu_island_version(self) -> str:
        return self._request('GET', '/pscpu/island/version')
    
    def update_pscpu_island(self, data: dict) -> str:
        return self._request('POST', '/pscpu/island', data=data)
    
    def control_pscpu_points(self, data: dict) -> str:
        return self._request('POST', '/pscpu/controls/points', data=data)
    
    def update_pscpu_points(self, data: dict) -> str:
        return self._request('POST', '/pscpu/points', data=data)
    
    def get_graph_apply_model(self, path: str) -> str:
        return self._request('GET', f'/graphs/apply/models/{path}')
    
    def get_graph_apply_paths(self) -> str:
        return self._request('GET', '/graphs/apply/paths')
    
    def get_graph_apply_version(self) -> str:
        return self._request('GET', '/graphs/apply/version')
    
    def apply_graph_version(self, data: dict) -> str:
        return self._request('POST', '/graphs/apply/version', data=data)
    
    def delete_graph_model(self, path: str) -> str:
        return self._request('DELETE', f'/graphs/models/{path}')
    
    def get_graph_model(self, path: str) -> str:
        return self._request('GET', f'/graphs/models/{path}')
    
    def get_graph_paths(self) -> str:
        return self._request('GET', '/graphs/paths')
    
    def add_graph_model(self, data: dict) -> str:
        return self._request('POST', '/graphs/models', data=data)
    
    def delete_graph_version(self, version_id: int) -> str:
        return self._request('DELETE', f'/graphs/version/{version_id}')
    
    def get_graph_versions(self) -> str:
        return self._request('GET', '/graphs/version')
    
    def commit_graph_version(self, data: dict) -> str:
        return self._request('POST', '/graphs/version', data=data)
    
    def delete_plan(self, ids: str) -> str:
        return self._request('DELETE', f'/plans/models/{ids}')
    
    def get_plans(self) -> str:
        return self._request('GET', '/plans/models')
    
    def get_plans_by_ids(self, ids: str) -> str:
        return self._request('GET', f'/plans/models/by_ids/{ids}')
    
    def get_plan(self, plan_id: int) -> str:
        return self._request('GET', f'/plans/models/{plan_id}')
    
    def delete_plan_paths(self) -> str:
        return self._request('DELETE', '/plans/paths')
    
    def get_plan_paths(self) -> str:
        return self._request('GET', '/plans/paths')
    
    def add_plan_path(self, data: dict) -> str:
        return self._request('POST', '/plans/paths', data=data)
    
    def update_plan_path(self, data: dict) -> str:
        return self._request('PUT', '/plans/paths', data=data)
    
    def add_plan(self, data: dict) -> str:
        return self._request('POST', '/plans/models', data=data)
    
    def update_plan(self, data: dict) -> str:
        return self._request('PUT', '/plans/models', data=data)
    
    def delete_script(self, ids: str) -> str:
        return self._request('DELETE', f'/scripts/{ids}')
    
    def get_script(self, script_id: int) -> str:
        return self._request('GET', f'/scripts/{script_id}')
    
    def add_script(self, data: dict) -> str:
        return self._request('POST', '/scripts', data=data)
    
    def delete_webplugin(self, ids: str) -> str:
        return self._request('DELETE', f'/webplugins/{ids}')
    
    def get_webplugins(self) -> str:
        return self._request('GET', '/webplugins')
    
    def get_webplugin_file(self, plugin_id: int) -> str:
        return self._request('GET', f'/webplugins/file/{plugin_id}')
    
    def get_webplugin(self, plugin_id: int) -> str:
        return self._request('GET', f'/webplugins/{plugin_id}')
    
    def add_webplugin(self, data: dict) -> str:
        return self._request('POST', '/webplugins', data=data)
    
    def add_webplugin_file(self, data: dict) -> str:
        return self._request('POST', '/webplugins/file', data=data)
    
    def get_flow_result(self, result_id: str) -> str:
        return self._request('GET', '/flows/results', params={'id': result_id})
    
    def get_flow_result_json(self, result_id: str) -> str:
        return self._request('GET', '/flows/results_json', params={'id': result_id})
    
    def get_flow_result_json_rows(self, result_id: str) -> str:
        return self._request('GET', '/flows/results_json_rows', params={'id': result_id})
    
    def get_ems(self, ems_id: str) -> str:
        return self._request('GET', f'/ems/{ems_id}')
    
    def get_ems_list(self) -> str:
        return self._request('GET', '/ems_list')
    
    def execute_ems_request(self, ems_id: str, data: dict) -> str:
        return self._request('POST', f'/ems/request/{ems_id}', data=data)
    
    def control_point_by_alias(self, data: dict) -> str:
        return self._request('POST', '/controls/points_by_alias', data=data)
    
    def delete_tag(self, group: int) -> str:
        return self._request('DELETE', f'/tags/{group}')
    
    def get_tags(self, group: int) -> str:
        return self._request('POST', f'/tags/{group}')
    
    def update_tags(self, group: int, data: dict) -> str:
        return self._request('PUT', f'/tags/{group}', data=data)
    
    def get_tag_defines(self, group: int) -> str:
        return self._request('GET', f'/tag_defines/{group}')
    
    def execute_common_map(self, data: dict) -> str:
        return self._request('POST', '/common_map', data=data)
    
    def save_script_wasm(self, data: dict) -> str:
        return self._request('POST', '/script_wasm', data=data)
    
    def get_script_results(self) -> str:
        return self._request('GET', '/script_results')
    
    def get_script_result(self, result_id: int) -> str:
        return self._request('GET', f'/script_results/{result_id}')
    
    def add_script_result(self, data: dict) -> str:
        return self._request('POST', '/script_results', data=data)
    
    def import_models_bytes(self, data: dict) -> str:
        return self._request('POST', '/multi_import_bytes', data=data)
    
    def save_config(self, data: dict) -> str:
        return self._request('POST', '/config', data=data)
    
    def execute_file_tree(self, data: dict) -> str:
        return self._request('POST', '/file_tree', data=data)
    
    def save_file_tree_node(self, tree_id: str, data: dict) -> str:
        return self._request('POST', f'/file_tree/{tree_id}', data=data)
    
    def commit_file_tree_version(self, tree_id: str, data: dict) -> str:
        return self._request('POST', '/file_tree_version', params={'id': tree_id}, data=data)

class MemsAgent:
    def __init__(self, api_key: str = None, base_url: str = None):
        llm_config = get_llm_config()
        self.mems_api = MemsAPI(base_url=base_url)
        self.client = OpenAI(
            api_key=api_key or llm_config.get("api_key"),
            base_url=llm_config.get("base_url", "https://yunwu.ai/v1")
        )
        self.model = llm_config.get("model", "gpt-4o-mini")
        self.tools = create_tools(self.mems_api)
        self.graph = self._build_graph()
        self.conversation_history: List[ConversationHistory] = []
        
        # 加载API文档并初始化RAG系统
        self.rag_system = self._init_rag_system()
    
    def _init_rag_system(self) -> Optional[FAISS]:
        """初始化RAG系统，加载API文档并创建向量存储"""
        try:
            with open('mems_api_docs.md', 'r', encoding='utf-8') as f:
                docs_content = f.read()
            
            # 分割文档
            text_splitter = MarkdownTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = text_splitter.split_text(docs_content)
            
            # 创建文档对象
            documents = [Document(page_content=doc, metadata={"source": "mems_api_docs.md"}) for doc in docs]
            
            # 创建向量存储
            llm_config = get_llm_config()
            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small",
                api_key=llm_config.get("api_key"),
                base_url=llm_config.get("base_url", "https://yunwu.ai/")
            )
            
            db = FAISS.from_documents(documents, embeddings)
            return db
            
        except FileNotFoundError:
            print("警告：未找到mems_api_docs.md文件")
            return None
    
    def _search_docs(self, query: str, k: int = 3) -> List[str]:
        """在API文档中搜索相关内容"""
        if not self.rag_system:
            return []
        
        results = self.rag_system.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    
    def _call_llm(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt}
                ],
                temperature=0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return json.dumps({"action": "summarize", "reason": "LLM调用失败: " + str(e)})
    
    def _build_graph(self) -> StateGraph:
        workflow = StateGraph(AgentState)
        
        workflow.add_node("agent", self._agent_node)
        workflow.add_node("tool", self._tool_node)
        workflow.add_node("summarize", self._summarize_node)
        
        workflow.set_entry_point("agent")
        workflow.add_edge("tool", "agent")
        workflow.add_edge("summarize", END)
        
        workflow.add_conditional_edges(
            "agent",
            self._decide_next_step,
            {
                "tool": "tool",
                "summarize": "summarize"
            }
        )
        
        return workflow.compile()
    
    def _agent_node(self, state: AgentState) -> AgentState:
        # 构建工具信息，包含参数描述
        tools_info = []
        for tool in self.tools:
            tool_desc = f"- {tool.name}: {tool.description}"
            if tool.parameters:
                params_desc = "\n  参数："
                for param in tool.parameters:
                    params_desc += f"\n    - {param['name']} ({param['type']}) {'[必填]' if param['required'] else ''}: {param['description']}"
                tool_desc += params_desc
            tools_info.append(tool_desc)
        tools_info = "\n".join(tools_info)
        
        # 构建对话历史字符串
        conversation_history_str = ""
        if state.get("conversation_history"):
            conversation_history_str = "\n对话历史:\n"
            for i, history in enumerate(state["conversation_history"]):
                conversation_history_str += f"\n轮次 {i+1}:\n用户: {history['user_input']}\n助手: {history['agent_response']}\n"
        
        # 搜索API文档相关内容
        relevant_docs = self._search_docs(state["user_input"], k=3)
        docs_content = "\n\n相关文档内容：\n" + "\n\n---\n\n".join(relevant_docs)
        
        prompt = """
你是一个MEMS系统的AI助手，能够调用多个API工具来完成用户的任务。同时你也可以回答关于MEMS API文档的细节问题。

可用工具列表：
{tools_info}

请根据用户的请求、对话历史、历史工具调用结果以及相关文档内容，决定下一步操作：

输出格式要求（必须是有效的JSON格式）：
1. 如果需要调用工具获取信息，请输出：
{{"action": "tool", "tool_name": "工具名称", "args": {{参数对象}}}}

2. 如果已经有足够的信息回答问题（包括API文档中的细节），请输出：
{{"action": "summarize", "reason": "总结原因"}}

注意事项：
- 调用工具时，参数必须正确传递，参数值必须与类型匹配
- 登录是调用其他接口的前提，如果还未登录或者token失效，需要先调用login工具
- 请仔细分析用户的问题，判断需要调用哪些工具
- 如果需要调用多个工具，可以依次调用
- 如果用户的问题是关于API文档的细节，不需要调用工具，直接总结回答
- 输出必须是纯JSON格式，不要包含其他任何文本

{conversation_history_str}
用户问题：{user_input}

历史工具调用结果：{tool_results}

{docs_content}
""".format(
            tools_info=tools_info,
            conversation_history_str=conversation_history_str,
            user_input=state["user_input"],
            tool_results=str(state["tool_results"]),
            docs_content=docs_content
        )
        
        response = self._call_llm(prompt)
        
        try:
            result = json.loads(response)
        except:
            result = {"action": "summarize", "reason": "无法解析工具调用指令"}
        
        state["agent_info"] = json.dumps(result)
        return state
    
    def _tool_node(self, state: AgentState) -> AgentState:
        try:
            agent_info = json.loads(state["agent_info"])
            tool_name = agent_info.get("tool_name")
            args = agent_info.get("args", {})
            
            print(f"[工具调用] ──────────────────────────────")
            print(f"[工具调用] 工具名称: {tool_name}")
            print(f"[工具调用] 输入参数: {json.dumps(args, ensure_ascii=False)}")
            
            tool = next((t for t in self.tools if t.name == tool_name), None)
            if tool:
                if args:
                    result = tool.func(**args)
                else:
                    result = tool.func()
                
                print(f"[工具调用] 输出结果: {result[:200]}{'...' if len(result) > 200 else ''}")
                print(f"[工具调用] 工具 {tool_name} 调用成功")
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": result,
                    "timestamp": time.time()
                })
            else:
                error_msg = json.dumps({"success": False, "message": "工具 " + tool_name + " 不存在"}, ensure_ascii=False)
                print(f"[工具调用] 输出结果: {error_msg}")
                print(f"[工具调用] 工具 {tool_name} 不存在")
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": error_msg,
                    "timestamp": time.time()
                })
        except Exception as e:
            error_msg = json.dumps({"success": False, "message": "工具调用失败: " + str(e)}, ensure_ascii=False)
            print(f"[工具调用] 输出结果: {error_msg}")
            print(f"[工具调用] 工具调用失败: {str(e)}")
            state["tool_results"].append({
                "tool_name": "unknown",
                "args": {},
                "result": error_msg,
                "timestamp": time.time()
            })
        
        return state
    
    def _summarize_node(self, state: AgentState) -> AgentState:
        # 搜索API文档相关内容
        relevant_docs = self._search_docs(state["user_input"], k=3)
        docs_content = "\n\n相关文档内容：\n" + "\n\n---\n\n".join(relevant_docs)
        
        prompt = """
你是一个MEMS系统的AI助手，请根据工具调用结果、对话历史和相关文档内容，用自然、友好的语言总结回答用户的问题。

用户问题：{user_input}

工具调用结果：
{tool_results}

{docs_content}

请提供详细、清晰的总结回答，包括：
1. 解决用户问题的步骤
2. 获取到的具体数据
3. 必要的分析和建议

输出格式：
- 使用中文回答
- 保持回答简洁明了
- 如果有错误信息，请告知用户
- 如果用户的问题是关于API文档的细节，直接从文档中提取信息回答
""".format(
            user_input=state["user_input"],
            tool_results="\n".join([json.dumps(r, ensure_ascii=False) for r in state["tool_results"]]),
            docs_content=docs_content
        )
        
        response = self._call_llm(prompt)
        state["final_answer"] = response
        state["is_finished"] = True
        return state
    
    def _decide_next_step(self, state: AgentState) -> str:
        try:
            agent_info = json.loads(state["agent_info"])
            action = agent_info.get("action", "summarize")
            return action
        except:
            return "summarize"
    
    def run(self, user_input: str) -> str:
        initial_state = {
            "user_input": user_input,
            "agent_info": "",
            "tool_results": [],
            "is_finished": False,
            "final_answer": "",
            "token": None,
            "base_url": self.mems_api.base_url,
            "conversation_history": self.conversation_history.copy()
        }
        
        result = self.graph.invoke(initial_state)
        
        # 保存当前对话到历史
        if result.get("final_answer"):
            self.conversation_history.append({
                "user_input": user_input,
                "agent_response": result["final_answer"],
                "tool_results": result["tool_results"],
                "timestamp": time.time()
            })
        
        return result["final_answer"]
    
    def reset_conversation(self):
        """重置对话历史"""
        self.conversation_history = []

def main():
    try:
        agent = MemsAgent()
        print("=" * 50)
        print("     MEMS AI Agent 智能助手")
        print("=" * 50)
        print("支持的功能模块：")
        print("  - Auth: 用户管理、角色管理、权限管理、菜单管理")
        print("  - Alarm: 告警管理、告警定义、告警确认")
        print("  - Aoes: AOE模型管理、版本管理")
        print("  - Points: 测点管理、版本管理")
        print("  - Devices: 设备管理、设备定义、电气岛")
        print("  - LCC: LCC设备管理、告警、配置")
        print("  - Pscpu: 运行状态、AOE控制、测点控制")
        print("  - Graphs: SVG图表管理、版本管理")
        print("  - Plans: 计划管理")
        print("  - Scripts: 脚本管理")
        print("  - Webplugins: 界面插件管理")
        print("  - Flows: 报表执行结果查询")
        print("  - Ems: EMS管理")
        print("  - Controls: 测点控制")
        print("  - Tags: 标签管理")
        print("  - Common: 通用功能")
        print("=" * 50)
        print(f"共 {len(agent.tools)} 个工具可用")
        print("输入问题来与Agent交互，输入 'exit' 退出，输入 'reset' 重置对话历史")
        print()
        
        while True:
            user_input = input("你: ")
            if user_input.lower() == 'exit':
                print("Agent: 再见！")
                break
            
            if user_input.lower() == 'reset':
                agent.reset_conversation()
                print("Agent: 对话历史已重置")
                continue
            
            if not user_input.strip():
                print("Agent: 请输入有效的问题")
                continue
            
            try:
                print("Agent: 正在处理...")
                start_time = time.time()
                response = agent.run(user_input)
                elapsed_time = time.time() - start_time
                print("Agent (" + str(elapsed_time)[:5] + "秒):")
                print("  " + response)
            except Exception as e:
                print("Agent: 处理失败: " + str(e))
            print()
            
    except Exception as e:
        print("初始化Agent失败: " + str(e))

if __name__ == "__main__":
    main()