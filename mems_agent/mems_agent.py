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
from prompts import build_agent_system_prompt, build_agent_user_message, build_summarize_system_prompt, build_summarize_user_message, build_plan_system_prompt, build_plan_user_message


class MemsAgent:
    def __init__(self, api_key: str = None, base_url: str = None):
        llm_config = get_llm_config()
        self.mems_api = MemsAPI(base_url=base_url)
        self.client = OpenAI(
            api_key=api_key or llm_config.get("api_key"),
            base_url=llm_config.get("base_url", "https://yunwu.ai/v1")
        )
        self.model = llm_config.get("model", "gpt-5.4")
        self.max_tool_steps = 15
        self.max_same_call_repeats = 1
        self.max_tools_in_prompt = 25
        self.max_tool_results_in_prompt = 30  # P0-1: 从10提升至30，避免早期结果被省略
        self.max_tool_result_chars = 4000  # P0-1: 从1500提升至4000，减少关键数据截断
        # summarize 完成度校验最多强制返工的次数，避免子任务无法推进时死循环
        self.max_completion_retries = 2
        # 每个子任务单独检索的工具数量，最终与其他子任务结果合并去重
        self.tools_per_subtask = 12  # P0-3: 从8提升至12，提高跨模块任务召回率
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

        workflow.add_node("plan", self._plan_node)
        workflow.add_node("agent", self._agent_node)
        workflow.add_node("tool", self._tool_node)
        workflow.add_node("summarize", self._summarize_node)

        workflow.set_entry_point("plan")
        workflow.add_edge("plan", "agent")
        workflow.add_edge("tool", "agent")
        workflow.add_edge("summarize", END)

        workflow.add_conditional_edges(
            "agent",
            self._decide_next_step,
            {
                "tool": "tool",
                "agent": "agent",
                "summarize": "summarize"
            }
        )

        return workflow.compile()

    def _plan_node(self, state: AgentState) -> AgentState:
        system_prompt = build_plan_system_prompt()
        user_message = build_plan_user_message(user_input=state["user_input"])
        response = self._call_llm(system_prompt, user_message=user_message)
        try:
            plan = json.loads(response)
            subtasks = plan.get("subtasks", []) if isinstance(plan, dict) else []
        except json.JSONDecodeError:
            subtasks = []
        # 兜底：规划失败时退化为单一子任务，保持后续逻辑一致
        if not subtasks:
            subtasks = [state["user_input"]]
        state["subtasks"] = subtasks

        # P0-2: 初始化子任务状态追踪
        state["subtask_status"] = {task: "pending" for task in subtasks}

        # P0-3: 按子任务分别检索工具并与整轮检索结果合并去重
        # 关键改进：先对整体用户输入做一次检索，确保基础工具不遗漏
        merged = list(state.get("relevant_tool_names") or [])
        seen = set(merged)
        
        # 先检索整体输入（覆盖通用工具）
        for name in self.memory.search_tools(state["user_input"], k=self.tools_per_subtask):
            if name not in seen:
                seen.add(name)
                merged.append(name)
        
        # 再对每个子任务单独检索（覆盖专项工具）
        if len(subtasks) > 1:
            for task in subtasks:
                for name in self.memory.search_tools(task, k=self.tools_per_subtask):
                    if name not in seen:
                        seen.add(name)
                        merged.append(name)

        # P0-3: 关键字兜底匹配 - 向量检索对短中文 query 召回英文工具名不稳定，
        # 这里把工具名按下划线拆词，只要任一词出现在用户输入/子任务中就强制纳入，
        # 确保 add_pscpu_reset 这类被明确点名的工具不会因检索波动而漏召回。
        full_text = (state["user_input"] + " " + " ".join(subtasks)).lower()
        keyword_hits = []
        for tool in self.tools:
            if tool.name in seen:
                continue
            tokens = [t for t in tool.name.lower().split("_") if len(t) >= 3 and t not in ("add", "get", "del", "set", "list", "the", "all", "api")]
            if any(token in full_text for token in tokens):
                seen.add(tool.name)
                merged.append(tool.name)
                keyword_hits.append(tool.name)

        state["relevant_tool_names"] = merged
        # print(f"[工具检索] 为 {len(subtasks)} 个子任务检索到 {len(merged)} 个工具（总工具数 {len(self.tools)}）")
        # print(f"[工具检索] 子任务清单: {subtasks}")
        # if keyword_hits:
        #     print(f"[工具检索] 关键字兜底补充的工具: {keyword_hits}")
        # print(f"[工具检索] 检索到的工具列表（共{len(merged)}个）:")
        # for i, name in enumerate(merged, start=1):
        #     print(f"  {i}. {name}")
        return state

    def _format_subtasks(self, subtasks: List[str], subtask_status: Dict[str, str] = None) -> str:
        """P0-2: 格式化子任务清单，包含状态标记"""
        if not subtasks:
            return ""
        if not subtask_status:
            return "\n".join(f"{i}. {task}" for i, task in enumerate(subtasks, start=1))
        
        # 带状态标记的格式
        lines = []
        status_icons = {
            "pending": "⏳ 待执行",
            "in_progress": "🔄 进行中",
            "completed": "✅ 已完成",
            "failed": "❌ 失败"
        }
        for i, task in enumerate(subtasks, start=1):
            status = subtask_status.get(task, "pending")
            icon = status_icons.get(status, "⏳ 待执行")
            lines.append(f"{i}. [{icon}] {task}")
        return "\n".join(lines)

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

        subtasks = state.get("subtasks") or []
        subtask_status = state.get("subtask_status") or {}
        subtasks_str = ""
        if subtasks:
            # P0-2: 展示带状态标记的子任务清单
            subtasks_str = "子任务清单（必须全部完成，未完成项需继续推进）：\n" + self._format_subtasks(subtasks, subtask_status) + "\n"
            feedback = state.get("completion_feedback") or []
            if feedback:
                subtasks_str += "\n⚠️ 以下子任务经校验仍未完成，请优先继续推进，不要输出 summarize：\n" + self._format_subtasks(feedback, subtask_status) + "\n"

        system_prompt = build_agent_system_prompt(tools_info=tools_info)
        user_message = build_agent_user_message(
            conversation_history_str=conversation_history_str,
            user_input=state["user_input"],
            tool_results=self._format_tool_results(state["tool_results"]),
            docs_content=docs_content,
            subtasks_str=subtasks_str,
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

            # P0-3: 改进重复调用检测逻辑 - 区分"失败重试"和"恶意循环"
            same_call_count = self._count_same_tool_call(state, tool_name, args)
            if same_call_count >= self.max_same_call_repeats:
                # 检查上一次调用是否失败，失败则允许重试
                last_result = None
                for result in reversed(state.get("tool_results", [])):
                    if result.get("tool_name") == tool_name:
                        last_result = result.get("result", "")
                        break
                
                is_last_failed = False
                if last_result:
                    try:
                        parsed = json.loads(last_result)
                        is_last_failed = not parsed.get("success", True)
                    except:
                        pass
                
                if not is_last_failed:
                    loop_msg = json.dumps({"success": False, "message": f"检测到重复调用工具 {tool_name} 且参数相同（已调用{same_call_count}次），已自动停止继续调用以避免死循环"}, ensure_ascii=False)
                    print(f"[工具调用] 输出结果: {loop_msg}")
                    state["tool_results"].append({
                        "tool_name": tool_name,
                        "args": args,
                        "result": loop_msg,
                        "timestamp": time.time()
                    })
                    state["agent_info"] = json.dumps({"action": "summarize", "reason": "重复工具调用触发保护"}, ensure_ascii=False)
                    return state
                else:
                    print(f"[工具调用] 检测到重复调用，但上次失败，允许重试")

            
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
                
                # P0-2: 更新子任务状态（根据工具调用结果推断）
                self._update_subtask_status_after_tool(state, tool_name, result)
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
    
    def _check_subtasks_completion(self, state: AgentState) -> List[str]:
        """基于已执行的工具调用结果，判断哪些子任务仍未完成，返回未完成子任务描述列表。
        无子任务或仅1项时不做校验（视为无遗漏风险）。"""
        subtasks = state.get("subtasks") or []
        if len(subtasks) <= 1:
            return []

        check_system = (
            "你是任务完成度审查员。根据子任务清单和已执行的工具调用结果，"
            "判断每个子任务是否已经被执行/完成。"
            "纯文档类、无需工具的子任务若信息已具备则视为已完成。"
            '只输出JSON：{"unfinished": [未完成子任务的原文描述, ...]}，全部完成则 unfinished 为空数组。'
        )
        check_user = (
            "子任务清单：\n" + self._format_subtasks(subtasks) +
            "\n\n已执行的工具调用结果：\n" + self._format_tool_results(state["tool_results"], max_results=self.max_tool_steps)
        )
        response = self._call_llm(check_system, user_message=check_user)
        parsed = self._parse_agent_response(response)
        unfinished = parsed.get("unfinished", []) if isinstance(parsed, dict) else []
        # 仅保留确实存在于清单中的项，避免模型臆造
        unfinished = [task for task in subtasks if task in unfinished]
        # P0-2: 同步更新子任务状态，未在未完成列表且非失败的视为已完成
        status = state.get("subtask_status") or {}
        for task in subtasks:
            if task not in unfinished and status.get(task) != "failed":
                status[task] = "completed"
        state["subtask_status"] = status
        return unfinished

    def _update_subtask_status_after_tool(self, state: AgentState, tool_name: str, result: str) -> None:
        """P0-2: 工具调用后由 LLM 推断当前推进的子任务并更新其状态。
        失败结果标记 failed，成功标记 completed，避免靠关键字硬匹配带来的误判。"""
        subtasks = state.get("subtasks") or []
        if len(subtasks) <= 1:
            return

        # 判断本次工具调用是否成功
        is_success = True
        try:
            parsed = json.loads(result)
            is_success = parsed.get("success", True)
        except Exception:
            pass

        status = state.get("subtask_status") or {}
        pending = [t for t in subtasks if status.get(t) != "completed"]
        if not pending:
            return

        # 用 LLM 将本次工具调用归属到某个待办子任务
        match_system = (
            "你是任务匹配器。给定子任务清单和刚刚执行的一次工具调用，"
            "判断这次工具调用对应清单中的哪一个子任务（返回其完整原文描述）。"
            '只输出JSON：{"matched": "对应的子任务原文描述，无法匹配则为空字符串"}'
        )
        match_user = (
            "待办子任务：\n" + self._format_subtasks(pending) +
            f"\n\n刚执行的工具调用：{tool_name}\n调用结果：{str(result)[:self.max_tool_result_chars]}"
        )
        response = self._call_llm(match_system, user_message=match_user)
        parsed = self._parse_agent_response(response)
        matched = parsed.get("matched", "") if isinstance(parsed, dict) else ""

        if matched in subtasks:
            status[matched] = "completed" if is_success else "failed"
            print(f"[子任务状态] '{matched}' -> {status[matched]}")
        state["subtask_status"] = status

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
                # P0-3: 仅当达到重复上限且上次调用成功时才强制 summarize，
                # 上次失败的调用允许重试（与 _tool_node 中逻辑保持一致）
                if self._count_same_tool_call(state, tool_name, args) >= self.max_same_call_repeats:
                    last_result = None
                    for result in reversed(state.get("tool_results", [])):
                        if result.get("tool_name") == tool_name:
                            last_result = result.get("result", "")
                            break
                    last_failed = False
                    if last_result:
                        try:
                            last_failed = not json.loads(last_result).get("success", True)
                        except Exception:
                            pass
                    if not last_failed:
                        state["agent_info"] = json.dumps({"action": "summarize", "reason": "重复工具调用次数过多"}, ensure_ascii=False)
                        return "summarize"
                # 已开始推进，清除上一轮的未完成反馈，避免在后续 prompt 中残留
                state["completion_feedback"] = []
                return "tool"

            if action == "summarize":
                # summarize 前校验子任务完成度，存在遗漏则强制返工（问题2）
                if state.get("completion_retries", 0) < self.max_completion_retries:
                    unfinished = self._check_subtasks_completion(state)
                    if unfinished:
                        state["completion_retries"] = state.get("completion_retries", 0) + 1
                        state["completion_feedback"] = unfinished
                        print(f"[完成度校验] 检测到未完成子任务，强制返工: {unfinished}")
                        # 回到 agent 节点继续推进未完成项，而非直接进入 tool
                        return "agent"
                state["completion_feedback"] = []
                return "summarize"

            return "summarize"
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
            "subtasks": [],
            "subtask_status": {},
            "completion_retries": 0,
            "completion_feedback": [],
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