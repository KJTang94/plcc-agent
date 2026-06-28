# PLCC MEMS Agent

一个面向 MEMS / PLCC 系统的 AI Agent 助手。项目把大模型、OpenAPI 接口描述、MEMS REST API、会话记忆和一个轻量 Web 控制台组合起来，让用户可以用自然语言查询、配置、导入和控制 MEMS 相关资源。

## 功能概览

- **自然语言操作 MEMS API**：用户输入任务后，Agent 会先规划子任务，再选择合适的 MEMS API 工具并执行。
- **OpenAPI 驱动的工具体系**：基于 `mems_agent/openapi_mems.json` 解析接口，生成工具描述、参数结构和 API 文档，可覆盖告警、AOE、测点、设备、LCC、PSCPU、流程、脚本、插件、标签等模块。
- **执行前确认机制**：Web 控制台模式下，涉及生成参数、默认参数或文件参数的 API 调用会先弹出确认框，用户确认后才执行。
- **文件上传与导入支持**：支持通过前端上传 Excel 等文件，也支持从 `excel_paths.json` 和 `config_files/` 中读取默认配置文件，调用模型导入类接口。
- **会话记忆与 RAG 检索**：通过 LangChain、FAISS 和 OpenAI Embeddings 检索历史对话、API 文档和工具描述，帮助 Agent 延续上下文并选择更准确的接口。
- **可视化执行轨迹**：前端展示任务规划、API 调用列表、调用参数、返回结果和原始 JSON，便于调试与追踪。
- **CLI 与 Web 双入口**：既可以在命令行中对话，也可以启动本地 Web 控制台使用。

## 技术栈

- Python 3.10+
- OpenAI Python SDK
- LangGraph
- LangChain / FAISS
- Requests
- Pydantic
- 原生 `http.server` Web 后端
- 原生 HTML / CSS / JavaScript 前端

## 目录结构

```text
.
+-- requirements.txt
+-- README.md
+-- mems_agent/
    +-- web_app.py                 # Web 服务入口，提供静态页面和 /api/chat 等接口
    +-- mems_agent.py              # Agent 主流程：规划、工具选择、确认、执行、总结
    +-- mems_api.py                # MEMS REST API 封装
    +-- mems_tools.py              # 将 MEMS API 转换为 LLM 可调用工具
    +-- openapi_shared.py          # OpenAPI 解析、参数提取、工具描述生成
    +-- generate_from_openapi.py   # 根据 OpenAPI 更新 API 封装和文档
    +-- memory.py                  # 会话记忆、工具检索、API 文档检索
    +-- prompts.py                 # Agent 规划、执行、总结提示词
    +-- config.py                  # 配置加载和 Excel 路径解析
    +-- openapi_mems.json          # MEMS OpenAPI 描述
    +-- mems_api_docs.md           # 生成后的 MEMS API 文档
    +-- excel_paths.json           # 默认 Excel 配置文件路径
    +-- config_files/              # 示例/默认 Excel 配置文件
    +-- web/
        +-- index.html
        +-- app.js
        +-- styles.css
```

## 安装

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Linux / macOS 激活虚拟环境：

```bash
source .venv/bin/activate
```

## 配置

项目需要在 `mems_agent/` 目录下创建 `config.json`。该文件包含密钥和登录信息，已被 `.gitignore` 忽略。

示例：

```json
{
  "llm": {
    "api_key": "your-llm-api-key",
    "base_url": "https://yunwu.ai/v1",
    "model": "gpt-5.4"
  },
  "mems_api": {
    "base_url": "http://localhost:80/api/v1",
    "username": "admin",
    "password": "your-password",
    "secret_key": "your-secret-key"
  }
}
```

也可以通过环境变量覆盖配置：

| 配置项 | 环境变量 |
| --- | --- |
| `llm.api_key` | `LLM_API_KEY` |
| `llm.base_url` | `LLM_BASE_URL` |
| `llm.model` | `LLM_MODEL` |
| `mems_api.base_url` | `MEMS_API_BASE_URL` |
| `mems_api.username` | `MEMS_API_USERNAME` |
| `mems_api.password` | `MEMS_API_PASSWORD` |
| `mems_api.secret_key` | `MEMS_API_SECRET_KEY` |

