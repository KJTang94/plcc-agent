
import json
import requests
import hmac
import hashlib
import base64
import time
import re
from typing import List, Dict, Any, Optional, TypedDict
from pathlib import Path
from langgraph.graph import StateGraph, END
from openai import OpenAI
from config import get_llm_config, get_plcc_api_config


class AgentState(TypedDict):
    user_input: str
    agent_info: str
    tool_results: List[Dict[str, Any]]
    is_finished: bool
    final_answer: str
    token: Optional[str]
    base_url: str


class ToolInfo:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func


class PlccAPI:
    def __init__(self, base_url: str = None, username: str = None, password: str = None, secret_key: str = None):
        plcc_config = get_plcc_api_config()
        self.base_url = base_url or plcc_config.get("base_url", "http://localhost:80/api/v1")
        self.token = None
        self.username = username or plcc_config.get("username", "admin")
        self.password = password or plcc_config.get("password", "")
        self.secret_key = (secret_key or plcc_config.get("secret_key", "")).encode("utf-8")

    def _request(self, method: str, path: str, params: dict = None, data: dict = None) -> str:
        if not self.token and not path.endswith("/auth/login") and not path.endswith("/auth/register"):
            self.login()
        
        headers = {}
        if self.token:
            headers['Access-Token'] = self.token
        
        url = f'{self.base_url}{path}'
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=10)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method.upper() == 'PUT':
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers, params=params, timeout=10)
            else:
                return json.dumps({"success": False, "message": "不支持的HTTP方法"}, ensure_ascii=False)
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    return json.dumps({"success": True, "data": result}, ensure_ascii=False)
                except:
                    return json.dumps({"success": True, "data": response.text}, ensure_ascii=False)
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


