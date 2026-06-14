import json
import re
import time
from typing import List, Dict, Any
from langgraph.graph import StateGraph, END
from openai import OpenAI
from mems_api import MemsAPI
from mems_tools import create_tools, ToolInfo
from config import get_llm_config
from memory import AgentState, MemoryManager
from prompts import build_agent_system_prompt, build_agent_user_message, build_summarize_system_prompt, build_summarize_user_message


class MemsAgent:
    def __init__(self, api_key: str = None, base_url: str = None):
        llm_config = get_llm_config()
        self.mems_api = MemsAPI(base_url=base_url)
        self.client = OpenAI(
            api_key=api_key or llm_config.get("api_key"),
            base_url=llm_config.get("base_url", "https://yunwu.ai/v1")
        )
        self.model = llm_config.get("model", "gpt-4o-mini")
        self.max_tool_steps = 15
        self.max_same_call_repeats = 2
        self.max_tools_in_prompt = 25
        self.max_tool_results_in_prompt = 4
        self.max_tool_result_chars = 1500
        self.tools = create_tools(self.mems_api)
        self.memory = MemoryManager()
        self.memory.build_tool_index(self.tools)
        self.graph = self._build_graph()
    
    def _call_llm(self, system_prompt: str, user_message: str = None) -> str:
        try:
            messages = [{"role": "system", "content": system_prompt}]

            if user_message:
                messages.append({"role": "user", "content": user_message})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return json.dumps({"action": "summarize", "reason": "LLM调用失败: " + str(e)})

    def _build_conversation_history_str(self, state: AgentState) -> str:
        history = state.get("conversation_history") or []
        if not history:
            return ""

        recent_history = history[-2:]
        parts = ["\n最近对话历史（仅保留最近2轮，历史只用于参考，不覆盖当前问题）："]
        for i, history_item in enumerate(recent_history, start=1):
            parts.append(f"\n轮次 {i}:")
            parts.append(f"用户: {history_item['user_input']}")
            if history_item.get("tool_results"):
                tool_summary = "; ".join(
                    f"{r['tool_name']}({json.dumps(r.get('args', {}), ensure_ascii=False)})" for r in history_item["tool_results"]
                )
                parts.append(f"工具调用: {tool_summary}")
            parts.append(f"助手: {history_item['agent_response']}")
        return "\n".join(parts)

    def _build_search_query(self, state: AgentState) -> str:
        """构建检索查询：以当前问题为主，追加最近一轮用户输入作为上下文，
        以便对指代型追问（如"那它的详情呢"）也能召回相关工具与文档。"""
        user_input = state["user_input"]
        history = state.get("conversation_history") or []
        if history:
            last_user_input = history[-1].get("user_input", "")
            if last_user_input:
                return f"{user_input}\n{last_user_input}"
        return user_input

    
    def _get_tool_call_signature(self, tool_name: str, args: Dict[str, Any]) -> str:
        return f"{tool_name}:{json.dumps(args or {}, ensure_ascii=False, sort_keys=True)}"

    def _count_same_tool_call(self, state: AgentState, tool_name: str, args: Dict[str, Any]) -> int:
        signature = self._get_tool_call_signature(tool_name, args)
        return sum(
            1
            for item in state.get("tool_results", [])
            if self._get_tool_call_signature(item.get("tool_name", ""), item.get("args", {})) == signature
        )

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
    
    def _select_relevant_tools(self, state: AgentState) -> List[ToolInfo]:
        """复用整轮预检索得到的工具子集，始终保留 login 与本轮已调用过的工具。
        索引不可用或工具总数较少时回退为全量工具。"""
        if len(self.tools) <= self.max_tools_in_prompt:
            return self.tools

        relevant_names = set(state.get("relevant_tool_names") or [])
        if not relevant_names:
            return self.tools

        relevant_names.add("login")
        for result in state.get("tool_results", []):
            relevant_names.add(result.get("tool_name"))

        return [tool for tool in self.tools if tool.name in relevant_names]

    def _format_tool_results(self, tool_results: List[Dict[str, Any]], max_results: int = None) -> str:
        """仅保留最近若干条工具结果并对单条做字符截断，避免 prompt 无限膨胀。
        max_results 为 None 时使用默认上限；汇总场景可传更大值以保留更多结果。"""
        if not tool_results:
            return "[]"

        limit = max_results if max_results is not None else self.max_tool_results_in_prompt
        recent = tool_results[-limit:]
        omitted = len(tool_results) - len(recent)
        lines = []
        if omitted > 0:
            lines.append(f"（已省略较早的 {omitted} 条工具调用结果）")
        for result in recent:
            result_str = str(result.get("result", ""))
            if len(result_str) > self.max_tool_result_chars:
                result_str = result_str[:self.max_tool_result_chars] + "...(已截断)"
            lines.append(json.dumps({
                "tool_name": result.get("tool_name"),
                "args": result.get("args", {}),
                "result": result_str,
            }, ensure_ascii=False))
        return "\n".join(lines)

    def _parse_agent_response(self, response: str) -> Dict[str, Any]:
        """解析LLM输出的JSON指令，对常见的非纯JSON输出做兜底提取。"""
        if not response:
            return {"action": "summarize", "reason": "LLM返回为空"}

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            pass

        # 兜底1：去除 ```json ... ``` 代码块包裹
        fenced = re.search(r"```(?:json)?\s*(.*?)\s*```", response, re.DOTALL)
        if fenced:
            try:
                return json.loads(fenced.group(1))
            except json.JSONDecodeError:
                pass

        # 兜底2：提取首个 { 到末个 } 之间的内容
        start = response.find("{")
        end = response.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(response[start:end + 1])
            except json.JSONDecodeError:
                pass

        return {"action": "summarize", "reason": "无法解析工具调用指令"}

    def _agent_node(self, state: AgentState) -> AgentState:
        tools_info = []
        for tool in self._select_relevant_tools(state):
            tool_desc = f"- {tool.name}: {tool.description}"
            if tool.parameters:
                params_desc = "\n  参数："
                for param in tool.parameters:
                    params_desc += f"\n    - {param['name']} ({param['type']}) {'[必填]' if param['required'] else ''}: {param['description']}"
                tool_desc += params_desc
            tools_info.append(tool_desc)
        tools_info = "\n".join(tools_info)

        conversation_history_str = self._build_conversation_history_str(state)

        docs_content = state.get("docs_content", "")

        system_prompt = build_agent_system_prompt(tools_info=tools_info)
        user_message = build_agent_user_message(
            conversation_history_str=conversation_history_str,
            user_input=state["user_input"],
            tool_results=self._format_tool_results(state["tool_results"]),
            docs_content=docs_content,
        )

        response = self._call_llm(system_prompt, user_message=user_message)

        result = self._parse_agent_response(response)
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

            same_call_count = self._count_same_tool_call(state, tool_name, args)
            if same_call_count >= self.max_same_call_repeats:
                loop_msg = json.dumps({"success": False, "message": f"检测到重复调用工具 {tool_name} 且参数相同，已自动停止继续调用以避免死循环"}, ensure_ascii=False)
                print(f"[工具调用] 输出结果: {loop_msg}")
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": loop_msg,
                    "timestamp": time.time()
                })
                state["agent_info"] = json.dumps({"action": "summarize", "reason": "重复工具调用触发保护"}, ensure_ascii=False)
                return state
            
            tool = next((t for t in self.tools if t.name == tool_name), None)
            if tool:
                if args:
                    import inspect
                    # 获取方法签名，区分路径/查询参数和请求体参数
                    sig = inspect.signature(tool.func)
                    params = set(sig.parameters.keys())
                    accepts_body = "data" in params

                    path_query_args = {}
                    body_args = {}

                    for key, value in args.items():
                        if key == "data" and accepts_body:
                            # 模型按约定显式给出的请求体，直接作为 data 传递
                            path_query_args["data"] = value
                        elif key in params:
                            # 路径参数或查询参数，直接传递
                            path_query_args[key] = value
                        elif accepts_body:
                            # 兼容请求体字段被平铺到顶层的情况，打包进 data
                            body_args[key] = value
                        # 工具不接受请求体且参数名未知时忽略该参数

                    if body_args:
                        # 与显式 data 合并；显式 data 优先
                        if isinstance(path_query_args.get("data"), dict):
                            merged = {**body_args, **path_query_args["data"]}
                            path_query_args["data"] = merged
                        elif "data" not in path_query_args:
                            path_query_args["data"] = body_args

                    result = tool.func(**path_query_args)
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
                error_msg = json.dumps({"success": False, "message": "工具 " + str(tool_name) + " 不存在"}, ensure_ascii=False)
                print(f"[工具调用] 输出结果: {error_msg}")
                print(f"[工具调用] 工具 {tool_name} 不存在")
                state["tool_results"].append({
                    "tool_name": tool_name,
                    "args": args,
                    "result": error_msg,
                    "timestamp": time.time()
                })
                state["agent_info"] = json.dumps({"action": "summarize", "reason": "工具不存在"}, ensure_ascii=False)
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
            state["agent_info"] = json.dumps({"action": "summarize", "reason": "工具调用异常"}, ensure_ascii=False)
        
        return state
    
    def _summarize_node(self, state: AgentState) -> AgentState:
        try:
            agent_info = json.loads(state["agent_info"])
            if agent_info.get("answer"):
                state["final_answer"] = agent_info["answer"]
                state["is_finished"] = True
                return state
        except:
            pass

        docs_content = state.get("docs_content", "")

        conversation_history_str = self._build_conversation_history_str(state)

        system_prompt = build_summarize_system_prompt()
        user_message = build_summarize_user_message(
            user_input=state["user_input"],
            tool_results=self._format_tool_results(state["tool_results"], max_results=self.max_tool_steps),
            docs_content=docs_content,
            conversation_history_str=conversation_history_str,
        )

        response = self._call_llm(system_prompt, user_message=user_message)
        state["final_answer"] = response
        state["is_finished"] = True
        return state
    
    def _decide_next_step(self, state: AgentState) -> str:
        if len(state.get("tool_results", [])) >= state.get("max_steps", self.max_tool_steps):
            state["agent_info"] = json.dumps({"action": "summarize", "reason": "达到最大工具调用次数限制"}, ensure_ascii=False)
            return "summarize"

        try:
            agent_info = json.loads(state["agent_info"])
            action = agent_info.get("action", "summarize")
            if action == "tool":
                tool_name = agent_info.get("tool_name")
                args = agent_info.get("args", {})
                if self._count_same_tool_call(state, tool_name, args) >= self.max_same_call_repeats:
                    state["agent_info"] = json.dumps({"action": "summarize", "reason": "重复工具调用次数过多"}, ensure_ascii=False)
                    return "summarize"
            return action if action in ("tool", "summarize") else "summarize"
        except:
            return "summarize"
    
    def run(self, user_input: str) -> str:
        initial_state = {
            "user_input": user_input,
            "agent_info": "",
            "tool_results": [],
            "is_finished": False,
            "final_answer": "",
            "conversation_history": self.memory.get_conversation_history_copy(),
            "max_steps": self.max_tool_steps,
            "relevant_tool_names": [],
            "docs_content": "",
        }

        # 整轮只做一次 embedding 检索，结果缓存进 state 供循环内各节点复用
        search_query = self._build_search_query(initial_state)
        initial_state["relevant_tool_names"] = self.memory.search_tools(search_query, k=self.max_tools_in_prompt)
        relevant_docs = self.memory.search_docs(search_query, k=3)
        initial_state["docs_content"] = "\n\n相关文档内容：\n" + "\n\n---\n\n".join(relevant_docs)

        result = self.graph.invoke(initial_state)

        if result.get("final_answer"):
            self.memory.add_conversation(
                user_input=user_input,
                agent_response=result["final_answer"],
                tool_results=result["tool_results"],
                timestamp=time.time()
            )

        return result["final_answer"]

    def reset_conversation(self):
        self.memory.reset_conversation()

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

# def main():
#     print("=" * 50)
    
#     try:
#         # 创建 MemsAPI 实例
#         api = MemsAPI()
        
#         result = api.add_points_models_file()
        
#         # 解析并打印结果
#         result_data = json.loads(result)
        
#         if result_data.get("success"):
#             print(f"  响应数据: {result}")
#         else:
#             print(f"  错误信息: {result_data.get('message', '未知错误')}")
            
#     except Exception as e:
#         print(f"✗ 测试失败: {str(e)}")
#         import traceback
#         traceback.print_exc()
    
#     print("\n" + "=" * 50)

if __name__ == "__main__":
    main()