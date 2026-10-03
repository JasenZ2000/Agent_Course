# LangChain Academy：Introduction to LangGraph 分析

研究日期：2026-10-03（Asia/Shanghai）  
范围：官方课程目录与 README、仓库快照中的 notebook 和 Studio 示例。仅静态阅读；未逐个播放课程视频、运行 notebook、连接模型 API 或部署应用。详细获取边界见 [evidence.md](evidence.md)，章节地图见 [curriculum.md](curriculum.md)。

## 结论

这门课适合会写 Python、想把 Agent 从“模型加工具”推进到有状态工作流的开发者。它围绕一份图状态和一组节点逐步搭建：先画最小图，再接模型与工具，随后增加对话持久化、人工介入、并行与子图、跨会话记忆，最后进入服务部署和并发输入处理。课程最有用的教学特点是同一套图模型从入门例子一直延伸到部署案例，学生能沿着源码看到节点、状态和执行控制如何逐步变复杂。

它不是零编程基础或 Agent 概念史课程。课程核心价值是 LangGraph 的操作模型与应用工程：State、Node、Edge、Reducer、Checkpoint、Thread、Store、Interrupt 和 Run。框架概念解释通常紧接 notebook 示例；对于“为什么用图、如何暂停后编辑状态、如何处理同一 thread 的并发请求”等具体问题，公开代码比课程宣传页更有信息量。

## 学习顺序与实际例子

Module 1 从三节点图、固定 Chain、条件 Router 进入带工具的 Agent。最小图用 TypedDict 保存一个值，由节点函数读取并写回，再用条件边决定下一节点；Chain 示例接上 chat model、messages 与 multiply 工具；Agent 示例用 ToolNode 和 tools_condition，在模型提出工具调用时执行并把 ToolMessage 回传。这个顺序把“固定步骤”与“模型决定是否调用工具”放进同一个可观察图里。

Module 2 与 Module 3 解决状态的生命周期和人为控制。消息默认需要 reducer 追加而非覆盖；聊天过长时示例先生成滚动摘要，再用 RemoveMessage 收缩历史。短期记忆先用 MemorySaver 和 thread_id 说明 checkpoint；随后 chatbot-external-memory.ipynb 改用 SqliteSaver，将状态写进 state_db/example.db，并展示重启 notebook kernel 后按 thread_id 读回记录。人工审核例子在 tools 节点之前中断图，查看待执行的工具调用，批准后继续；其它章节展示动态中断、编辑 state、流式响应和从旧 checkpoint 回放或 fork。

Module 4 用并行节点、子图和 map-reduce 扩大工作流。小练习把多个 joke 生成结果汇总后选一个；Research Assistant 则先生成研究者角色，人工可以要求补充“创业公司视角”，再并行采访与检索，最后聚合访谈写报告。它把“人参与修正任务定义”与“图并行执行”串到同一个例子中，是整套源码里最清晰的综合练习。

Module 5 把同一 thread 内的 checkpoint 和跨 thread 的长期 Store 分开教。用户画像/偏好被按 schema 写入命名空间；复杂结构化抽取可能失败，Trustcall 章节改用工具调用和 JSON Patch 更新现有资料，避免每次重写整个 profile。Module 6 把名为 task_maistro 的待办助手打成 LangGraph Server：Docker 部署示例配置 Redis 与 PostgreSQL；SDK 章节展示 run/thread、stream、thread fork、checkpoint 查询与跨会话 Store。double-texting notebook 比较 reject、enqueue、interrupt、rollback 四种同一 thread 收到新输入时的处理方式。

## 静态学习体验与边界

学习材料是目录页、视频和 notebook 的组合。仓库 notebook 常按“复习—目标—概念—代码—查看结果/trace”组织，代码旁边有短解释，适合边读边改；README 给出 Python 3.11–3.13、虚拟环境、Jupyter 与环境变量步骤。建立实际环境仍需要模型 API key；LangSmith tracing 和 Module 4 的 Tavily 搜索需要各自账号/凭证。课程页虽标为免费，外部 API 是否免费取决于对应服务和账户，不应把“课程免费”理解成“所有实验零成本”。

术语链条覆盖较完整：图状态如何声明、节点如何返回部分状态、边如何路由、Reducer 如何合并消息、Checkpoint 如何按 thread 保存、Store 如何跨 thread 取资料，都配有可定位源码。课程也有实现边界：SQLite 例子是本地单连接的持久化演示，没有压测、连接池或容量比较；后续部署样例用 Postgres/Redis 和 Server 来展示服务拓扑，但没有完整容量规划、SLO、故障恢复演练或生产权限审计。工具批准以图中断和人工反馈为主，没有系统讨论最小权限、写操作分级、幂等或补偿事务。

另一个阅读成本来自版本迁移：若干 notebook 明确说明录制时使用的 Studio 桌面应用已过时，建议改用本地 LangSmith Studio；这类维护注记对代码复现有帮助，也提醒学习者按当前文档修正安装方式。仓库依赖中有一部分版本只给下限或未固定，实际复跑要记录安装时的包版本。这里是对源码和教学设计的静态判断，不代表已经跑通外部服务或验证当前 API 兼容性。

## 对本轮研究的用途

本课程可作为“把工具调用放进有状态、可暂停、可恢复的图”的原始证据。适合从简单 Router 讲到人工批准，再用 Research Assistant 展示并行编排；若需要 SQLite 后续如何转入服务型部署，可对照 Module 2 与 Module 6。口播与跨课程/面经定位请以资料库总览为准；本文只总结该课程自身材料，不替用户写视频文案。
