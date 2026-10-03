# 逐课程、逐知识点证据

此表定位到本仓库已有研究记录与官方入口。摘录是研究者的归纳，不冒充官方逐字引文。层级为当前证据支持的下限；需与原课核对后再升级。

## Datawhale《从零开始构建智能体》

[官网](https://github.com/datawhalechina/hello-agents) · [课程笔记](../courses/datawhale_hello_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)：研究基准：Datawhale 仓库固定提交 [`4b014ad47e2658af24b59f21e7bdb3f89a66205e`](https://github.com/datawhalechina/hello-agents/tree/4b014ad47e2658af24b59f21e7bdb3f89a66205e)。这里按仓库的中文主目录逐章盘点，阅读的是教材与代码文件，不包含视频实看或运行验收。课程判断和限定见 [analysis.md](analysis.md)，来源边界见 [evidence.md](evidence.md)。 |
| K02 LLM、消息、Token与模型选择 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  二、构建 LLM Agent  /  4–7  /  手写范式、使用低代码产品、比较框架、搭建自己的 Agent 基类和工具系统  /  能比较不同实现形态，并理解框架替自己封装了哪些部分  /  |
| K03 提示、指令与Prompt Patterns | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  3 大语言模型基础  /  N-gram/RNN 到 Transformer、Decoder-only、prompt、token/BPE、模型选择、缩放法则与幻觉  /  正文 + N-gram、词向量、BPE、Transformer、Qwen 脚本  /  兼有手写简化算法与调用开源模型；Attention 的 Query 是 Q/K/V 术语  /  |
| K05 Agent loop、ReAct与停止条件 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  1 初识智能体  /  Agent 是什么；环境、状态、观察、工具、行动循环；Agent 与 Workflow 的差异  /  正文 + `FirstAgentTest.py`/Notebook；天气查询后再找景点的两步任务  /  “5 分钟”是案例标题/引导，实际要配好模型、天气与搜索服务  /  |
| K06 工具定义、发现与实际调用 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  二、构建 LLM Agent  /  4–7  /  手写范式、使用低代码产品、比较框架、搭建自己的 Agent 基类和工具系统  /  能比较不同实现形态，并理解框架替自己封装了哪些部分  /  |
| K07 结构化输出与参数校验 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  MCP/A2A/ANP  /  第十章代码目录（原本地资料引用，未随公开版收录）  /  MCP 发现/调用工具，A2A 联接 Agent，ANP 讨论动态发现  /  身份认证、schema 兼容、断连重试和规模验证在哪里  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)：读 1、3 章，再读 4.2 ReAct。先能解释“输入从哪里来、工具如何选择和执行、Observation 如何反馈、任务在哪里结束”。第 2 章可当背景阅读，不需要把发展史当成动手前置条件。 |
| K09 文件、代码执行与沙箱 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)：研究基准：Datawhale 仓库固定提交 [`4b014ad47e2658af24b59f21e7bdb3f89a66205e`](https://github.com/datawhalechina/hello-agents/tree/4b014ad47e2658af24b59f21e7bdb3f89a66205e)。这里按仓库的中文主目录逐章盘点，阅读的是教材与代码文件，不包含视频实看或运行验收。课程判断和限定见 [analysis.md](analysis.md)，来源边界见 [evidence.md](evidence.md)。 |
| K10 链式工作流、Query与意图路由 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  3 大语言模型基础  /  N-gram/RNN 到 Transformer、Decoder-only、prompt、token/BPE、模型选择、缩放法则与幻觉  /  正文 + N-gram、词向量、BPE、Transformer、Qwen 脚本  /  兼有手写简化算法与调用开源模型；Attention 的 Query 是 Q/K/V 术语  /  |
| K11 任务分解、规划与重规划 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  4 智能体经典范式  /  ReAct、Plan-and-Solve、Reflection；工具定义、提示格式、执行状态和步数边界  /  正文 + `llm_client.py`、`ReAct.py`、`Plan_and_solve.py`、`Reflection.py`、`tools.py`  /  是从概念进入 Agent loop 的最佳代码入口之一；搜索调用需要相应 API  /  |
| K12 反思、自检与修订 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  4 智能体经典范式  /  ReAct、Plan-and-Solve、Reflection；工具定义、提示格式、执行状态和步数边界  /  正文 + `llm_client.py`、`ReAct.py`、`Plan_and_solve.py`、`Reflection.py`、`tools.py`  /  是从概念进入 Agent loop 的最佳代码入口之一；搜索调用需要相应 API  /  |
| K13 图编排、节点、边与状态Schema | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  1 初识智能体  /  Agent 是什么；环境、状态、观察、工具、行动循环；Agent 与 Workflow 的差异  /  正文 + `FirstAgentTest.py`/Notebook；天气查询后再找景点的两步任务  /  “5 分钟”是案例标题/引导，实际要配好模型、天气与搜索服务  /  |
| K15 短期记忆与会话历史 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  8 记忆与检索  /  记忆类型、记忆管理、RAG 原理与检索策略、文档问答助手  /  11 个左右的分步脚本；有本地/云数据库配置示例  /  需要 HelloAgents 包和向量/图存储选项；SQLite 在此出现为文档/情景记忆存储之一  /  |
| K19 上下文选择、压缩、卸载与缓存 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  9 上下文工程  /  ContextBuilder 的 GSSC 管线、NoteTool、TerminalTool、跨天代码库维护  /  代码库维护助手、CSV/日志/代码样例、终端限制演示  /  组件主要通过外部包导入；相关性选择示例不等于完成了跨模型/真实长任务评测  /  |
| K20 文档加载、切分与摘要 | 3 | [记录](../research/agent_courses/providers/datawhale/analysis.md)： /  **长任务状态、checkpoint、危险命令、Memory**：[快手电商后端实习一面](https://www.nowcoder.com/feed/main/detail/78fc3b815b4a4b3bb27d642fb53da16b)（目录标记 A*，年份未完整）  /  第 7 章 `max_steps`；第 9 章 Note 和三日代码库维护；第 15 章 NPC 持久记忆。  /  跨进程 checkpoint、异常退出后恢复、摘要漂移、可回放轨迹和危险动作权限。  /  |
| K21 Embedding、向量库与索引 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  3 大语言模型基础  /  N-gram/RNN 到 Transformer、Decoder-only、prompt、token/BPE、模型选择、缩放法则与幻觉  /  正文 + N-gram、词向量、BPE、Transformer、Qwen 脚本  /  兼有手写简化算法与调用开源模型；Attention 的 Query 是 Q/K/V 术语  /  |
| K22 混合检索、BM25、RRF与重排 | 2 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  8 记忆与检索  /  记忆类型、记忆管理、RAG 原理与检索策略、文档问答助手  /  11 个左右的分步脚本；有本地/云数据库配置示例  /  需要 HelloAgents 包和向量/图存储选项；SQLite 在此出现为文档/情景记忆存储之一  /  |
| K23 Agentic RAG与检索工具 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  8 记忆与检索  /  记忆类型、记忆管理、RAG 原理与检索策略、文档问答助手  /  11 个左右的分步脚本；有本地/云数据库配置示例  /  需要 HelloAgents 包和向量/图存储选项；SQLite 在此出现为文档/情景记忆存储之一  /  |
| K24 多Agent角色、分工与通信 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  6 框架开发实践  /  AutoGen、AgentScope、CAMEL、LangGraph 的设计差异和项目  /  四套独立示例；AgentScope 游戏角色、AutoGen 软件团队、CAMEL 合作写书、LangGraph 对话系统  /  框架依赖不共用同一环境；LangGraph 的 state/node/edge/conditional edge 是意图路由话题的入口  /  |
| K25 Handoff、Agent-as-tool与委派 | 2 | [记录](../research/agent_courses/providers/datawhale/analysis.md)：13. **NPC 记忆与降本**：第 15 章给 NPC 工作记忆和 SQLite+Qdrant 情景记忆，同时把背景闲聊批量生成；`state_manager.py`（原本地资料引用，未随公开版收录） 可见后台周期更新和进程内状态缓存。 |
| K27 MCP客户端、服务器与原语 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  10 智能体通信协议  /  MCP 工具连接、A2A Agent 对话、ANP 服务发现/路由/负载均衡  /  35 个左右的客户端/服务端示例、配置、部分报告与协议材料  /  引入 Node.js、服务启动与网络配置；ANP 大规模网络部分更偏概念和设计题  /  |
| K28 A2A、ANP与跨Agent互操作 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  10 智能体通信协议  /  MCP 工具连接、A2A Agent 对话、ANP 服务发现/路由/负载均衡  /  35 个左右的客户端/服务端示例、配置、部分报告与协议材料  /  引入 Node.js、服务启动与网络配置；ANP 大规模网络部分更偏概念和设计题  /  |
| K29 框架抽象、手写框架与选型 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  二、构建 LLM Agent  /  4–7  /  手写范式、使用低代码产品、比较框架、搭建自己的 Agent 基类和工具系统  /  能比较不同实现形态，并理解框架替自己封装了哪些部分  /  |
| K49 低代码平台与流程搭建 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  二、构建 LLM Agent  /  4–7  /  手写范式、使用低代码产品、比较框架、搭建自己的 Agent 基类和工具系统  /  能比较不同实现形态，并理解框架替自己封装了哪些部分  /  |
| K31 评测数据集、实验与版本对照 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  9 上下文工程  /  ContextBuilder 的 GSSC 管线、NoteTool、TerminalTool、跨天代码库维护  /  代码库维护助手、CSV/日志/代码样例、终端限制演示  /  组件主要通过外部包导入；相关性选择示例不等于完成了跨模型/真实长任务评测  /  |
| K32 指标、Judge与任务基准 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  12 智能体性能评估  /  BFCL/GAIA、工具调用与任务评估、数据生成、LLM Judge、胜率比较  /  评估脚本、结果格式、上游报告/score 样例  /  有可读评估流程；仓库已有输出属于上游样例，不是本次审阅者的复现结果  /  |
| K34 成本、延迟与模型优化 | 2 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  15 构建赛博小镇  /  NPC Agent、个性/记忆/好感度、批量背景对话、FastAPI、Godot 前端  /  Godot 项目 + Python 后端；记忆样例文件  /  展示成本优化和进程内状态，但不是多人/分布式规模证明；教材将 SQLite 与 Qdrant用于持久情景记忆  /  |
| K35 服务部署、UI/API集成与交付 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  13 智能旅行助手  /  前端/后端、数据校验、景点/天气/酒店 Agent、规划器、MCP 与地图服务  /  Vue 前端、FastAPI 后端、Agent 与服务层代码  /  适合看多个子任务的串联；网络/API 凭证和外部数据源是动手门槛  /  |
| K39 审计、动作凭据、幂等与回滚 | 1 | [记录](../research/agent_courses/providers/datawhale/analysis.md)： /  编排层与重构  /  第 6 章比较框架编排；第 7 章自研接口；第 13/14 章把任务拆成专门 Agent/服务；第 9 章有代码库维护和重构规划。  /  有从固定流程到图、多 Agent、任务计划的素材；没有直接示范把一个既有大项目的 orchestrator 分层迁移、保住公共 API、做灰度和回滚。面试若问“为什么重构编排层”，仍须用自己的项目证据回答。  /  |
| K41 Coding Agent与开发Harness | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  9 上下文工程  /  ContextBuilder 的 GSSC 管线、NoteTool、TerminalTool、跨天代码库维护  /  代码库维护助手、CSV/日志/代码样例、终端限制演示  /  组件主要通过外部包导入；相关性选择示例不等于完成了跨模型/真实长任务评测  /  |
| K44 端到端应用与综合项目 | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  五、毕业设计  /  16  /  自选项目、整理实现、测试、文档和贡献  /  以可读仓库和 PR 形式整理成果；实际选题与验收由学习者/社区承担  /  |
| K45 SFT、LoRA与Agentic RL | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  11 Agentic-RL  /  数据集、奖励函数、LoRA、SFT、GRPO、完整训练和分布式训练流程  /  训练脚本、config、DeepSpeed/多卡配置  /  是高级分支，涉及模型、数据、硬件和费用；不应与 Agent 应用 Demo 的基础完成度混为一谈  /  |
| K46 研究论文、能力基准与研究方法 | 2 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)：研究基准：Datawhale 仓库固定提交 [`4b014ad47e2658af24b59f21e7bdb3f89a66205e`](https://github.com/datawhalechina/hello-agents/tree/4b014ad47e2658af24b59f21e7bdb3f89a66205e)。这里按仓库的中文主目录逐章盘点，阅读的是教材与代码文件，不包含视频实看或运行验收。课程判断和限定见 [analysis.md](analysis.md)，来源边界见 [evidence.md](evidence.md)。 |
| K47 游戏、具身与机器人Agent | 3 | [记录](../research/agent_courses/providers/datawhale/curriculum.md)： /  2 智能体发展史  /  符号主义、专家系统、ELIZA、心智社会、强化学习与 LLM Agent 的发展  /  正文 + `ELIZA.py`  /  是概念史和规则机器人示例，不是现代 Agent 运行时教程  /  |
## 吴恩达 Agentic AI

[官网](https://www.deeplearning.ai/courses/agentic-ai) · [课程笔记](../courses/deeplearning_ai_agentic_ai/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)：官方课程页：[Agentic AI](https://www.deeplearning.ai/courses/agentic-ai)。官方社区公开索引列出五个课程模块。下表按该模块索引整理，并用本地视频转录中的标题/内容补充；可见转录标题不保证与平台的每个 lesson 槽位一一对应。 |
| K06 工具定义、发现与实际调用 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  3  /  Tool use  /  What are tools?、Tool syntax、Creating a tool、Code execution、MCP。讲模型返回工具调用请求、参数 schema、工具执行后把结果回填；示例有当前时间、网页搜索、SQL 数据库、计算和 GitHub MCP Server。  /  |
| K07 结构化输出与参数校验 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  3  /  Tool use  /  What are tools?、Tool syntax、Creating a tool、Code execution、MCP。讲模型返回工具调用请求、参数 schema、工具执行后把结果回填；示例有当前时间、网页搜索、SQL 数据库、计算和 GitHub MCP Server。  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  2  /  Reflection Design Pattern  /  Reflection to improve outputs、Evaluating the impact of reflection、Using external feedback。对邮件/代码先生成，再批评并修订；通过执行代码取得异常信息，展示外部反馈为何比纯自评更有帮助。  /  |
| K09 文件、代码执行与沙箱 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)：本地保存 31 个视频转录文件及各自的标题、字数、SHA-256 与原 lesson URL，见 source/videos/transcript_manifest.json 和 source/videos/transcripts/。标题总索引见 [evidence.md](evidence.md)。课程站 lesson 页面正文未在这份归档中保存；这一章节地图是“社区目录加可读转录”的研究地图，不代表课程所有测验和练习均已获得。 |
| K10 链式工作流、Query与意图路由 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/analysis.md)：这门课的主线是开发方法而非某一个 Agent 框架：把任务拆成可以由模型、代码或工具完成的步骤，先做工作流原型，再通过反思、外部反馈和评测逐步改进，复杂任务再考虑多 Agent 协作。转录里反复出现“先定义每步解决什么问题，再看结果是否值得增加复杂度”的工程判断。它适合用来理解 Agentic Workflow 的动机、设计模式、工具接入和评测闭环。 |
| K11 任务分解、规划与重规划 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  1  /  Introduction to Agentic Workflows  /  Welcome、What is agentic AI?、Degrees of autonomy、Benefits、Applications、Why not just direct generation?、Task decomposition、Planning workflows、Creating and executing LLM plans、Planning with code execution、Evaluating agentic AI。Research Agent 由直接写作演变为提纲、搜索、草稿、编辑和重写；另举订单邮件、发票和电子表格分析。  /  |
| K12 反思、自检与修订 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  2  /  Reflection Design Pattern  /  Reflection to improve outputs、Evaluating the impact of reflection、Using external feedback。对邮件/代码先生成，再批评并修订；通过执行代码取得异常信息，展示外部反馈为何比纯自评更有帮助。  /  |
| K24 多Agent角色、分工与通信 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  5  /  Patterns for Highly Autonomous Agents  /  Agentic design patterns、Multi-agentic workflows、Communication patterns for multi-agent systems、Conclusion。以营销材料为例，拆分 researcher、designer、writer 角色，并对比顺序通信与 manager-led hierarchy。  /  |
| K25 Handoff、Agent-as-tool与委派 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  5  /  Patterns for Highly Autonomous Agents  /  Agentic design patterns、Multi-agentic workflows、Communication patterns for multi-agent systems、Conclusion。以营销材料为例，拆分 researcher、designer、writer 角色，并对比顺序通信与 manager-led hierarchy。  /  |
| K27 MCP客户端、服务器与原语 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  3  /  Tool use  /  What are tools?、Tool syntax、Creating a tool、Code execution、MCP。讲模型返回工具调用请求、参数 schema、工具执行后把结果回填；示例有当前时间、网页搜索、SQL 数据库、计算和 GitHub MCP Server。  /  |
| K31 评测数据集、实验与版本对照 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  4  /  Practical Tips for Building Agentic AI  /  Evaluations、Error analysis、More error analysis examples、How to address problems、Component-level evaluations、Chart generation workflow、Latency/cost optimization、Development process summary。讲端到端与组件评测、gold set、代码裁判/模型裁判、失败归因、测量后优化。  /  |
| K32 指标、Judge与任务基准 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  1  /  Introduction to Agentic Workflows  /  Welcome、What is agentic AI?、Degrees of autonomy、Benefits、Applications、Why not just direct generation?、Task decomposition、Planning workflows、Creating and executing LLM plans、Planning with code execution、Evaluating agentic AI。Research Agent 由直接写作演变为提纲、搜索、草稿、编辑和重写；另举订单邮件、发票和电子表格分析。  /  |
| K33 错误归因、迭代与回归 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  4  /  Practical Tips for Building Agentic AI  /  Evaluations、Error analysis、More error analysis examples、How to address problems、Component-level evaluations、Chart generation workflow、Latency/cost optimization、Development process summary。讲端到端与组件评测、gold set、代码裁判/模型裁判、失败归因、测量后优化。  /  |
| K34 成本、延迟与模型优化 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/curriculum.md)： /  4  /  Practical Tips for Building Agentic AI  /  Evaluations、Error analysis、More error analysis examples、How to address problems、Component-level evaluations、Chart generation workflow、Latency/cost optimization、Development process summary。讲端到端与组件评测、gold set、代码裁判/模型裁判、失败归因、测量后优化。  /  |
| K41 Coding Agent与开发Harness | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/analysis.md)：从已读公开材料看，它没有形成一条状态存储、恢复、人工审批、工具最小权限、幂等、数据库事务和部署容量的系统工程主线。Agentic AI 范围覆盖从固定 workflow 到自主工具使用、MCP 和多 Agent，但“Harness”并不是课程统一使用的课程术语。用它学任务拆分、反思、工具与评测比较合适；把课程定位成完整的 Agent 工程实训或已经拿到全部实验内容，则超出当前证据。 |
| K44 端到端应用与综合项目 | 2 | [记录](../research/agent_courses/providers/deeplearning_ai/analysis.md)：最具体的贯穿案例是 Research Agent。用户给一个研究主题，系统先列提纲并生成搜索词，再取回网页、写草稿、检查是否缺少研究或有不连贯之处、修订，最后输出报告。课程把一个“直接写 essay”的单次生成问题改造成多步流程；随后又用 customer support email、invoice processing、spreadsheet chart 和 marketing assets 解释哪些环节要用模型、数据库/API、代码执行或多个角色。案例使工作流概念易懂，也能看见“需要何时动态调用工具、何时开发者固定步骤”的区别。 |
## Hugging Face AI Agents Course