Excel 导入类接口默认从 `mems_agent/excel_paths.json` 读取文件路径。如果对应路径不存在，会回退到 `mems_agent/config_files/` 下的约定文件。

## 启动 Web 控制台

```bash
python -m mems_agent.web_app
```

默认访问地址：

```text
http://127.0.0.1:7860
```

可通过环境变量修改监听地址和端口：

```bash
set MEMS_AGENT_HOST=0.0.0.0
set MEMS_AGENT_PORT=7860
python -m mems_agent.web_app
```

Web 控制台提供：

- 聊天输入和附件上传
- 会话 ID 管理与重置
- 子任务规划视图
- API 调用轨迹视图
- 原始 JSON 响应视图
- API 参数确认弹窗

## 使用命令行入口

```bash
python mems_agent/mems_agent.py
```

命令行支持：

- 输入自然语言任务与 Agent 交互
- 输入 `reset` 重置当前会话历史
- 输入 `exit` 退出

## Web API

`web_app.py` 暴露以下本地接口：

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| `GET` | `/api/health` | 健康检查 |
| `POST` | `/api/chat` | 发送用户消息和附件，返回回答或待确认 API 调用 |
| `POST` | `/api/confirm` | 提交确认后的 API 参数并继续执行 |
| `POST` | `/api/reset` | 重置指定会话记忆 |

`/api/chat` 使用 `multipart/form-data`，主要字段：

- `message`：用户输入
- `session_id`：会话 ID
- `files`：可选附件，可多文件

## Agent 执行流程

1. 读取用户输入和附件信息。
2. 构建会话记忆、历史上下文、API 文档片段和候选工具列表。
3. 使用 LLM 将任务拆分成子任务。
4. 根据子任务检索相关 MEMS API 工具。
5. 使用 function calling 生成工具调用。
6. 如果需要确认，返回 `awaiting_confirmation` 状态给前端。
7. 用户确认参数后执行 MEMS API。
8. 记录工具结果、更新子任务状态。
9. 汇总 API 返回内容，生成最终回答。
10. 保存会话记忆，供后续对话检索。

## OpenAPI 维护

MEMS API 的工具、文档和部分封装逻辑由 `openapi_mems.json` 驱动。

当 OpenAPI 文件变更后，可运行：

```bash
python mems_agent/generate_from_openapi.py
```

脚本会尝试更新：

- `mems_agent/mems_api.py`
- `mems_agent/mems_api_docs.md`

注意：当前项目中部分文件包含手写增强逻辑，例如文件上传、默认 Excel 路径、PSCPU 启动参数等。重新生成后请检查这些定制逻辑是否仍然保留。

## 运行数据

运行过程中会生成以下本地数据：

- `mems_agent/.memory/`：按会话保存的对话历史和结构化记忆
- `mems_agent/.faiss_cache/`：API 文档和工具索引缓存
- `mems_agent/uploads/`：Web 前端上传的附件

这些目录已被 `.gitignore` 忽略。

## 常见问题

### 启动后首次请求较慢

首次使用时会初始化 Embeddings、构建 FAISS 索引和工具索引，耗时会比后续请求长。索引缓存生成后会复用。

### Agent 无法登录 MEMS

检查 `config.json` 或环境变量中的以下配置：

- `mems_api.base_url`
- `mems_api.username`
- `mems_api.password`
- `mems_api.secret_key`

项目登录时会使用 `secret_key` 对密码做 HMAC-SHA256，再发送到 `/auth/login`。

### 文件导入接口找不到文件

检查 `mems_agent/excel_paths.json` 中配置的路径是否存在。相对路径会基于 `mems_agent/` 目录解析。

### 中文显示异常

请确保终端、编辑器和源码文件都使用 UTF-8。当前项目部分历史注释或字符串可能存在编码异常，不影响 README 的 UTF-8 编码。

## 开发建议

- 修改 MEMS API 描述时，优先更新 `openapi_mems.json`，再运行生成脚本。
- 修改 Agent 行为时，重点关注 `mems_agent.py`、`prompts.py` 和 `memory.py`。
- 修改前端交互时，重点关注 `web/index.html`、`web/app.js` 和 `web/styles.css`。
- 涉及真实设备控制或配置写入的接口，建议保留执行前确认流程。
