# LangChain Academy 课程章节地图

课程：[Introduction to LangGraph - Python](https://academy.langchain.com/courses/intro-to-langgraph)。官方页列为免费、55 lessons、约 6 小时视频；本地仓库将材料按 Module 0–6 组织。下面按目录与现有 notebook 列出可核对内容，不代表视频已观看或所有线上练习均已离线保存。

| 模块 | 课程页目录 | 仓库中的主要 notebook 与可见练习 |
|---|---|---|
| 0：准备 | Getting Set Up、Video Guide、Resources、Course Transcripts | basics.ipynb：chat model、message、调用模型、Tavily 搜索；README 说明 Python/Jupyter、环境变量和 API key。 |
| 1：Introduction | Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment | simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。 |
| 2：State and Memory | State Schema、State Reducers、Multiple Schemas、Trim and Filter Messages、摘要与 Memory、External Memory | state-schema.ipynb 展示 TypedDict/dataclass/Pydantic；state-reducers.ipynb 讲覆盖、追加、自定义 reducer 与 message 删除；chatbot-summarization.ipynb 在超过六条消息后滚动总结；chatbot-external-memory.ipynb 用 SqliteSaver 持久化。 |
| 3：UX and Human-in-the-Loop | Streaming、Breakpoints、Editing State and Human Feedback、Dynamic Breakpoints、Time Travel | breakpoints.ipynb 在 tools 节点执行前停下等待批准；edit-state-human-feedback.ipynb 展示编辑 state 和等待输入；time-travel.ipynb 演示历史查看、重放与 fork。 |
| 4：Building Your Assistant | Parallelization、Sub-graphs、Map-reduce、Research Assistant | map-reduce.ipynb 并行生成笑话后归并挑选；research-assistant.ipynb 让人工修订 analyst 人设，再并行访谈/检索并生成报告。 |
| 5：Long-Term Memory | Short vs. Long-Term Memory、LangGraph Store、Profile、Collection、Long-Term Memory Agent | memory_store.ipynb 区分 thread checkpoint 与跨会话 Store；profile/collection notebook 用 schema 管理资料；Trustcall 示例通过 JSON Patch 更新已有用户偏好。 |
| 6：Deployment | Deployment Concepts、Creating/Connecting to Deployment、Double Texting、Assistants | creating.ipynb 使用 CLI/Docker 并配置 Redis/PostgreSQL；connecting.ipynb 展示 run/thread/stream、历史与 Store；double-texting.ipynb 比较 reject/enqueue/interrupt/rollback；assistant.ipynb 区分个人与工作待办助手。 |

章节次序体现从单图到服务部署的递进，但完整课堂视频和平台内练习与仓库 notebook 并非同一份材料。模块中的 Studio 说明还包含录制版与当前工具名称/部署方式的差异提示。

主要源码入口：仓库 README（原本地资料引用，未随公开版收录）、Agent memory（原本地资料引用，未随公开版收录）、SQLite 外部记忆（原本地资料引用，未随公开版收录）、人工批准（原本地资料引用，未随公开版收录）、Research Assistant（原本地资料引用，未随公开版收录）、跨会话记忆（原本地资料引用，未随公开版收录）、部署拓扑（原本地资料引用，未随公开版收录）、并发输入策略（原本地资料引用，未随公开版收录）。