[官网](https://huggingface.co/learn/agents-course/en/unit0/introduction) · [课程笔记](../courses/huggingface_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)：课程主页：[英文](https://huggingface.co/learn/agents-course/unit0/introduction)｜[简体中文](https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction) |
| K02 LLM、消息、Token与模型选择 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)：课程不是一套单框架速成教程。它先建立 Agent、LLM、消息、工具和 Thought–Action–Observation 循环，再分别讲 `smolagents`、LlamaIndex、LangGraph，随后用同一个晚宴助理案例做 Agentic RAG，最后以 GAIA 子集作公开评测。三个附加单元补函数调用微调、可观测性/评测和游戏 Agent。 |
| K03 提示、指令与Prompt Patterns | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.2：LLM 基础  /  token、next-token prediction、Transformer/attention、prompt、训练阶段、模型调用方式，以及 LLM 在 Agent 中如何承担文本推理。  /  静态图、动画和示例；没有训练作业。  /  对完全没学过 LLM 的读者是快速复习，不足以替代系统的 Transformer 课程。见 `what-are-llms.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K05 Agent loop、ReAct与停止条件 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.5：Agent loop  /  以 Alfred 查天气为例拆 Thought → Action → Observation → updated thought → final action；另讲 ReAct、CoT、Action 的 JSON/function call/code 三种表现，以及模型必须在完整 Action 后停止生成。  /  `dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） 从裸 `InferenceClient` 手写 stop/parse/execute/append loop；展示一次“模型幻觉天气，必须真的执行函数”的失败。  /  与面经中的 `loop`、停止条件、工具反馈、轨迹调试直接对应。课程警告执行模型生成代码有风险，但没有把风险延伸成完整审批协议。  /  |
| K06 工具定义、发现与实际调用 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.5：Agent loop  /  以 Alfred 查天气为例拆 Thought → Action → Observation → updated thought → final action；另讲 ReAct、CoT、Action 的 JSON/function call/code 三种表现，以及模型必须在完整 Action 后停止生成。  /  `dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） 从裸 `InferenceClient` 手写 stop/parse/execute/append loop；展示一次“模型幻觉天气，必须真的执行函数”的失败。  /  与面经中的 `loop`、停止条件、工具反馈、轨迹调试直接对应。课程警告执行模型生成代码有风险，但没有把风险延伸成完整审批协议。  /  |
| K07 结构化输出与参数校验 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.6：第一个 smolagents Agent  /  在 Space 中配置 `HF_TOKEN`，用 `DuckDuckGoSearchTool`、自定义工具、`CodeAgent`、system prompt，并把工具/Agent 推到 Hub。  /  动手搭建派对助理；加载 Hub 工具时示例用了 `trust_remote_code=True`；最终 Unit 1 测验可领取基础证书。  /  可展示从 schema 到运行 Agent 的最短闭环；真实项目需额外审计远程代码、密钥、网络和写操作。见 `tutorial.mdx`（原本地资料引用，未随公开版收录） 与 `final-quiz.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.5：Agent loop  /  以 Alfred 查天气为例拆 Thought → Action → Observation → updated thought → final action；另讲 ReAct、CoT、Action 的 JSON/function call/code 三种表现，以及模型必须在完整 Action 后停止生成。  /  `dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） 从裸 `InferenceClient` 手写 stop/parse/execute/append loop；展示一次“模型幻觉天气，必须真的执行函数”的失败。  /  与面经中的 `loop`、停止条件、工具反馈、轨迹调试直接对应。课程警告执行模型生成代码有风险，但没有把风险延伸成完整审批协议。  /  |
| K09 文件、代码执行与沙箱 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K10 链式工作流、Query与意图路由 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K11 任务分解、规划与重规划 | 2 | [记录](../research/agent_courses/providers/huggingface/analysis.md)：1. **Agent 定义清楚。** 正文把 Agent 定义为“利用 AI 模型与环境交互以完成用户目标的系统”，包含 reasoning、planning、actions/tools；又用 processor → router → tool caller → multi-step → multi-agent 的 agency 光谱避免“所有聊天机器人都算 Agent”的混淆。证据：`what-are-agents.mdx`（原本地资料引用，未随公开版收录），[提交固定页](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/what-are-agents.mdx#L46-L78)。 |
| K13 图编排、节点、边与状态Schema | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2 总览  /  说明何时框架能减少重复实现，课程并列三条路径，而非宣称只有一个正确框架。  /  无独立作业。  /  比较框架时应沿状态、控制流、工具、记忆、可观测性比较，不能只比 API 长短。见 `unit2/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K15 短期记忆与会话历史 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.3：消息与特殊 token  /  system/user/assistant 消息、base 与 instruct 模型、chat template 如何把对话拼成模型所需 prompt。  /  在线 chat-template viewer；代码展示 tokenizer 的模板应用。  /  对“同一消息为何换模型后表现不同”给出了底层格式解释，但没有跨模型回归测试方法。见 `messages-and-special-tokens.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K16 长期、共享与分层记忆 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K19 上下文选择、压缩、卸载与缓存 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K20 文档加载、切分与摘要 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K21 Embedding、向量库与索引 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K22 混合检索、BM25、RRF与重排 | 1 | [记录](../research/agent_courses/providers/huggingface/analysis.md)： /  RAG  /  中强  /  ingestion/index/query/eval，QueryEngineTool，guest retriever，Agentic RAG 多工具案例。  /  chunk/召回/重排实验、引用正确性、ACL、增量更新、线上 bad-case 回归。  /  |
| K23 Agentic RAG与检索工具 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K24 多Agent角色、分工与通信 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.1：什么是 Agent  /  给出正式定义：Agent 是利用 AI 模型与环境交互、完成用户目标的系统；把系统拆为“模型大脑”和“能力/工具身体”；用从 processor、router、tool caller、multi-step 到 multi-agent 的连续 agency 光谱解释“多自主才算 Agent”。  /  6 题不计分小测。  /  这是课程最适合做定义锚点的章节；它把 router 和 loop 放在同一连续谱上，也明确 Action 不等于 Tool。见 `what-are-agents.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K25 Handoff、Agent-as-tool与委派 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K27 MCP客户端、服务器与原语 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K29 框架抽象、手写框架与选型 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.6：第一个 smolagents Agent  /  在 Space 中配置 `HF_TOKEN`，用 `DuckDuckGoSearchTool`、自定义工具、`CodeAgent`、system prompt，并把工具/Agent 推到 Hub。  /  动手搭建派对助理；加载 Hub 工具时示例用了 `trust_remote_code=True`；最终 Unit 1 测验可领取基础证书。  /  可展示从 schema 到运行 Agent 的最短闭环；真实项目需额外审计远程代码、密钥、网络和写操作。见 `tutorial.mdx`（原本地资料引用，未随公开版收录） 与 `final-quiz.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K30 Trace、Span与运行可观测性 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2 总览  /  说明何时框架能减少重复实现，课程并列三条路径，而非宣称只有一个正确框架。  /  无独立作业。  /  比较框架时应沿状态、控制流、工具、记忆、可观测性比较，不能只比 API 长短。见 `unit2/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K31 评测数据集、实验与版本对照 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 3：Agentic RAG 用例  /  晚宴助理 Alfred 读取 `unit3-invitees` 数据集，建 guest retriever，再接 DuckDuckGo、天气、Hub stats 工具；分别提供 smolagents、LlamaIndex、LangGraph 实现；最后比较三者的记忆接法。  /  在公开 HF Space 中按模块组织代码；端到端例子覆盖 guest 查询、天气、研究者资料和多工具组合。  /  是课程把工具、RAG、编排和 memory 汇总成一个项目的核心单元。语料小且固定，示例含 email 等字段；没有访问控制、数据更新、召回指标和 PII 治理。见 `agentic-rag/invitees.mdx`（原本地资料引用，未随公开版收录）、`tools.mdx`（原本地资料引用，未随公开版收录）、`agent.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K32 指标、Judge与任务基准 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.2：LlamaIndex  /  RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。  /  两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。  /  对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K33 错误归因、迭代与回归 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.3：消息与特殊 token  /  system/user/assistant 消息、base 与 instruct 模型、chat template 如何把对话拼成模型所需 prompt。  /  在线 chat-template viewer；代码展示 tokenizer 的模板应用。  /  对“同一消息为何换模型后表现不同”给出了底层格式解释，但没有跨模型回归测试方法。见 `messages-and-special-tokens.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K34 成本、延迟与模型优化 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 4：最终项目  /  介绍 GAIA 的多步、工具、多模态任务与三档难度；课程取 Level 1 validation 中 20 题，提供取题、取附件、提交答案 API；答案按 exact match 评分。  /  复制 Final Assignment Space，公开 `agent_code`，提交 `task_id/submitted_answer`，上学生榜，之后领取结业证书。  /  这是明确可量化的终局作业，但 leaderboard 本身提示可绕过验证；exact match 也只评最终答案，不等于轨迹安全、成本和权限正确。见 `what-is-gaia.mdx`（原本地资料引用，未随公开版收录）、`hands-on.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K35 服务部署、UI/API集成与交付 | 3 | [记录](../research/agent_courses/providers/huggingface/analysis.md)：它不是完整的生产 Agent 工程课程。写操作审批、模糊请求澄清、最小权限、幂等、数据库事务、并发隔离、checkpoint/恢复、部署、容量与多租户没有形成主线。课程会提醒代码执行风险和 sandbox，会展示 Langfuse trace、GAIA 及 exact match，但这些还不足以回答国内面经里关于 Harness、写操作边界、SQLite/并发、上线与回滚的连续追问。 |
| K37 授权、Guardrails与操作边界 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.4：工具  /  Tool 的名称、描述、typed arguments、输出、callable；模型只生成调用文本，Agent 才负责解析、执行并把 Observation 回填；用 decorator/反射自动生成工具说明，末尾介绍 MCP。  /  手写 `calculator`、通用 `Tool` 类和 `@tool` 思路；5 题小测。  /  工具 schema 与执行 loop 解释完整；缺少幂等、副作用、权限和审批的系统设计。见 `tools.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K38 不可信输入、注入与数据安全 | 1 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 3：Agentic RAG 用例  /  晚宴助理 Alfred 读取 `unit3-invitees` 数据集，建 guest retriever，再接 DuckDuckGo、天气、Hub stats 工具；分别提供 smolagents、LlamaIndex、LangGraph 实现；最后比较三者的记忆接法。  /  在公开 HF Space 中按模块组织代码；端到端例子覆盖 guest 查询、天气、研究者资料和多工具组合。  /  是课程把工具、RAG、编排和 memory 汇总成一个项目的核心单元。语料小且固定，示例含 email 等字段；没有访问控制、数据更新、召回指标和 PII 治理。见 `agentic-rag/invitees.mdx`（原本地资料引用，未随公开版收录）、`tools.mdx`（原本地资料引用，未随公开版收录）、`agent.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K42 浏览器与Computer Use | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K43 多模态、视觉与环境输入 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 2.1：smolagents  /  `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。  /  两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。  /  loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K44 端到端应用与综合项目 | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.3：消息与特殊 token  /  system/user/assistant 消息、base 与 instruct 模型、chat template 如何把对话拼成模型所需 prompt。  /  在线 chat-template viewer；代码展示 tokenizer 的模板应用。  /  对“同一消息为何换模型后表现不同”给出了底层格式解释，但没有跨模型回归测试方法。见 `messages-and-special-tokens.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K45 SFT、LoRA与Agentic RL | 3 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)： /  Unit 1.2：LLM 基础  /  token、next-token prediction、Transformer/attention、prompt、训练阶段、模型调用方式，以及 LLM 在 Agent 中如何承担文本推理。  /  静态图、动画和示例；没有训练作业。  /  对完全没学过 LLM 的读者是快速复习，不足以替代系统的 Transformer 课程。见 `what-are-llms.mdx`（原本地资料引用，未随公开版收录）。  /  |
| K46 研究论文、能力基准与研究方法 | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)：研究日期：2026-10-03（Asia/Shanghai） |
| K47 游戏、具身与机器人Agent | 2 | [记录](../research/agent_courses/providers/huggingface/curriculum.md)：课程不是一套单框架速成教程。它先建立 Agent、LLM、消息、工具和 Thought–Action–Observation 循环，再分别讲 `smolagents`、LlamaIndex、LangGraph，随后用同一个晚宴助理案例做 Agentic RAG，最后以 GAIA 子集作公开评测。三个附加单元补函数调用微调、可观测性/评测和游戏 Agent。 |
## Google × Kaggle：5-Day AI Agents Intensive（2025）

[官网](https://www.kaggle.com/learn-guide/5-day-agents) · [课程笔记](../courses/google_agents_2025/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第1天：Agent入门: Agent基础、单Agent与多Agent |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第2天：工具与MCP: Python工具、MCP、人工批准 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第3天：会话与记忆: 会话管理、跨会话记忆 |
| K16 长期、共享与分层记忆 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第3天：会话与记忆: 会话管理、跨会话记忆 |
| K18 人工介入、批准与交接 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第2天：工具与MCP: Python工具、MCP、人工批准 |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第1天：Agent入门: Agent基础、单Agent与多Agent |
| K27 MCP客户端、服务器与原语 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第2天：工具与MCP: Python工具、MCP、人工批准 |
| K28 A2A、ANP与跨Agent互操作 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第5天：A2A与生产部署: A2A、生产部署、综合项目 |
| K30 Trace、Span与运行可观测性 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第4天：可观测性与评测: 运行观测、Agent评测 |
| K31 评测数据集、实验与版本对照 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第4天：可观测性与评测: 运行观测、Agent评测 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第5天：A2A与生产部署: A2A、生产部署、综合项目 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第5天：A2A与生产部署: A2A、生产部署、综合项目 |
## Google × Kaggle：5-Day AI Agents Intensive（2026 Vibe Coding版）

[官网](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding) · [课程笔记](../courses/google_agents_2026_vibecoding/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第1天：Agent与Vibe Coding: Agent基础、Vibe Coding |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第2天：工具互操作: 工具互操作、连接不同工具 |
| K26 Skills与可复用能力 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第3天：Agent Skills: Agent Skills、技能使用 |
| K31 评测数据集、实验与版本对照 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第4天：安全与评测: 安全、评测 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第5天：规格驱动部署: 规格驱动开发、部署 |
| K38 不可信输入、注入与数据安全 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第4天：安全与评测: 安全、评测 |
| K48 Vibe Coding与规格驱动开发 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：第1天：Agent与Vibe Coding: Agent基础、Vibe Coding |
## Vanderbilt：AI Agents and Agentic AI with Python & Generative AI

[官网](https://www.coursera.org/specializations/ai-agents-python) · [课程笔记](../courses/vanderbilt_python_agent_implementation/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 手写框架组件、工具发现与函数调用、文件探索、文档生成 |
| K09 文件、代码执行与沙箱 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 手写框架组件、工具发现与函数调用、文件探索、文档生成 |
| K29 框架抽象、手写框架与选型 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 手写框架组件、工具发现与函数调用、文件探索、文档生成 |
## Vanderbilt：Prompt Engineering for ChatGPT

[官网](https://www.coursera.org/specializations/ai-agents-python) · [课程笔记](../courses/vanderbilt_prompt_engineering/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K03 提示、指令与Prompt Patterns | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 提示词设计、Prompt Patterns 提示模式、生活、工作与教育中的提示应用 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 提示词设计、Prompt Patterns 提示模式、生活、工作与教育中的提示应用 |
## Vanderbilt：AI Agents and Agentic AI Architecture in Python

[官网](https://www.coursera.org/specializations/ai-agents-python) · [课程笔记](../courses/vanderbilt_python_agent_architecture/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K16 长期、共享与分层记忆 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 多Agent协作、共享记忆、分阶段执行、可逆动作 |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 多Agent协作、共享记忆、分阶段执行、可逆动作 |
| K39 审计、动作凭据、幂等与回滚 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：简介主题: 多Agent协作、共享记忆、分阶段执行、可逆动作 |
## Microsoft AI Agents for Beginners

[官网](https://github.com/microsoft/ai-agents-for-beginners) · [课程笔记](../courses/microsoft_ai_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)：上游仓库：[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) |
| K02 LLM、消息、Token与模型选择 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  01 Intro to AI Agents  /  Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。  /  Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。  /  为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K03 提示、指令与Prompt Patterns | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  06 Trustworthy Agents  /  system message framework；任务/指令攻击、关键系统访问、资源过载、知识库投毒、级联错误；input filters、turn limits、limited environment、fallback/retry；human-in-the-loop。  /  两个 notebook：system message 与 pre-action approval/risk tier/audit log。  /  对写操作边界和人工审批建立第一层机制；风险分级细节主要在 notebook，不只在 README。正文：`06-building-trustworthy-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K05 Agent loop、ReAct与停止条件 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  01 Intro to AI Agents  /  Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。  /  Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。  /  为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K06 工具定义、发现与实际调用 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  01 Intro to AI Agents  /  Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。  /  Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。  /  为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K07 结构化输出与参数校验 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  04 Tool Use  /  工具模式、function/tool schema、执行逻辑、路由、消息处理、validation/error handling、state；Responses API function calling；MAF 与 Foundry toolset；SQLite 查询和 Code Interpreter；SQL 应配置只读角色。  /  Python notebook、.NET 代码；SQLite tool 例子；可部署后 smoke test。  /  直接对应工具 schema、意图选工具、参数校验和 SQLite 权限。正文：`04-tool-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  02 Explore Agentic Frameworks  /  框架为何提供模型、工具、状态、协作与实时反馈；区分 MAF（客户端 framework）与 Microsoft Foundry Agent Service（托管服务）；比较两种使用场景。  /  两个 Python notebook（Foundry 与 Azure OpenAI）和 .NET 示例。  /  对“框架和托管 Agent 服务有什么区别”给出可面试的结构；也为 Harness/运行时拆层。正文：`02-explore-agentic-frameworks/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K09 文件、代码执行与沙箱 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  11 Agentic Protocols  /  MCP 的 host/client/server/tools/resources/prompts；A2A 的 Agent Card/Executor/Artifact/Event Queue；NLWeb 和 MCP endpoint。  /  MCP、A2A notebooks；GitHub MCP + Chainlit app/配置文件；mcp-agents 示例。  /  能讲协议角色，不等于已解决鉴权、租户隔离或工具信任。正文：`11-agentic-protocols/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K10 链式工作流、Query与意图路由 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  04 Tool Use  /  工具模式、function/tool schema、执行逻辑、路由、消息处理、validation/error handling、state；Responses API function calling；MAF 与 Foundry toolset；SQLite 查询和 Code Interpreter；SQL 应配置只读角色。  /  Python notebook、.NET 代码；SQLite tool 例子；可部署后 smoke test。  /  直接对应工具 schema、意图选工具、参数校验和 SQLite 权限。正文：`04-tool-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K11 任务分解、规划与重规划 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  01 Intro to AI Agents  /  Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。  /  Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。  /  为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K12 反思、自检与修订 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  09 Metacognition  /  课程最长正文（1434 行）：self-reflection、planning、corrective RAG、pre-emptive context、goal bootstrap、LLM rerank/relevance、intent-aware search、code-as-tool、环境感知、SQL-as-RAG、反思后调整策略。  /  单个 Python notebook；README 内含大量可复制 Python 片段。  /  覆盖 query/intent、rerank、SQL、反思；内容广但松散，动态 SQL 例子用字符串拼接，不是生产 SQL 安全模板。正文：`09-metacognition/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K13 图编排、节点、边与状态Schema | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  02 Explore Agentic Frameworks  /  框架为何提供模型、工具、状态、协作与实时反馈；区分 MAF（客户端 framework）与 Microsoft Foundry Agent Service（托管服务）；比较两种使用场景。  /  两个 Python notebook（Foundry 与 Azure OpenAI）和 .NET 示例。  /  对“框架和托管 Agent 服务有什么区别”给出可面试的结构；也为 Harness/运行时拆层。正文：`02-explore-agentic-frameworks/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K14 并行、子图与Map-Reduce | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  08 Multi-Agent  /  何时需要多 Agent；specialization、scalability、fault tolerance；communication、coordination、visibility、HITL；group chat、handoff、collaborative filtering；refund process。  /  多个 Python/.NET workflow notebook，覆盖 basic/sequential/concurrent/conditional；作业要求设计 customer support 多 Agent，附 solution 和 2 题 knowledge check。  /  与“单 Agent 还是多 Agent、怎么路由、怎么观测”高度对应。正文：`08-multi-agent/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K15 短期记忆与会话历史 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  04 Tool Use  /  工具模式、function/tool schema、执行逻辑、路由、消息处理、validation/error handling、state；Responses API function calling；MAF 与 Foundry toolset；SQLite 查询和 Code Interpreter；SQL 应配置只读角色。  /  Python notebook、.NET 代码；SQLite tool 例子；可部署后 smoke test。  /  直接对应工具 schema、意图选工具、参数校验和 SQLite 权限。正文：`04-tool-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K16 长期、共享与分层记忆 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  14 Microsoft Agent Framework  /  Agent/thread/message、thread serialize/deserialize、自定义 message store、Mem0；workflow sequential/concurrent/conditional/handoff/HITL/middleware；把 LangChain/LangGraph Agent 托管到 Foundry `/responses`。  /  7 个 notebooks + `hotel_booking_workflow_sample.py` + `14-langchain-hosted-agent.py`。  /  最接近 Harness/编排实作核心；能展示 state persistence 和 middleware，但主路径仍绑定 MAF/Foundry。正文：`14-microsoft-agent-framework/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K17 Checkpoint、持久化与恢复 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  03 Agentic Design Patterns  /  Agent Space/Time/Core 三个设计维度；将复杂旅行 Agent 拆成角色、步骤、能力与用户旅程。  /  Python/.NET 旅行示例；无评分作业。  /  更偏产品/架构草图，具体失败恢复和权限还没有进入。正文：`03-agentic-design-patterns/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K18 人工介入、批准与交接 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  06 Trustworthy Agents  /  system message framework；任务/指令攻击、关键系统访问、资源过载、知识库投毒、级联错误；input filters、turn limits、limited environment、fallback/retry；human-in-the-loop。  /  两个 notebook：system message 与 pre-action approval/risk tier/audit log。  /  对写操作边界和人工审批建立第一层机制；风险分级细节主要在 notebook，不只在 README。正文：`06-building-trustworthy-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K19 上下文选择、压缩、卸载与缓存 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  01 Intro to AI Agents  /  Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。  /  Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。  /  为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K20 文档加载、切分与摘要 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  05 Agentic RAG  /  区分传统 RAG 与 Agentic RAG；Agent 拥有查询重写、迭代检索、多工具、memory/self-correction；列失败模式、agency 边界、governance。  /  Python/.NET notebook，默认可用内存知识库，可选 Azure AI Search；可部署后 smoke test。  /  适合回答“为什么 RAG 要 Agent 化”，但 chunk/召回/重排评测深度有限。正文：`05-agentic-rag/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K22 混合检索、BM25、RRF与重排 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  05 Agentic RAG  /  区分传统 RAG 与 Agentic RAG；Agent 拥有查询重写、迭代检索、多工具、memory/self-correction；列失败模式、agency 边界、governance。  /  Python/.NET notebook，默认可用内存知识库，可选 Azure AI Search；可部署后 smoke test。  /  适合回答“为什么 RAG 要 Agent 化”，但 chunk/召回/重排评测深度有限。正文：`05-agentic-rag/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K23 Agentic RAG与检索工具 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  05 Agentic RAG  /  区分传统 RAG 与 Agentic RAG；Agent 拥有查询重写、迭代检索、多工具、memory/self-correction；列失败模式、agency 边界、governance。  /  Python/.NET notebook，默认可用内存知识库，可选 Azure AI Search；可部署后 smoke test。  /  适合回答“为什么 RAG 要 Agent 化”，但 chunk/召回/重排评测深度有限。正文：`05-agentic-rag/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K24 多Agent角色、分工与通信 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  08 Multi-Agent  /  何时需要多 Agent；specialization、scalability、fault tolerance；communication、coordination、visibility、HITL；group chat、handoff、collaborative filtering；refund process。  /  多个 Python/.NET workflow notebook，覆盖 basic/sequential/concurrent/conditional；作业要求设计 customer support 多 Agent，附 solution 和 2 题 knowledge check。  /  与“单 Agent 还是多 Agent、怎么路由、怎么观测”高度对应。正文：`08-multi-agent/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K25 Handoff、Agent-as-tool与委派 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  08 Multi-Agent  /  何时需要多 Agent；specialization、scalability、fault tolerance；communication、coordination、visibility、HITL；group chat、handoff、collaborative filtering；refund process。  /  多个 Python/.NET workflow notebook，覆盖 basic/sequential/concurrent/conditional；作业要求设计 customer support 多 Agent，附 solution 和 2 题 knowledge check。  /  与“单 Agent 还是多 Agent、怎么路由、怎么观测”高度对应。正文：`08-multi-agent/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K26 Skills与可复用能力 | 1 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  15 Computer Use Agents  /  Browser-Use、Playwright/CDP、vision、Pydantic extraction；Agent 与 actor 的取舍；页面不可信；域名/动作/时间预算；观察与动作分离；登录、发信、购买、删除、改设置前显式审批；遇模糊状态停止。  /  Airbnb 搜索 notebook；5 题 knowledge check；Project Opal 案例把 Skills 描述为可复用 `.md` 指令。  /  这套课对“模糊问题/写操作边界”最具体的一课。正文：`15-browser-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K27 MCP客户端、服务器与原语 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  11 Agentic Protocols  /  MCP 的 host/client/server/tools/resources/prompts；A2A 的 Agent Card/Executor/Artifact/Event Queue；NLWeb 和 MCP endpoint。  /  MCP、A2A notebooks；GitHub MCP + Chainlit app/配置文件；mcp-agents 示例。  /  能讲协议角色，不等于已解决鉴权、租户隔离或工具信任。正文：`11-agentic-protocols/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K28 A2A、ANP与跨Agent互操作 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  11 Agentic Protocols  /  MCP 的 host/client/server/tools/resources/prompts；A2A 的 Agent Card/Executor/Artifact/Event Queue；NLWeb 和 MCP endpoint。  /  MCP、A2A notebooks；GitHub MCP + Chainlit app/配置文件；mcp-agents 示例。  /  能讲协议角色，不等于已解决鉴权、租户隔离或工具信任。正文：`11-agentic-protocols/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K29 框架抽象、手写框架与选型 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)：当前 README 标题是“18 Lessons to Get Started Building AI Agents”，实际仓库包含 `00-course-setup` 加 `01`–`18`。2026 年 7 月课程完成了一次大迁移：从 GitHub Models/旧 API 转向 Microsoft Agent Framework（MAF）和 Azure OpenAI Responses API，并新增可扩展部署、本地 Agent 与安全收据章节。最新代码把 `agent-framework-core` 固定为 `1.10.0`，Foundry/OpenAI integrations 固定在 `~1.10.0`，主模型示例换成 `gpt-5-mini`。证据见 `CHANGELOG.md`（原本地资料引用，未随公开版收录）、`requirements.txt`（原本地资料引用，未随公开版收录） 和 [当前 README](https://github.com/microsoft/ai-agents-for-beginners)。 |
| K30 Trace、Span与运行可观测性 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  08 Multi-Agent  /  何时需要多 Agent；specialization、scalability、fault tolerance；communication、coordination、visibility、HITL；group chat、handoff、collaborative filtering；refund process。  /  多个 Python/.NET workflow notebook，覆盖 basic/sequential/concurrent/conditional；作业要求设计 customer support 多 Agent，附 solution 和 2 题 knowledge check。  /  与“单 Agent 还是多 Agent、怎么路由、怎么观测”高度对应。正文：`08-multi-agent/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K31 评测数据集、实验与版本对照 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  05 Agentic RAG  /  区分传统 RAG 与 Agentic RAG；Agent 拥有查询重写、迭代检索、多工具、memory/self-correction；列失败模式、agency 边界、governance。  /  Python/.NET notebook，默认可用内存知识库，可选 Azure AI Search；可部署后 smoke test。  /  适合回答“为什么 RAG 要 Agent 化”，但 chunk/召回/重排评测深度有限。正文：`05-agentic-rag/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K32 指标、Judge与任务基准 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  03 Agentic Design Patterns  /  Agent Space/Time/Core 三个设计维度；将复杂旅行 Agent 拆成角色、步骤、能力与用户旅程。  /  Python/.NET 旅行示例；无评分作业。  /  更偏产品/架构草图，具体失败恢复和权限还没有进入。正文：`03-agentic-design-patterns/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K33 错误归因、迭代与回归 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  03 Agentic Design Patterns  /  Agent Space/Time/Core 三个设计维度；将复杂旅行 Agent 拆成角色、步骤、能力与用户旅程。  /  Python/.NET 旅行示例；无评分作业。  /  更偏产品/架构草图，具体失败恢复和权限还没有进入。正文：`03-agentic-design-patterns/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K34 成本、延迟与模型优化 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  10 Agents in Production  /  traces/spans；生产观测价值；latency、cost、request errors、显式/隐式反馈、accuracy、automated eval；OpenTelemetry；offline/online eval 闭环；连续 loop、multi-agent 不稳定、fallback、模型路由、cache。  /  费用报销 observability/eval notebook；没有独立作业。  /  与 `eval/model consistency/production` 强相关；强调 offline eval 是上线前最低门槛。正文：`10-ai-agents-production/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K35 服务部署、UI/API集成与交付 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)：当前 README 标题是“18 Lessons to Get Started Building AI Agents”，实际仓库包含 `00-course-setup` 加 `01`–`18`。2026 年 7 月课程完成了一次大迁移：从 GitHub Models/旧 API 转向 Microsoft Agent Framework（MAF）和 Azure OpenAI Responses API，并新增可扩展部署、本地 Agent 与安全收据章节。最新代码把 `agent-framework-core` 固定为 `1.10.0`，Foundry/OpenAI integrations 固定在 `~1.10.0`，主模型示例换成 `gpt-5-mini`。证据见 `CHANGELOG.md`（原本地资料引用，未随公开版收录）、`requirements.txt`（原本地资料引用，未随公开版收录） 和 [当前 README](https://github.com/microsoft/ai-agents-for-beginners)。 |
| K36 扩展、并发、外部状态与生命周期 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  13 Agent Memory  /  working、short-term、long-term、persona、episodic/workflow、entity、structured RAG memory；Mem0、Cognee、RAG storage；memory optimization/self-improve。  /  两个 notebook：MAF memory 与 Cognee。  /  分类较完整；隐私、遗忘、污染检测、版本和并发写冲突仍浅。正文：`13-agent-memory/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K37 授权、Guardrails与操作边界 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  03 Agentic Design Patterns  /  Agent Space/Time/Core 三个设计维度；将复杂旅行 Agent 拆成角色、步骤、能力与用户旅程。  /  Python/.NET 旅行示例；无评分作业。  /  更偏产品/架构草图，具体失败恢复和权限还没有进入。正文：`03-agentic-design-patterns/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K38 不可信输入、注入与数据安全 | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)：当前 README 标题是“18 Lessons to Get Started Building AI Agents”，实际仓库包含 `00-course-setup` 加 `01`–`18`。2026 年 7 月课程完成了一次大迁移：从 GitHub Models/旧 API 转向 Microsoft Agent Framework（MAF）和 Azure OpenAI Responses API，并新增可扩展部署、本地 Agent 与安全收据章节。最新代码把 `agent-framework-core` 固定为 `1.10.0`，Foundry/OpenAI integrations 固定在 `~1.10.0`，主模型示例换成 `gpt-5-mini`。证据见 `CHANGELOG.md`（原本地资料引用，未随公开版收录）、`requirements.txt`（原本地资料引用，未随公开版收录） 和 [当前 README](https://github.com/microsoft/ai-agents-for-beginners)。 |
| K39 审计、动作凭据、幂等与回滚 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  18 Securing Agents  /  Ed25519 + JCS 的 tool-call cryptographic receipt；hash args/result；verify tampering；链式 receipt；明确“证明了什么/没证明什么”；human approval receipt 绑定同一 canonical action、policy version、key registry 与 expiry。  /  两个 notebook、sample receipts；5 题 knowledge check；4 节 practice；两个 stretch challenges；production checklist。  /  对高风险写操作、审计和人类批准给出课程中最严格的证据模型；但 receipt 不能替代输入验证、policy 或身份基础设施。正文：`18-securing-ai-agents/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K40 本地模型、本地Agent与混合运行 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)：当前 README 标题是“18 Lessons to Get Started Building AI Agents”，实际仓库包含 `00-course-setup` 加 `01`–`18`。2026 年 7 月课程完成了一次大迁移：从 GitHub Models/旧 API 转向 Microsoft Agent Framework（MAF）和 Azure OpenAI Responses API，并新增可扩展部署、本地 Agent 与安全收据章节。最新代码把 `agent-framework-core` 固定为 `1.10.0`，Foundry/OpenAI integrations 固定在 `~1.10.0`，主模型示例换成 `gpt-5-mini`。证据见 `CHANGELOG.md`（原本地资料引用，未随公开版收录）、`requirements.txt`（原本地资料引用，未随公开版收录） 和 [当前 README](https://github.com/microsoft/ai-agents-for-beginners)。 |
| K41 Coding Agent与开发Harness | 2 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  02 Explore Agentic Frameworks  /  框架为何提供模型、工具、状态、协作与实时反馈；区分 MAF（客户端 framework）与 Microsoft Foundry Agent Service（托管服务）；比较两种使用场景。  /  两个 Python notebook（Foundry 与 Azure OpenAI）和 .NET 示例。  /  对“框架和托管 Agent 服务有什么区别”给出可面试的结构；也为 Harness/运行时拆层。正文：`02-explore-agentic-frameworks/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K42 浏览器与Computer Use | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  15 Computer Use Agents  /  Browser-Use、Playwright/CDP、vision、Pydantic extraction；Agent 与 actor 的取舍；页面不可信；域名/动作/时间预算；观察与动作分离；登录、发信、购买、删除、改设置前显式审批；遇模糊状态停止。  /  Airbnb 搜索 notebook；5 题 knowledge check；Project Opal 案例把 Skills 描述为可复用 `.md` 指令。  /  这套课对“模糊问题/写操作边界”最具体的一课。正文：`15-browser-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K43 多模态、视觉与环境输入 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  15 Computer Use Agents  /  Browser-Use、Playwright/CDP、vision、Pydantic extraction；Agent 与 actor 的取舍；页面不可信；域名/动作/时间预算；观察与动作分离；登录、发信、购买、删除、改设置前显式审批；遇模糊状态停止。  /  Airbnb 搜索 notebook；5 题 knowledge check；Project Opal 案例把 Skills 描述为可复用 `.md` 指令。  /  这套课对“模糊问题/写操作边界”最具体的一课。正文：`15-browser-use/README.md`（原本地资料引用，未随公开版收录）。  /  |
| K44 端到端应用与综合项目 | 3 | [记录](../research/agent_courses/providers/microsoft/curriculum.md)： /  00 Course Setup  /  浅克隆/稀疏克隆、Codespaces；Python 3.12+、可选 .NET 10+、Azure CLI；Foundry hub/project/model；`az login` 无密钥认证；`.env`；Azure AI Search；Azure OpenAI；MiniMax、Novita、Foundry Local；Bing connection。  /  安装 `requirements.txt`（原本地资料引用，未随公开版收录），创建 Foundry 项目与模型部署；未要求执行付费 API。  /  先分清“公开教材免费”和“运行主路径需要 Azure subscription/模型资源”。正文：`00-course-setup/README.md`（原本地资料引用，未随公开版收录）。  /  |
## Datawhale《Generic Agent 使用指南》

[官网](https://datawhalechina.github.io/hello-generic-agent/) · [课程笔记](../courses/generic_agent/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：原理篇: Agent循环、工具集、分层记忆、上下文压缩、自我进化 |
| K05 Agent loop、ReAct与停止条件 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：原理篇: Agent循环、工具集、分层记忆、上下文压缩、自我进化 |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：原理篇: Agent循环、工具集、分层记忆、上下文压缩、自我进化 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：应用指南: 安装、浏览器能力、日常使用、记忆与技能、聊天平台集成 |
| K16 长期、共享与分层记忆 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：原理篇: Agent循环、工具集、分层记忆、上下文压缩、自我进化 |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：原理篇: Agent循环、工具集、分层记忆、上下文压缩、自我进化 |
| K26 Skills与可复用能力 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：应用指南: 安装、浏览器能力、日常使用、记忆与技能、聊天平台集成 |
| K42 浏览器与Computer Use | 1 | [记录](../research/agent_courses/additional_open_courses.md)：应用指南: 安装、浏览器能力、日常使用、记忆与技能、聊天平台集成 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：应用指南: 安装、浏览器能力、日常使用、记忆与技能、聊天平台集成 |
## freeCodeCamp发布：Agentic AI – Complete Course for Beginners

[官网](https://www.youtube.com/watch?v=Zy7EXDONlTY) · [课程笔记](../courses/freecodecamp_agentic_ai/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：基础: Agentic AI基础、异步Python、Pydantic |
| K04 Python、异步与类型化编程基础 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：基础: Agentic AI基础、异步Python、Pydantic |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K07 结构化输出与参数校验 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：基础: Agentic AI基础、异步Python、Pydantic |
| K10 链式工作流、Query与意图路由 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：LangGraph与项目: 工作流、聊天机器人 |
| K13 图编排、节点、边与状态Schema | 1 | [记录](../research/agent_courses/additional_open_courses.md)：LangGraph与项目: 工作流、聊天机器人 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K18 人工介入、批准与交接 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K23 Agentic RAG与检索工具 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：LangChain Agent: 单Agent、多Agent |
| K29 框架抽象、手写框架与选型 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：LangChain Agent: 单Agent、多Agent |
| K30 Trace、Span与运行可观测性 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：项目工程主题: 记忆与工具、RAG、人工介入、监控、部署 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：LangGraph与项目: 工作流、聊天机器人 |
## LangChain Academy Introduction to LangGraph

[官网](https://academy.langchain.com/courses/intro-to-langgraph) · [课程笔记](../courses/langgraph_fundamentals/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K03 提示、指令与Prompt Patterns | 2 | [记录](../research/agent_courses/providers/langchain/curriculum.md)：章节次序体现从单图到服务部署的递进，但完整课堂视频和平台内练习与仓库 notebook 并非同一份材料。模块中的 Studio 说明还包含录制版与当前工具名称/部署方式的差异提示。 |
| K05 Agent loop、ReAct与停止条件 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K06 工具定义、发现与实际调用 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K07 结构化输出与参数校验 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  2：State and Memory  /  State Schema、State Reducers、Multiple Schemas、Trim and Filter Messages、摘要与 Memory、External Memory  /  state-schema.ipynb 展示 TypedDict/dataclass/Pydantic；state-reducers.ipynb 讲覆盖、追加、自定义 reducer 与 message 删除；chatbot-summarization.ipynb 在超过六条消息后滚动总结；chatbot-external-memory.ipynb 用 SqliteSaver 持久化。  /  |
| K10 链式工作流、Query与意图路由 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K11 任务分解、规划与重规划 | 2 | [记录](../research/agent_courses/providers/langchain/analysis.md)：术语链条覆盖较完整：图状态如何声明、节点如何返回部分状态、边如何路由、Reducer 如何合并消息、Checkpoint 如何按 thread 保存、Store 如何跨 thread 取资料，都配有可定位源码。课程也有实现边界：SQLite 例子是本地单连接的持久化演示，没有压测、连接池或容量比较；后续部署样例用 Postgres/Redis 和 Server 来展示服务拓扑，但没有完整容量规划、SLO、故障恢复演练或生产权限审计。工具批准以图中断和人工反馈为主，没有系统讨论最小权限、写操作分级、幂等或补偿事务。 |
| K13 图编排、节点、边与状态Schema | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)：课程：[Introduction to LangGraph - Python](https://academy.langchain.com/courses/intro-to-langgraph)。官方页列为免费、55 lessons、约 6 小时视频；本地仓库将材料按 Module 0–6 组织。下面按目录与现有 notebook 列出可核对内容，不代表视频已观看或所有线上练习均已离线保存。 |
| K14 并行、子图与Map-Reduce | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  4：Building Your Assistant  /  Parallelization、Sub-graphs、Map-reduce、Research Assistant  /  map-reduce.ipynb 并行生成笑话后归并挑选；research-assistant.ipynb 让人工修订 analyst 人设，再并行访谈/检索并生成报告。  /  |
| K15 短期记忆与会话历史 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  2：State and Memory  /  State Schema、State Reducers、Multiple Schemas、Trim and Filter Messages、摘要与 Memory、External Memory  /  state-schema.ipynb 展示 TypedDict/dataclass/Pydantic；state-reducers.ipynb 讲覆盖、追加、自定义 reducer 与 message 删除；chatbot-summarization.ipynb 在超过六条消息后滚动总结；chatbot-external-memory.ipynb 用 SqliteSaver 持久化。  /  |
| K16 长期、共享与分层记忆 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  5：Long-Term Memory  /  Short vs. Long-Term Memory、LangGraph Store、Profile、Collection、Long-Term Memory Agent  /  memory_store.ipynb 区分 thread checkpoint 与跨会话 Store；profile/collection notebook 用 schema 管理资料；Trustcall 示例通过 JSON Patch 更新已有用户偏好。  /  |
| K17 Checkpoint、持久化与恢复 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K18 人工介入、批准与交接 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  3：UX and Human-in-the-Loop  /  Streaming、Breakpoints、Editing State and Human Feedback、Dynamic Breakpoints、Time Travel  /  breakpoints.ipynb 在 tools 节点执行前停下等待批准；edit-state-human-feedback.ipynb 展示编辑 state 和等待输入；time-travel.ipynb 演示历史查看、重放与 fork。  /  |
| K19 上下文选择、压缩、卸载与缓存 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  2：State and Memory  /  State Schema、State Reducers、Multiple Schemas、Trim and Filter Messages、摘要与 Memory、External Memory  /  state-schema.ipynb 展示 TypedDict/dataclass/Pydantic；state-reducers.ipynb 讲覆盖、追加、自定义 reducer 与 message 删除；chatbot-summarization.ipynb 在超过六条消息后滚动总结；chatbot-external-memory.ipynb 用 SqliteSaver 持久化。  /  |
| K23 Agentic RAG与检索工具 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  4：Building Your Assistant  /  Parallelization、Sub-graphs、Map-reduce、Research Assistant  /  map-reduce.ipynb 并行生成笑话后归并挑选；research-assistant.ipynb 让人工修订 analyst 人设，再并行访谈/检索并生成报告。  /  |
| K24 多Agent角色、分工与通信 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  2：State and Memory  /  State Schema、State Reducers、Multiple Schemas、Trim and Filter Messages、摘要与 Memory、External Memory  /  state-schema.ipynb 展示 TypedDict/dataclass/Pydantic；state-reducers.ipynb 讲覆盖、追加、自定义 reducer 与 message 删除；chatbot-summarization.ipynb 在超过六条消息后滚动总结；chatbot-external-memory.ipynb 用 SqliteSaver 持久化。  /  |
| K29 框架抽象、手写框架与选型 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)：课程：[Introduction to LangGraph - Python](https://academy.langchain.com/courses/intro-to-langgraph)。官方页列为免费、55 lessons、约 6 小时视频；本地仓库将材料按 Module 0–6 组织。下面按目录与现有 notebook 列出可核对内容，不代表视频已观看或所有线上练习均已离线保存。 |
| K34 成本、延迟与模型优化 | 1 | [记录](../research/agent_courses/providers/langchain/analysis.md)：学习材料是目录页、视频和 notebook 的组合。仓库 notebook 常按“复习—目标—概念—代码—查看结果/trace”组织，代码旁边有短解释，适合边读边改；README 给出 Python 3.11–3.13、虚拟环境、Jupyter 与环境变量步骤。建立实际环境仍需要模型 API key；LangSmith tracing 和 Module 4 的 Tavily 搜索需要各自账号/凭证。课程页虽标为免费，外部 API 是否免费取决于对应服务和账户，不应把“课程免费”理解成“所有实验零成本”。 |
| K35 服务部署、UI/API集成与交付 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  1：Introduction  /  Motivation、Simple Graph、Studio、Chain、Router、Agent、Agent with Memory、可选 Deployment  /  simple-graph.ipynb 从 TypedDict 状态、节点函数和条件边搭图；chain.ipynb 讲 message/tool/reducer；router.ipynb 与 agent.ipynb 对比静态路由和 ToolNode 循环；agent-memory.ipynb 引入 checkpoint/thread_id。  /  |
| K36 扩展、并发、外部状态与生命周期 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  6：Deployment  /  Deployment Concepts、Creating/Connecting to Deployment、Double Texting、Assistants  /  creating.ipynb 使用 CLI/Docker 并配置 Redis/PostgreSQL；connecting.ipynb 展示 run/thread/stream、历史与 Store；double-texting.ipynb 比较 reject/enqueue/interrupt/rollback；assistant.ipynb 区分个人与工作待办助手。  /  |
| K39 审计、动作凭据、幂等与回滚 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  6：Deployment  /  Deployment Concepts、Creating/Connecting to Deployment、Double Texting、Assistants  /  creating.ipynb 使用 CLI/Docker 并配置 Redis/PostgreSQL；connecting.ipynb 展示 run/thread/stream、历史与 Store；double-texting.ipynb 比较 reject/enqueue/interrupt/rollback；assistant.ipynb 区分个人与工作待办助手。  /  |
| K44 端到端应用与综合项目 | 3 | [记录](../research/agent_courses/providers/langchain/curriculum.md)： /  6：Deployment  /  Deployment Concepts、Creating/Connecting to Deployment、Double Texting、Assistants  /  creating.ipynb 使用 CLI/Docker 并配置 Redis/PostgreSQL；connecting.ipynb 展示 run/thread/stream、历史与 Store；double-texting.ipynb 比较 reject/enqueue/interrupt/rollback；assistant.ipynb 区分个人与工作待办助手。  /  |
## LangChain Academy：Project — Ambient Agents with LangGraph

[官网](https://academy.langchain.com/courses/ambient-agents) · [课程笔记](../courses/langchain_ambient_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K13 图编排、节点、边与状态Schema | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：LangGraph基础: 图基础、状态与流程 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：记忆: 记忆管理、跨步骤上下文 |
| K18 人工介入、批准与交接 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：人工介入: 人工检查、交接处理 |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：记忆: 记忆管理、跨步骤上下文 |
| K31 评测数据集、实验与版本对照 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：评测: Agent评测、结果检查 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：部署: 应用部署 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：构建Agent: 邮件管理助手、邮件处理 |
## Anthropic Claude Platform 101

[官网](https://academy.claude.com/courses/claude-platform-101) · [课程笔记](../courses/anthropic_platform_101/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [The agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained)  /  7 min  /  What an agent actually is ；A minimal working example ；Running it ；The same loop in production ；Recap   /  claude-platform-101__the-agent-loop-explained（原本地资料引用，未随公开版收录）  /  |
| K03 提示、指令与Prompt Patterns | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [Context management](https://academy.claude.com/courses/claude-platform-101/context-management)  /  6 min  /  What counts as context ；Pattern 1: Just-in-time context ；Pattern 2: Server-side compaction ；Pattern 3: Prompt caching ；Pattern 4: The memory tool ；Layering the patterns ；Recap   /  claude-platform-101__context-management（原本地资料引用，未随公开版收录）  /  |
| K05 Agent loop、ReAct与停止条件 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [The agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained)  /  7 min  /  What an agent actually is ；A minimal working example ；Running it ；The same loop in production ；Recap   /  claude-platform-101__the-agent-loop-explained（原本地资料引用，未随公开版收录）  /  |
| K06 工具定义、发现与实际调用 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [What is tool use?](https://academy.claude.com/courses/claude-platform-101/what-is-tool-use)  /  8 min  /  What a tool is ；How tools are defined ；Multiple tools: letting Claude pick ；The tool runner: skip the boilerplate ；Real tools wrap your existing code ；Recap   /  claude-platform-101__what-is-tool-use（原本地资料引用，未随公开版收录）  /  |
| K19 上下文选择、压缩、卸载与缓存 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [Context management](https://academy.claude.com/courses/claude-platform-101/context-management)  /  6 min  /  What counts as context ；Pattern 1: Just-in-time context ；Pattern 2: Server-side compaction ；Pattern 3: Prompt caching ；Pattern 4: The memory tool ；Layering the patterns ；Recap   /  claude-platform-101__context-management（原本地资料引用，未随公开版收录）  /  |
| K26 Skills与可复用能力 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [Skills](https://academy.claude.com/courses/claude-platform-101/skills)  /  6 min  /  Skills vs. tools ；Uploading a Skill ；Attaching a Skill to a request ；Running it ；Recap   /  claude-platform-101__skills（原本地资料引用，未随公开版收录）  /  |
| K27 MCP客户端、服务器与原语 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  claude-platform-101  /  [MCP](https://academy.claude.com/courses/claude-platform-101/mcp)  /  6 min  /  The maintenance problem ；Tools vs. skills vs. MCP ；Connecting to an MCP server ；Filtering which tools Claude can use ；Recap   /  claude-platform-101__mcp（原本地资料引用，未随公开版收录）  /  |
## Anthropic Building with the Claude API

[官网](https://academy.claude.com/courses/building-with-the-claude-api) · [课程笔记](../courses/anthropic_claude_api/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [A typical eval workflow](https://academy.claude.com/courses/building-with-the-claude-api/a-typical-eval-workflow)  /  10 min  /  Step 1: Draft a Prompt ；Step 2: Create an Eval Dataset ；Step 3: Feed Through Claude ；Step 4: Feed Through a Grader ；Step 5: Change Prompt and Repeat ；Prompt Scoring   /  building-with-the-claude-api__a-typical-eval-workflow（原本地资料引用，未随公开版收录）  /  |
| K02 LLM、消息、Token与模型选择 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Accessing the API](https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api)  /  3 min  /  The Five-Step Request Flow ；Why You Need a Server ；Making API Requests ；Inside Claude's Processing ；Tokenization ；Embedding ；Contextualization ；Generation ；When Claude Stops Generating ；The API Response ；Key Takeaways   /  building-with-the-claude-api__accessing-the-api（原本地资料引用，未随公开版收录）  /  |
| K03 提示、指令与Prompt Patterns | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [System prompts](https://academy.claude.com/courses/building-with-the-claude-api/system-prompts)  /  9 min  /  Why System Prompts Matter ；How System Prompts Work ；Seeing the Difference ；Building a Flexible Chat Function   /  building-with-the-claude-api__system-prompts（原本地资料引用，未随公开版收录）  /  |
| K05 Agent loop、ReAct与停止条件 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Multi-turn conversations with tools](https://academy.claude.com/courses/building-with-the-claude-api/multi-turn-conversations-with-tools)  /  10 min  /  The Multi-Turn Tool Pattern ；Building a Conversation Loop ；Refactoring Helper Functions ；Updating Message Handlers ；Updating the Chat Function ；Extracting Text from Messages ；Key Improvements   /  building-with-the-claude-api__multi-turn-conversations-with-tools（原本地资料引用，未随公开版收录）  /  |
| K06 工具定义、发现与实际调用 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Introducing tool use](https://academy.claude.com/courses/building-with-the-claude-api/introducing-tool-use)  /  2 min  /  The Problem Without Tools ；How Tool Use Works ；Weather Example in Practice ；Key Benefits   /  building-with-the-claude-api__introducing-tool-use（原本地资料引用，未随公开版收录）  /  |
| K07 结构化输出与参数校验 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Structured data](https://academy.claude.com/courses/building-with-the-claude-api/structured-data)  /  15 min  /  The Problem with Default Responses ；The Solution: Assistant Message Prefilling + Stop Sequences ；Processing the Response ；Beyond JSON   /  building-with-the-claude-api__structured-data（原本地资料引用，未随公开版收录）  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Implementing multiple turns](https://academy.claude.com/courses/building-with-the-claude-api/implementing-multiple-turns)  /  15 min  /  Detecting Tool Requests ；The Conversation Loop ；Handling Multiple Tool Calls ；Tool Result Blocks ；Error Handling ；Scalable Tool Routing ；Complete Workflow   /  building-with-the-claude-api__implementing-multiple-turns（原本地资料引用，未随公开版收录）  /  |
| K10 链式工作流、Query与意图路由 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Implementing multiple turns](https://academy.claude.com/courses/building-with-the-claude-api/implementing-multiple-turns)  /  15 min  /  Detecting Tool Requests ；The Conversation Loop ；Handling Multiple Tool Calls ；Tool Result Blocks ；Error Handling ；Scalable Tool Routing ；Complete Workflow   /  building-with-the-claude-api__implementing-multiple-turns（原本地资料引用，未随公开版收录）  /  |
| K14 并行、子图与Map-Reduce | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Parallelization workflows](https://academy.claude.com/courses/building-with-the-claude-api/parallelization-workflows)  /  3 min  /  The Problem with Complex Single Prompts ；A Better Approach: Parallelization ；How Parallelization Workflows Work ；Benefits of This Approach ；When to Use Parallelization   /  building-with-the-claude-api__parallelization-workflows（原本地资料引用，未随公开版收录）  /  |
| K15 短期记忆与会话历史 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Handling message blocks](https://academy.claude.com/courses/building-with-the-claude-api/handling-message-blocks)  /  7 min  /  Making Tool-Enabled API Calls ；Understanding Multi-Block Messages ；Managing Conversation History with Multi-Block Messages ；The Complete Tool Usage Flow ；Updating Helper Functions   /  building-with-the-claude-api__handling-message-blocks（原本地资料引用，未随公开版收录）  /  |
| K19 上下文选择、压缩、卸载与缓存 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Accessing the API](https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api)  /  3 min  /  The Five-Step Request Flow ；Why You Need a Server ；Making API Requests ；Inside Claude's Processing ；Tokenization ；Embedding ；Contextualization ；Generation ；When Claude Stops Generating ；The API Response ；Key Takeaways   /  building-with-the-claude-api__accessing-the-api（原本地资料引用，未随公开版收录）  /  |
| K20 文档加载、切分与摘要 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/building-with-the-claude-api/introducing-retrieval-augmented-generation)  /  5 min  /  The Problem with Large Documents ；Option 1: Include Everything in the Prompt ；Option 2: Break Documents into Chunks ；Benefits of RAG ；Challenges with RAG ；When to Use RAG   /  building-with-the-claude-api__introducing-retrieval-augmented-generation（原本地资料引用，未随公开版收录）  /  |
| K21 Embedding、向量库与索引 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Accessing the API](https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api)  /  3 min  /  The Five-Step Request Flow ；Why You Need a Server ；Making API Requests ；Inside Claude's Processing ；Tokenization ；Embedding ；Contextualization ；Generation ；When Claude Stops Generating ；The API Response ；Key Takeaways   /  building-with-the-claude-api__accessing-the-api（原本地资料引用，未随公开版收录）  /  |
| K22 混合检索、BM25、RRF与重排 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [BM25 lexical search](https://academy.claude.com/courses/building-with-the-claude-api/bm25-lexical-search)  /  5 min  /  The Problem with Semantic Search Alone ；Hybrid Search Strategy ；How BM25 Works ；Implementing BM25 Search ；Why This Works Better   /  building-with-the-claude-api__bm25-lexical-search（原本地资料引用，未随公开版收录）  /  |
| K23 Agentic RAG与检索工具 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/building-with-the-claude-api/introducing-retrieval-augmented-generation)  /  5 min  /  The Problem with Large Documents ；Option 1: Include Everything in the Prompt ；Option 2: Break Documents into Chunks ；Benefits of RAG ；Challenges with RAG ；When to Use RAG   /  building-with-the-claude-api__introducing-retrieval-augmented-generation（原本地资料引用，未随公开版收录）  /  |
| K24 多Agent角色、分工与通信 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Multi-Turn conversations](https://academy.claude.com/courses/building-with-the-claude-api/multi-turn-conversations)  /  6 min  /  The Problem with Stateless Conversations ；How Multi-Turn Conversations Work ；Building Helper Functions ；Putting It All Together   /  building-with-the-claude-api__multi-turn-conversations（原本地资料引用，未随公开版收录）  /  |
| K27 MCP客户端、服务器与原语 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Introducing MCP](https://academy.claude.com/courses/building-with-the-claude-api/introducing-mcp)  /  2 min  /  Understanding MCP Through a Real Example ；The Tool Function Problem ；How MCP Solves This ；Common Questions About MCP ；Who Authors MCP Servers? ；How is MCP Different from Direct API Calls? ；Isn't MCP Just Tool Use?   /  building-with-the-claude-api__introducing-mcp（原本地资料引用，未随公开版收录）  /  |
| K31 评测数据集、实验与版本对照 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [A typical eval workflow](https://academy.claude.com/courses/building-with-the-claude-api/a-typical-eval-workflow)  /  10 min  /  Step 1: Draft a Prompt ；Step 2: Create an Eval Dataset ；Step 3: Feed Through Claude ；Step 4: Feed Through a Grader ；Step 5: Change Prompt and Repeat ；Prompt Scoring   /  building-with-the-claude-api__a-typical-eval-workflow（原本地资料引用，未随公开版收录）  /  |
| K32 指标、Judge与任务基准 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Prompt evaluation](https://academy.claude.com/courses/building-with-the-claude-api/prompt-evaluation)  /  2 min  /  Prompt Engineering vs Prompt Evaluation ；Three Paths After Writing a Prompt ；Why Most Engineers Fall Into Testing Traps ；The Evaluation-First Approach   /  building-with-the-claude-api__prompt-evaluation（原本地资料引用，未随公开版收录）  /  |
| K33 错误归因、迭代与回归 | 1 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)：提示评测: 生成测试数据集、模型评分、代码评分与人工评分、迭代优化提示 |
| K34 成本、延迟与模型优化 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  building-with-the-claude-api  /  [Rules of prompt caching](https://academy.claude.com/courses/building-with-the-claude-api/rules-of-prompt-caching)  /  3 min  /  Cache Breakpoints ；How Cache Breakpoints Work ；Cross-Message Caching ；System Prompts and Tools ；Cache Ordering ；Minimum Content Length   /  building-with-the-claude-api__rules-of-prompt-caching（原本地资料引用，未随公开版收录）  /  |
| K43 多模态、视觉与环境输入 | 1 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)：检索与上下文: RAG与文档切分、Embedding与检索、BM25词法搜索、多索引与RRF、缓存及多模态内容 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)：MCP与应用集成: MCP概念与客户端、实现工具、资源和提示、Inspector调试、连接Claude应用与MCP服务、Claude Code开发流程 |
## Anthropic Introduction to Model Context Protocol

[官网](https://academy.claude.com/courses/introduction-to-model-context-protocol) · [课程笔记](../courses/anthropic_mcp_course/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K06 工具定义、发现与实际调用 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  introduction-to-model-context-protocol  /  [Introducing MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp)  /  2 min  /  The Problem MCP Solves ；How MCP Works ；MCP Servers Explained ；Common Questions ；Who authors MCP Servers? ；How is this different from calling APIs directly? ；Isn't MCP just the same as tool use?   /  introduction-to-model-context-protocol__introducing-mcp（原本地资料引用，未随公开版收录）  /  |
| K27 MCP客户端、服务器与原语 | 2 | [记录](../research/agent_courses/providers/anthropic/lesson_index.md)： /  introduction-to-model-context-protocol  /  [Introducing MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp)  /  2 min  /  The Problem MCP Solves ；How MCP Works ；MCP Servers Explained ；Common Questions ；Who authors MCP Servers? ；How is this different from calling APIs directly? ；Isn't MCP just the same as tool use?   /  introduction-to-model-context-protocol__introducing-mcp（原本地资料引用，未随公开版收录）  /  |
## OpenAI Building Agents 文档路线

[官网](https://developers.openai.com/tracks/building-agents) · [课程笔记](../courses/openai_building_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)：盘点日期：2026-10-03。本地完整正文的文件清单和获取状态见 source/web_manifest.json（原本地资料引用，未随公开版收录），静态阅读评价见 [analysis.md](analysis.md)，获取限制见 [evidence.md](evidence.md)。OpenAI 的“Building agents”是一张学习路线与延伸指南集合，不是有一组可完成章节/作业/证书的完整线上课程。 |
| K03 提示、指令与Prompt Patterns | 1 | [记录](../research/agent_courses/providers/openai/curriculum.md)：定义Agent: Quickstart、指令与模型、工具和专家Agent |
| K05 Agent loop、ReAct与停止条件 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  1. 认识概念与选择抽象层  /  [Building agents track](https://developers.openai.com/tracks/building-agents)、[Agents overview](https://developers.openai.com/api/docs/guides/agents)、[Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk)  /  明白 agent 定义、Responses API 和 Agents SDK 分别承担什么；确定要显式管理 loop 还是采用 SDK runner  /  |
| K06 工具定义、发现与实际调用 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  2. 建立最小 Agent  /  [Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)、[Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)  /  定义 instructions/model/tools；创建 History tutor 并调用简单函数工具  /  |
| K08 执行反馈、异常与重试 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)  /  run loop、多轮 session、continuation、streaming 与异常/暂停处理  /  |
| K10 链式工作流、Query与意图路由 | 1 | [记录](../research/agent_courses/providers/openai/curriculum.md)：观测、评估与模型: 运行轨迹、工作流评估、模型与服务商选择 |
| K15 短期记忆与会话历史 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  2. 建立最小 Agent  /  [Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)、[Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)  /  定义 instructions/model/tools；创建 History tutor 并调用简单函数工具  /  |
| K17 Checkpoint、持久化与恢复 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  5. 处理边界与人工介入  /  [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)  /  比较 input/output/tool guardrail 的位置，添加副作用前审批并从暂停状态恢复  /  |
| K18 人工介入、批准与交接 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  5. 处理边界与人工介入  /  [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)  /  比较 input/output/tool guardrail 的位置，添加副作用前审批并从暂停状态恢复  /  |
| K24 多Agent角色、分工与通信 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  3. 看清运行时  /  [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)、[Results and state](https://developers.openai.com/api/docs/guides/agents/results)  /  了解 runner loop、run result、multi-turn session、continuation、stream 和 interruption  /  |
| K25 Handoff、Agent-as-tool与委派 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  4. 拆分专家与决定责任归属  /  [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)  /  判断 specialist 应接管用户对话，还是由 manager 把 specialist 当子能力调用  /  |
| K30 Trace、Span与运行可观测性 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  6. 观察和评估运行过程  /  [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability)、[Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)  /  检查完整 trace，并评估最终产物和 agent 轨迹  /  |
| K31 评测数据集、实验与版本对照 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  [Building agents track](https://developers.openai.com/tracks/building-agents)  /  Agent 定义、模型和构建方式选择、工具、编排、评测与路线链接  /  |
| K32 指标、Judge与任务基准 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  6. 观察和评估运行过程  /  [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability)、[Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)  /  检查完整 trace，并评估最终产物和 agent 轨迹  /  |
| K33 错误归因、迭代与回归 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)  /  Trace grading、评测器与回归检查  /  |
| K34 成本、延迟与模型优化 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  7. 根据目标选择模型与供应商  /  [Models and providers](https://developers.openai.com/api/docs/guides/agents/models)  /  按任务、延迟、成本和接口支持比较模型/Provider；版本选择需用当前官方页面核对  /  |
| K37 授权、Guardrails与操作边界 | 2 | [记录](../research/agent_courses/providers/openai/curriculum.md)： /  5. 处理边界与人工介入  /  [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)  /  比较 input/output/tool guardrail 的位置，添加副作用前审批并从暂停状态恢复  /  |
## LangChain Academy：Introduction to Deep Agents

[官网](https://academy.langchain.com/courses/foundation-introduction-to-deepagents) · [课程笔记](../courses/langchain_deep_agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K09 文件、代码执行与沙箱 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：执行环境: 文件系统、沙箱 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：上下文管理: 摘要、上下文卸载、记忆 |
| K18 人工介入、批准与交接 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：Agent构建: Agent构建、MCP、状态保存、人工介入 |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：上下文管理: 摘要、上下文卸载、记忆 |
| K25 Handoff、Agent-as-tool与委派 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：任务委派: Skills、子Agent |
| K26 Skills与可复用能力 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：任务委派: Skills、子Agent |
| K27 MCP客户端、服务器与原语 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：Agent构建: Agent构建、MCP、状态保存、人工介入 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：综合项目: 销售助手、本地部署 |
| K40 本地模型、本地Agent与混合运行 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：综合项目: 销售助手、本地部署 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：综合项目: 销售助手、本地部署 |
## LangChain Academy：Introduction to Agent Observability & Evaluations

[官网](https://academy.langchain.com/courses/intro-to-langsmith) · [课程笔记](../courses/langchain_observability_evaluations/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K03 提示、指令与Prompt Patterns | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：提示词开发: 提示词开发、版本比较 |
| K30 Trace、Span与运行可观测性 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：运行观测: 运行追踪、失败定位 |
| K31 评测数据集、实验与版本对照 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：测试与评估: 数据集、评估器、实验结果 |
| K33 错误归因、迭代与回归 | 1 | [记录](../research/agent_courses/additional_framework_university_courses.md)：运行观测: 运行追踪、失败定位 |
## Hugging Face MCP Course

[官网](https://huggingface.co/learn/mcp-course/en/unit0/introduction) · [课程笔记](../courses/huggingface-mcp/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K27 MCP客户端、服务器与原语 | 1 | [记录](../research/agent_courses/providers/extras/analysis.md)：协议基础: 课程导览、MCP术语与架构、通信与协议能力、SDK、客户端与服务端、单元测验 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/providers/extras/analysis.md)：应用集成: Gradio服务与客户端、Continue客户端、Tiny Agents、本地加速路线 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/providers/extras/analysis.md)：应用集成: Gradio服务与客户端、Continue客户端、Tiny Agents、本地加速路线 |
## NVIDIA DLI：Building RAG Agents with LLMs

[官网](https://www.nvidia.com/en-au/training/instructor-led-workshops/building-rag-agents-with-llms/) · [课程笔记](../courses/nvidia-building-rag-agents/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K02 LLM、消息、Token与模型选择 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：模型与应用服务: LLM推理接口、LangChain与LCEL、Gradio与LangServe |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：对话与知识处理: 对话状态与slot filling、长文切分与摘要、Embedding与输入护栏 |
| K20 文档加载、切分与摘要 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：对话与知识处理: 对话状态与slot filling、长文切分与摘要、Embedding与输入护栏 |
| K21 Embedding、向量库与索引 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：对话与知识处理: 对话状态与slot filling、长文切分与摘要、Embedding与输入护栏 |
| K23 Agentic RAG与检索工具 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：检索与评测: 向量数据库RAG、LLM-as-a-Judge评测、研究论文集问答RAG Agent |
| K29 框架抽象、手写框架与选型 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：模型与应用服务: LLM推理接口、LangChain与LCEL、Gradio与LangServe |
| K32 指标、Judge与任务基准 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：检索与评测: 向量数据库RAG、LLM-as-a-Judge评测、研究论文集问答RAG Agent |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：模型与应用服务: LLM推理接口、LangChain与LCEL、Gradio与LangServe |
| K37 授权、Guardrails与操作边界 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：对话与知识处理: 对话状态与slot filling、长文切分与摘要、Embedding与输入护栏 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：模型与应用服务: LLM推理接口、LangChain与LCEL、Gradio与LangServe |
## NVIDIA DLI：Building Agentic AI Applications with LLMs

[官网](https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/) · [课程笔记](../courses/nvidia-building-agentic-ai-applications/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K13 图编排、节点、边与状态Schema | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：已核实的课程简介: 使用LangGraph构建Agent、集成NVIDIA NIM、长程推理、内容管理、实时操作型Agent |
## IBM：Agentic AI in Practice

[官网](https://www.ibm.com/training/learning-path/agentic-ai-in-practice-1058) · [课程笔记](../courses/ibm-agentic-ai-in-practice/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：基础与框架: Agent基础、CrewAI与LangChain |
| K05 Agent loop、ReAct与停止条件 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：工具与推理: 自定义工具、数学助手工具调用、ReAct Agent |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：工具与推理: 自定义工具、数学助手工具调用、ReAct Agent |
| K10 链式工作流、Query与意图路由 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：工作流: LangGraph工作流与模式 |
| K13 图编排、节点、边与状态Schema | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：工作流: LangGraph工作流与模式 |
| K23 Agentic RAG与检索工具 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：领域应用: CrewAI与Gradio多Agent、医疗AG2/AutoGen、PydanticAI客服Agent、LangGraph与Docling Agentic RAG |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：基础与框架: Agent基础、CrewAI与LangChain |
| K29 框架抽象、手写框架与选型 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：基础与框架: Agent基础、CrewAI与LangChain |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：领域应用: CrewAI与Gradio多Agent、医疗AG2/AutoGen、PydanticAI客服Agent、LangGraph与Docling Agentic RAG |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_vendor_courses.md)：工具与推理: 自定义工具、数学助手工具调用、ReAct Agent |
## DeepLearning.AI：AI Agents in LangGraph

[官网](https://www.deeplearning.ai/courses/ai-agents-in-langgraph) · [课程笔记](../courses/dlai-ai-agents-in-langgraph/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K13 图编排、节点、边与状态Schema | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：Agent与图流程: 从Python和LLM构建Agent、LangGraph组件、Agentic Search |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：状态与交互控制: 跨会话持久化与恢复、流式输出、人机协作 |
| K17 Checkpoint、持久化与恢复 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：状态与交互控制: 跨会话持久化与恢复、流式输出、人机协作 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：综合项目: Essay Writer研究与写作流程 |
## DeepLearning.AI：Multi AI Agent Systems with crewAI

[官网](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai) · [课程笔记](../courses/dlai-multi-ai-agent-systems-crewai/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：角色与协作: Agent角色、目标与工具、多Agent分工协作、顺序、并行与层级流程 |
| K08 执行反馈、异常与重试 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：记忆与可靠性: 短期、长期与共享记忆、错误处理与护栏 |
| K14 并行、子图与Map-Reduce | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：角色与协作: Agent角色、目标与工具、多Agent分工协作、顺序、并行与层级流程 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：记忆与可靠性: 短期、长期与共享记忆、错误处理与护栏 |
| K16 长期、共享与分层记忆 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：记忆与可靠性: 短期、长期与共享记忆、错误处理与护栏 |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：角色与协作: Agent角色、目标与工具、多Agent分工协作、顺序、并行与层级流程 |
| K37 授权、Guardrails与操作边界 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：记忆与可靠性: 短期、长期与共享记忆、错误处理与护栏 |
## DeepLearning.AI：Building Coding Agents with Tool Execution

[官网](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution) · [课程笔记](../courses/dlai-building-coding-agents-tool-execution/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K05 Agent loop、ReAct与停止条件 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：代码执行循环: 生成并执行Python代码、读取错误并继续尝试、文件管理 |
| K08 执行反馈、异常与重试 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：代码执行循环: 生成并执行Python代码、读取错误并继续尝试、文件管理 |
| K09 文件、代码执行与沙箱 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：代码执行循环: 生成并执行Python代码、读取错误并继续尝试、文件管理 |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：项目实践: Pandas分析CSV并用Gradio问答、沙箱中编辑多文件并生成Next.js应用、用运行时摘要管理长上下文 |
| K35 服务部署、UI/API集成与交付 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：项目实践: Pandas分析CSV并用Gradio问答、沙箱中编辑多文件并生成Next.js应用、用运行时摘要管理长上下文 |
| K41 Coding Agent与开发Harness | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：项目实践: Pandas分析CSV并用Gradio问答、沙箱中编辑多文件并生成Next.js应用、用运行时摘要管理长上下文 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)：项目实践: Pandas分析CSV并用Gradio问答、沙箱中编辑多文件并生成Next.js应用、用运行时摘要管理长上下文 |
## Berkeley：LLM Agents Fall 2024

[官网](https://rdi.berkeley.edu/llm-agents-mooc/f24) · [课程笔记](../courses/berkeley-llm-agents-fall-2024/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：推理与Agent基础: LLM推理、Agent历史与概览、ReAct与WebShop、AutoGen框架与多模态知识助手 |
| K05 Agent loop、ReAct与停止条件 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：推理与Agent基础: LLM推理、Agent历史与概览、ReAct与WebShop、AutoGen框架与多模态知识助手 |
| K11 任务分解、规划与重规划 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：规划、具身与评测: 神经符号决策与规划、GR00T与机器人Agent、开源、科学与能力评测、Agent安全、政策与可信证据 |
| K23 Agentic RAG与检索工具 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：企业与开发工作流: Grounding与RAG、Compound AI Systems与DSPy、软件开发Agent：SWE-agent与OpenHands、WorkArena与TapeAgents |
| K24 多Agent角色、分工与通信 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：推理与Agent基础: LLM推理、Agent历史与概览、ReAct与WebShop、AutoGen框架与多模态知识助手 |
| K29 框架抽象、手写框架与选型 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：推理与Agent基础: LLM推理、Agent历史与概览、ReAct与WebShop、AutoGen框架与多模态知识助手 |
| K37 授权、Guardrails与操作边界 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：规划、具身与评测: 神经符号决策与规划、GR00T与机器人Agent、开源、科学与能力评测、Agent安全、政策与可信证据 |
| K38 不可信输入、注入与数据安全 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：规划、具身与评测: 神经符号决策与规划、GR00T与机器人Agent、开源、科学与能力评测、Agent安全、政策与可信证据 |
| K41 Coding Agent与开发Harness | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：企业与开发工作流: Grounding与RAG、Compound AI Systems与DSPy、软件开发Agent：SWE-agent与OpenHands、WorkArena与TapeAgents |
| K43 多模态、视觉与环境输入 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：推理与Agent基础: LLM推理、Agent历史与概览、ReAct与WebShop、AutoGen框架与多模态知识助手 |
| K46 研究论文、能力基准与研究方法 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：规划、具身与评测: 神经符号决策与规划、GR00T与机器人Agent、开源、科学与能力评测、Agent安全、政策与可信证据 |
| K47 游戏、具身与机器人Agent | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：规划、具身与评测: 神经符号决策与规划、GR00T与机器人Agent、开源、科学与能力评测、Agent安全、政策与可信证据 |
## Berkeley：LLM Agents Spring 2025

[官网](https://rdi.berkeley.edu/llm-agents-mooc/sp25) · [课程笔记](../courses/berkeley-llm-agents-spring-2025/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：课程主题（页面级）: 大型语言模型Agent专题、未核实该学期逐讲顺序与项目细节 |
## Berkeley：Agentic AI Fall 2025

[官网](https://rdi.berkeley.edu/agentic-ai/f25) · [课程笔记](../courses/berkeley-agentic-ai-fall-2025/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/providers/berkeley/curriculum.md)：课程主题（页面级）: Agentic AI专题、未核实该学期逐讲顺序与项目细节 |
## CMU 11-768：AI Agents Fall 2026

[官网](https://www.cmu-agents.com/) · [课程笔记](../courses/cmu-11768-ai-agents-fall-2026/README.md)

| 点 | 等级 | 研究记录中的定位依据 |
|---|---|---|
| K01 Agent、Workflow与自主程度 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K06 工具定义、发现与实际调用 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K11 任务分解、规划与重规划 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K15 短期记忆与会话历史 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K19 上下文选择、压缩、卸载与缓存 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K31 评测数据集、实验与版本对照 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：工程作业: 构建Coding Agent harness、设计Agent评测框架、实现Agent训练方法 |
| K38 不可信输入、注入与数据安全 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K41 Coding Agent与开发Harness | 1 | [记录](../research/agent_courses/additional_open_courses.md)：工程作业: 构建Coding Agent harness、设计Agent评测框架、实现Agent训练方法 |
| K44 端到端应用与综合项目 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：研究实践: 学期研究项目 |
| K45 SFT、LoRA与Agentic RL | 1 | [记录](../research/agent_courses/additional_open_courses.md)：Agent核心主题: 工具使用、长上下文管理、规划、记忆、Agent训练、安全与人机交互 |
| K46 研究论文、能力基准与研究方法 | 1 | [记录](../research/agent_courses/additional_open_courses.md)：研究实践: 学期研究项目 |