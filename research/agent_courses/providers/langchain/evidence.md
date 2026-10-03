# LangChain Academy 获取范围与证据

研究日期：2026-10-03。此档案只说明本地研究材料与判断依据。

| 材料 | 已保存内容 | 范围与限制 |
|---|---|---|
| 官方课程页 | [课程页](https://academy.langchain.com/courses/intro-to-langgraph)；原始 HTML 与提取文本在 source/web/raw 和 source/web/text | full_body 文本保存了目录、FAQ、免费标注、55 lessons 与 6 小时视频信息；另一条 collector 记录仅提取到 15 字符并标 needs_review，故课程目录以 full_body 归档为据。未登录课程、未看视频、未获取平台账号后的完整互动内容。 |
| 官方 GitHub 仓库 | [课程仓库](https://github.com/langchain-ai/langchain-academy/tree/fa15bec4a51c541c40c261586b037c9d134977b1)；本地 source/langchain-academy | 已有 commit fa15bec4a51c541c40c261586b037c9d134977b1 的浅克隆（is-shallow-repository 为 true）；README、模块 0–6 notebook、Studio 示例、依赖清单、示例 SQLite DB 可静态查看。浅克隆不含完整 Git 历史；此报告不声称全部视频或全部网页教学已保存。 |
| 课程/代码许可 | 仓库 LICENSE 与 README | 原始许可证保留在 source 中；本地保存供课程研究，不代表可以重新发布完整教材。 |

## 可复核的具体证据

- 目录与时长：source/web/text/academy_intro_to_langgraph_full_body.txt；模块清单亦可在本地仓库 README 开头复核。
- Agent tool loop：module-1/chain.ipynb、module-1/router.ipynb、module-1/agent.ipynb；multiply 工具和 ToolNode/tools_condition 代码可见。
- 状态与 SQLite：module-2/chatbot-external-memory.ipynb；标题“Sqlite”下安装 langgraph-checkpoint-sqlite，先连内存库，再打开 state_db/example.db 并用 SqliteSaver 保存 checkpoint；module-2/state_db/example.db 已随仓库存在。
- 人工检查：module-3/breakpoints.ipynb；明确以 interrupt_before=["tools"] 暂停并在确认后继续；module-4/research-assistant.ipynb 有修改 analyst 视角的人工反馈。
- 长期记忆：module-5/memoryschema_profile.ipynb 描述复杂 schema 提取与 JSON Patch 更新；module-5/memory_store.ipynb 保存 thread_id/user_id 示例。
- 服务侧拓扑：module-6/creating.ipynb 描述 Docker、Redis 和 PostgreSQL；module-6/connecting.ipynb 把 run 存入 PostgreSQL、流式消息经 Redis；module-6/double-texting.ipynb 比较并发输入策略。
- 环境要求：README 与 requirements.txt；README 要求 Python 3.11、3.12 或 3.13，并说明 OpenAI、LangSmith 与 Module 4 的 Tavily 凭证设置。

获取过程沿用仓库已有目标与源文件，没有重复下载已成功仓库。上述 notebook 和代码仅静态阅读，未运行或执行外部工具调用。
