# Agent 教材比较：按学习任务搭配，不做统一名次

本研究基于公开文字与代码静态审阅。具体章节、版本、获取限制见各档案。未测试新手完成率、教学视频体验或真实API费用，不给无依据的量化评分。

## 首先分清教材类型

| 类型 | 本轮材料 | 适合解决的问题 | 局限 |
|---|---|---|---|
| 中文连续教材/项目 | Datawhale Hello-Agents | 用中文建立概念和项目脉络 | 仍需语言基础；每个项目环境与模型接入要核对。 |
| 基础加框架比较课 | HF Agents Course | 看清loop，再比较smolagents/LlamaIndex/LangGraph | 生产权限、容量及恢复不是完整主线。 |
| 模式加平台实践 | Microsoft AI Agents for Beginners | 工具、RAG、记忆、协议、部署、安全路线 | 云平台前提较重；知识点很多，需要按目标分流。 |
| 模型平台连续课程 | Anthropic Academy | API、工具、评测、RAG、workflow/agent、MCP与Skills | 教学实现以自身生态为主；代码片段不全是独立程序。 |
| 官方SDK/工程参考 | OpenAI Agent/SDK说明；Anthropic SDK/文章 | 对具体接口、控制权、批准、trace和harness查证 | 文档导航缺统一作业节奏；文章不能代替所有基础知识。 |
| 单框架编排课 | LangChain Academy / LangGraph | 状态、分支、持久化、中断等编排实现 | 熟悉框架不代表完成全部Agent基础和生产设计。 |
| 专题教学课 | DeepLearning.AI Agentic AI等 | 以模式和项目建立可动手的理解 | 公开获取范围、账号与收费边界应分别记录。 |
| 研究讲座课程 | Berkeley Agent MOOC | 看研究和产业问题的广度、形成论文方向 | 不适合作为完全新手唯一的逐步编程教材。 |

“权威”可以指接口定义可靠；“好教材”还要求起点、依赖、例子、练习、反馈和连贯性。两者应分别评价。

Datawhale当前主教材16章，主线从基础、手写模式、框架进入Memory/RAG、context、协议、训练与评测，再看旅行/深度研究/小镇项目。跨度大，适合获得中文全景；其中Agentic RL不是每个应用开发者的必修前提。部分章节调用外部发布的`hello_agents`包，教材仓库里的调用示例不能代替该依赖底层源码审计。详见[Datawhale分析](providers/datawhale/analysis.md)。

## 已有证据最清楚的几项比较

### 1. 最小loop解释

HF Unit1有工具、动作、观察与手写loop，能让人看到模型输出与真实执行的边界。Anthropic Platform101用天气工具解释循环，API课进一步解释schema与返回。OpenAI SDK quickstart更快进入可组合接口，但一些循环细节由SDK承担。

因此想知道“为什么工具没有真的执行”，先看前两者；想迅速建立SDK原型，可同时看quickstart。详细证据见[HF分析](providers/huggingface/analysis.md)、[Anthropic分析](providers/anthropic/analysis.md)、[OpenAI分析](providers/openai/analysis.md)。

### 2. 体系的宽度与连贯性

HF先基础、后三框架、再共同应用/评测，结构容易看懂，但框架章节对前提要求上升。微软当前18课拓展到浏览器、生产部署、本地Agent和安全；STUDY_GUIDE有按目标分流，比让新手平均精读所有章节更合理。

Anthropic当前三套公开文字课共90节，覆盖的不是只有聊天API，还包括工具、检索、评测、MCP与Agent工作流。OpenAI学习track有结构，但主要链接文档，统一作业与毕业项目不如课程形式清楚。以上评价不是课数越多越好，而是看章节间如何组成任务链。

### 3. 与原面经的关系

原面经里的query、routing、Tool/Skill、编排等可在上述材料中找到明确入口。harness、写操作批准、状态恢复需要把课程与SDK/工程文章组合起来。SQLite选型、数据库原理、并发容量、Java基础不能由Agent入门材料包办。

最适合视频解释的不是“这套课覆盖了百分之多少真题”，而是“这题的概念在哪一章、这章没有教完什么、我怎么做一个练习验证”。详见[面经映射](interview_alignment.md)。

### 4. 实践材料与实际可运行性

LangGraph课程把checkpoint、人工中断、并行/子图、跨会话Store及服务部署分模块展开。其SQLite持久化示范与后续Postgres/Redis部署样例可以对照阅读；同一thread的新输入也有reject/enqueue/interrupt/rollback等处理例子。这些提供具体架构入口，但并未代替真实负载和故障恢复验证。详见[LangChain课程分析](providers/langchain/analysis.md)。

公开仓库和notebook便于看实现；但教学mock、占位代码、未固定依赖、云账号及模型接口变化会影响复现。代码在课程里出现并不等于我们已验证可运行。本轮只报告静态观察；后续真实体验应按[审阅模板](learning_experience_audit.md)记录。

### 5. 术语解释是否完整

HF对基本loop和框架构件解释细；Anthropic对Skills、工具和context有较明确入口；微软后期章节更重视实际操作边界与部署。没有一套材料独占所有名词。

还要分清通用技术词与生态词：query、JSON Schema、BM25、事务早已存在；Skill和特定SDK中的Session/Runner要依平台定义；“重构编排层”是架构工作描述。见[术语表](glossary.md)。

## 按你的起点选组合

| 当前起点 | 主线候选 | 少量补充 | 第一个可验证成果 |
|---|---|---|---|
| 会Python，但Agent词汇陌生 | Datawhale中文教材或HF Unit1 | glossary + 官方工具/loop说明 | 一次真实工具执行与一次非法参数拒绝。 |
| 已经接过模型API，想组织项目 | HF Unit2/3或LangGraph课程 | 官方SDK orchestration + routing例子 | 同一请求的两条分支与错误回退。 |
| 想看中文体系再查原始接口 | Datawhale作主线 | Anthropic/OpenAI具体文档 | 把教程架构画到真实接口并核对控制权。 |
| 想做客服/知识库应用 | API课程工具/RAG/评测 + HF案例 | 微软15/16/18的权限与部署 | 缺参数追问、检索引用、退款批准。 |
| 想研究Coding Agent/Harness | Anthropic SDK与长任务文章 | 图式状态/恢复 + evals | 文件任务的预算、checkpoint和批准记录。 |
| 已有后端经验，关注生产 | 微软14/16/18 + 各SDK | 数据库、身份、队列与容量知识 | 可解释的故障恢复与权限负例。 |
| 想读研究论文 | Berkeley讲座及相关论文 | 先补基础loop和实验方法 | 一份问题/基线/指标/局限的论文笔记。 |

这是研究者的路线建议，没有经过真实班级的学习效果比较。主线选一门，其他材料按具体问题补查，避免同时承担全部课程作业。

## 建议用于综述的比较维度

每门材料都讲这六件事即可形成公平的目录：它面对谁；章节如何衔接；第一段代码做什么；最清楚地解释哪个词；哪条面经能找到入口；最重要的缺口是什么。具体素材放provider档案，不用把90课或所有章节塞进视频。
