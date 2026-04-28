import json
import requests
import hmac
import hashlib
import base64
from typing import List, Dict, Any, Optional, TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.tools import StructuredTool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config import get_llm_config, get_mems_api_config

class AgentState(TypedDict):
    user_input: str
    agent_info: str
    tool_results: List[Dict[str, Any]]
    is_finished: bool
    final_answer: str
    token: Optional[str]
    base_url: str

class MemsAPI:
    def __init__(self, base_url: str = None, username: str = None, password: str = None, secret_key: str = None):
        mems_config = get_mems_api_config()
        self.base_url = base_url or mems_config.get("base_url", "http://localhost:80/api/v1")
        self.token = None
        self.username = username or mems_config.get("username", "admin")
        self.password = password or mems_config.get("password", "")
        self.secret_key = (secret_key or mems_config.get("secret_key", "")).encode("utf-8")
    
    def login(self) -> str:
        encrypted_password = hmac.new(self.secret_key, self.password.encode('utf-8'), hashlib.sha256).digest()
        base64_password = base64.b64encode(encrypted_password).decode('utf-8')
        login_data = [self.username, base64_password]
        response = requests.post(f'{self.base_url}/auth/login', json=login_data, timeout=10)
        if response.status_code == 200:
            data = response.json()
            self.token = data[0]
            return f"登录成功，用户ID: {data[1]}, 用户名: {data[2]}"
        return f"登录失败: {response.text}"
    
    def get_users(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/auth/users', headers=headers, timeout=10)
        if response.status_code == 200:
            users = response.json()
            return json.dumps(users, ensure_ascii=False, indent=2)
        return f"获取用户列表失败: {response.text}"
    
    def get_user(self, user_id: int) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/auth/users/{user_id}', headers=headers, timeout=10)
        if response.status_code == 200:
            return json.dumps(response.json(), ensure_ascii=False, indent=2)
        return f"获取用户失败: {response.text}"
    
    def get_roles(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/auth/roles', headers=headers, timeout=10)
        if response.status_code == 200:
            roles = response.json()
            return json.dumps(roles, ensure_ascii=False, indent=2)
        return f"获取角色列表失败: {response.text}"
    
    def get_alarms(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/alarms', headers=headers, timeout=10)
        if response.status_code == 200:
            alarms = response.json()
            return json.dumps(alarms, ensure_ascii=False, indent=2)
        return f"获取告警列表失败: {response.text}"
    
    def get_alarm_count(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/alarm/count', headers=headers, timeout=10)
        if response.status_code == 200:
            return json.dumps(response.json(), ensure_ascii=False, indent=2)
        return f"获取告警数量失败: {response.text}"
    
    def get_unconfirmed_alarm_count(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/alarm/unconfirmed_number', headers=headers, timeout=10)
        if response.status_code == 200:
            return json.dumps(response.json(), ensure_ascii=False, indent=2)
        return f"获取未确认告警数量失败: {response.text}"
    
    def get_points(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/points/models', headers=headers, timeout=10)
        if response.status_code == 200:
            points = response.json()
            return json.dumps(points, ensure_ascii=False, indent=2)
        return f"获取测点列表失败: {response.text}"
    
    def get_devices(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/devices/devs', headers=headers, timeout=10)
        if response.status_code == 200:
            devices = response.json()
            return json.dumps(devices, ensure_ascii=False, indent=2)
        return f"获取设备列表失败: {response.text}"
    
    def get_device_defines(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/devices/defines', headers=headers, timeout=10)
        if response.status_code == 200:
            defines = response.json()
            return json.dumps(defines, ensure_ascii=False, indent=2)
        return f"获取设备定义失败: {response.text}"
    
    def get_topology(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/devices/cns', headers=headers, timeout=10)
        if response.status_code == 200:
            cns = response.json()
            return json.dumps(cns, ensure_ascii=False, indent=2)
        return f"获取设备拓扑失败: {response.text}"
    
    def get_lcc_list(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/lcc_list', headers=headers, timeout=10)
        if response.status_code == 200:
            lcc_list = response.json()
            return json.dumps(lcc_list, ensure_ascii=False, indent=2)
        return f"获取LCC列表失败: {response.text}"
    
    def get_config(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/config', headers=headers, timeout=10)
        if response.status_code == 200:
            config = response.json()
            return json.dumps(config, ensure_ascii=False, indent=2)
        return f"获取配置失败: {response.text}"
    
    def get_aoe_models(self) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.get(f'{self.base_url}/aoes/models', headers=headers, timeout=10)
        if response.status_code == 200:
            aoes = response.json()
            return json.dumps(aoes, ensure_ascii=False, indent=2)
        return f"获取AOE列表失败: {response.text}"
    
    def confirm_alarm(self, user_id: int) -> str:
        if not self.token:
            self.login()
        headers = {'Access-Token': self.token}
        response = requests.post(f'{self.base_url}/alarm/confirm/{user_id}', headers=headers, timeout=10)
        if response.status_code == 200:
            return "告警确认成功"
        return f"告警确认失败: {response.text}"

class MemsAgent:
    def __init__(self, api_key: str = None, base_url: str = None):
        llm_config = get_llm_config()
        self.mems_api = MemsAPI(base_url=base_url)
        self.llm = ChatOpenAI(
            model=llm_config.get("model", "gpt-4o-mini"),
            api_key=api_key or llm_config.get("api_key"),
            base_url=llm_config.get("base_url", "https://yunwu.ai/")
        )
        self.tools = self._create_tools()
        self.graph = self._build_graph()
    
    def _create_tools(self) -> List[StructuredTool]:
        tools = []
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.login,
            name="login",
            description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_users,
            name="get_users",
            description="获取所有用户列表，返回用户信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_user,
            name="get_user",
            description="根据用户ID获取指定用户的详细信息。",
            args_schema={"user_id": {"type": "integer", "description": "用户ID"}}
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_roles,
            name="get_roles",
            description="获取所有角色列表，返回角色信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_alarms,
            name="get_alarms",
            description="获取所有告警列表，返回告警信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_alarm_count,
            name="get_alarm_count",
            description="获取告警总数。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_unconfirmed_alarm_count,
            name="get_unconfirmed_alarm_count",
            description="获取未确认的告警数量。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_points,
            name="get_points",
            description="获取所有测点列表，返回测点信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_devices,
            name="get_devices",
            description="获取所有设备列表，返回设备信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_device_defines,
            name="get_device_defines",
            description="获取所有设备定义列表，返回设备定义信息数组。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_topology,
            name="get_topology",
            description="获取设备拓扑信息。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_lcc_list,
            name="get_lcc_list",
            description="获取所有LCC设备列表。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_config,
            name="get_config",
            description="获取系统配置信息。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.get_aoe_models,
            name="get_aoe_models",
            description="获取所有AOE模型列表。"
        ))
        
        tools.append(StructuredTool.from_function(
            func=self.mems_api.confirm_alarm,
            name="confirm_alarm",
            description="确认告警。",
            args_schema={"user_id": {"type": "integer", "description": "用户ID"}}
        ))
        
        return tools
    
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
        tools_info = "\n".join([f"- {tool.name}: {tool.description}" for tool in self.tools])
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """
你是一个MEMS系统的AI助手，能够调用多个API工具来完成用户的任务。

可用工具列表：
{tools_info}

请根据用户的请求，决定下一步操作：
1. 如果需要调用工具获取信息，请输出JSON格式：{{"action": "tool", "tool_name": "工具名称", "args": {{参数}}}}
2. 如果已经收集到足够的信息可以直接回答用户，请输出JSON格式：{{"action": "summarize", "reason": "总结原因"}}

注意：
- 调用工具时，参数必须正确传递
- 登录是调用其他接口的前提，如果还未登录，需要先调用login工具
- 请仔细分析用户的问题，判断需要调用哪些工具
"""),
            ("human", "用户问题：{user_input}\n\n历史工具调用结果：{tool_results}")
        ])
        
        chain = prompt | self.llm | JsonOutputParser()
        result = chain.invoke({
            "tools_info": tools_info,
            "user_input": state["user_input"],
            "tool_results": str(state["tool_results"])
        })
        
        state["agent_info"] = json.dumps(result)
        return state
    
    def _tool_node(self, state: AgentState) -> AgentState:
        try:
            agent_info = json.loads(state["agent_info"])
            tool_name = agent_info.get("tool_name")
            args = agent_info.get("args", {})
            
            tool = next((t for t in self.tools if t.name == tool_name), None)
            if tool:
                result = tool.run(**args)
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": result
                })
            else:
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": f"工具 {tool_name} 不存在"
                })
        except Exception as e:
            state["tool_results"].append({
                "tool_name": "unknown",
                "args": {},
                "result": f"工具调用失败: {str(e)}"
            })
        
        return state
    
    def _summarize_node(self, state: AgentState) -> AgentState:
        prompt = ChatPromptTemplate.from_messages([
            ("system", """
你是一个MEMS系统的AI助手，请根据工具调用结果，用自然、友好的语言总结回答用户的问题。

用户问题：{user_input}

工具调用结果：
{tool_results}

请提供详细、清晰的总结回答。
"""),
            ("human", "")
        ])
        
        chain = prompt | self.llm
        result = chain.invoke({
            "user_input": state["user_input"],
            "tool_results": "\n".join([json.dumps(r, ensure_ascii=False) for r in state["tool_results"]])
        })
        
        state["final_answer"] = result.content
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
            "base_url": self.mems_api.base_url
        }
        
        result = self.graph.invoke(initial_state)
        return result["final_answer"]

if __name__ == "__main__":
    agent = MemsAgent()
    
    print("=== MEMS AI Agent ===")
    print("输入问题来与Agent交互，输入 'exit' 退出")
    print()
    
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'exit':
            print("Agent: 再见！")
            break
        
        try:
            print("Agent: 正在处理...")
            response = agent.run(user_input)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Agent: 处理失败: {str(e)}")
        print()