def load_openapi_spec():
    openapi_path = Path(__file__).parent / "openapi.json"
    with open(openapi_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_api_list():
    api_list_path = Path(__file__).parent / "api_list.json"
    with open(api_list_path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_description_from_api_info(api_info: Dict[str, Any]) -> str:
    """根据API信息构建详细的工具描述"""
    parts = []
    
    # 添加摘要
    if api_info.get("summary"):
        parts.append(api_info["summary"])
    
    # 添加方法和路径
    method = api_info.get("method", "GET").upper()
    path = api_info.get("path", "")
    parts.append(f"[{method}] {path}")
    
    # 添加参数信息
    if "parameters" in api_info and api_info["parameters"]:
        parts.append("参数:")
        for param in api_info["parameters"]:
            param_name = param.get("name", "")
            param_in = param.get("in", "")
            param_required = param.get("required", False)
            param_desc = param.get("description", "")
            param_schema = param.get("schema", {})
            param_type = param_schema.get("type", "any")
            
            required_mark = " [必填]" if param_required else ""
            parts.append(f"  - {param_name} ({param_in}, {param_type}){required_mark}: {param_desc}")
    
    # 添加请求体信息
    if "requestBody" in api_info:
        req_body = api_info["requestBody"]
        req_required = req_body.get("required", False)
        req_required_mark = " [必填]" if req_required else ""
        req_content_type = req_body.get("contentType", "application/json")
        parts.append(f"请求体{req_required_mark} ({req_content_type}):")
        
        # 简化的schema描述
        req_schema = req_body.get("schema", {})
        if req_schema.get("type") == "object" and "properties" in req_schema:
            for prop_name, prop_info in req_schema["properties"].items():
                prop_type = prop_info.get("type", "any")
                prop_desc = prop_info.get("description", "")
                prop_required = prop_name in req_schema.get("required", [])
                prop_required_mark = " [必填]" if prop_required else ""
                parts.append(f"  - {prop_name} ({prop_type}){prop_required_mark}: {prop_desc}")
    
    return " ".join(parts)


def create_tools_from_openapi(plcc_api: PlccAPI) -> List[ToolInfo]:
    tools = []
    
    # 首先添加登录工具
    tools.append(ToolInfo(
        name="login",
        description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。",
        func=plcc_api.login
    ))
    
    # 从 api_list.json 创建其他工具
    try:
        api_list = load_api_list()
        for api_info in api_list:
            operation_id = api_info.get("operationId", "")
            if not operation_id:
                continue
            
            method = api_info.get("method", "GET")
            path = api_info.get("path", "")
            
            # 创建工具函数
            def create_api_func(method_name=method, path_name=path, op_id=operation_id):
                def api_func(**kwargs):
                    # 从 kwargs 中提取参数
                    params = {}
                    data = {}
                    actual_path = path_name
                    
                    # 从路径中提取参数
                    path_params = re.findall(r'\{([^}]+)\}', actual_path)
                    for param in path_params:
                        if param in kwargs:
                            actual_path = actual_path.replace(f'{{{param}}}', str(kwargs[param]))
                    
                    # 处理查询参数和请求体
                    for key, value in kwargs.items():
                        if key not in path_params:
                            if method_name.upper() in ['GET', 'DELETE']:
                                params[key] = value
                            else:
                                data[key] = value
                    
                    # 如果 data 只有一个 'data' 键，直接使用其值
                    if 'data' in data and len(data) == 1:
                        data = data['data']
                    
                    return plcc_api._request(method_name, actual_path, params=params, data=data)
                return api_func
            
            func = create_api_func()
            
            # 构建详细的工具描述
            description = build_description_from_api_info(api_info)
            tools.append(ToolInfo(
                name=operation_id,
                description=description,
                func=func
            ))
    except Exception as e:
        print(f"警告: 无法加载api_list.json，将使用openapi.json: {str(e)}")
        # 如果api_list.json加载失败，回退到原来的方法
        openapi_spec = load_openapi_spec()
        for path, methods in openapi_spec["paths"].items():
            for method, operation in methods.items():
                operation_id = operation.get("operationId", "")
                if not operation_id:
                    continue
                
                summary = operation.get("summary", "")
                
                # 创建工具函数
                def create_api_func_backup(method_name=method, path_name=path, op_id=operation_id):
                    def api_func(**kwargs):
                        params = {}
                        data = {}
                        actual_path = path_name
                        
                        path_params = re.findall(r'\{([^}]+)\}', actual_path)
                        for param in path_params:
                            if param in kwargs:
                                actual_path = actual_path.replace(f'{{{param}}}', str(kwargs[param]))
                        
                        for key, value in kwargs.items():
                            if key not in path_params:
                                if method_name.upper() in ['GET', 'DELETE']:
                                    params[key] = value
                                else:
                                    data[key] = value
                        
                        if 'data' in data and len(data) == 1:
                            data = data['data']
                        
                        return plcc_api._request(method_name, actual_path, params=params, data=data)
                    return api_func
                
                func = create_api_func_backup()
                description = summary or operation_id
                tools.append(ToolInfo(
                    name=operation_id,
                    description=description,
                    func=func
                ))
    
    return tools


class PlccAgent:
    def __init__(self, api_key: str = None, base_url: str = None):
        llm_config = get_llm_config()
        self.plcc_api = PlccAPI(base_url=base_url)
        self.client = OpenAI(
            api_key=api_key or llm_config.get("api_key"),
            base_url=llm_config.get("base_url", "https://yunwu.ai/v1")
        )
        self.model = llm_config.get("model", "gpt-4o-mini")
        self.tools = create_tools_from_openapi(self.plcc_api)
        self.graph = self._build_graph()

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
        # 为了避免描述太长，我们将工具信息精简显示
        tools_info = []
        for tool in self.tools:
            desc = tool.description
            # 如果描述太长，只显示前200个字符
            if len(desc) > 200:
                desc = desc[:200] + "..."
            tools_info.append(f"- {tool.name}: {desc}")
        
        tools_info_str = "\n".join(tools_info)
        
        prompt = f"""
你是一个PLCC系统的AI助手，能够调用多个API工具来完成用户的任务。

可用工具列表：
{tools_info_str}

请根据用户的请求和历史工具调用结果，决定下一步操作：

输出格式要求（必须是有效的JSON格式）：
1. 如果需要调用工具获取信息，请输出：
{{
  "action": "tool", 
  "tool_name": "工具名称", 
  "args": {{
    "参数名": "参数值", 
    ...
  }}
}}

2. 如果已经收集到足够的信息可以直接回答用户，请输出：
{{"action": "summarize", "reason": "总结原因"}}

注意事项：
- 调用工具时，必须仔细阅读工具描述中的参数信息，确保参数正确传递
- 参数值必须与类型匹配（整数应该用数字，字符串应该用引号等）
- 对于必填参数，必须提供
- 登录是调用其他接口的前提，如果还未登录或者token失效，需要先调用login工具
- 请仔细分析用户的问题，判断需要调用哪些工具
- 如果需要调用多个工具，可以依次调用
- 如果已经有足够的信息回答问题，请直接总结
- 输出必须是纯JSON格式，不要包含其他任何文本

用户问题：{state["user_input"]}

历史工具调用结果：{str(state["tool_results"])}
"""
        
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
            
            print(f"[工具调用] --------------------------")
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
        prompt = f"""
你是一个PLCC系统的AI助手，请根据工具调用结果，用自然、友好的语言总结回答用户的问题。

用户问题：{state["user_input"]}

工具调用结果：
{chr(10).join([json.dumps(r, ensure_ascii=False) for r in state["tool_results"]])}

请提供详细、清晰的总结回答，包括：
1. 解决用户问题的步骤
2. 获取到的具体数据
3. 必要的分析和建议

输出格式：
- 使用中文回答
- 保持回答简洁明了
- 如果有错误信息，请告知用户
"""
        
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
            "base_url": self.plcc_api.base_url
        }
        
        result = self.graph.invoke(initial_state)
        return result["final_answer"]


def main():
    try:
        agent = PlccAgent()
        print("=" * 50)
        print("     PLCC AI Agent 智能助手")
        print("=" * 50)
        print(f"共 {len(agent.tools)} 个工具可用")
        print("输入问题来与Agent交互，输入 'exit' 退出")
        print()
        
        while True:
            user_input = input("你: ")
            if user_input.lower() == 'exit':
                print("Agent: 再见！")
                break
            
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

