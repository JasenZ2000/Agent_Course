# Microsoft AI Agents for Beginners：逐课正文、代码与作业地图

研究日期：2026-10-03（Asia/Shanghai）  
上游仓库：[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)  
本地源码：`source/`（原本地资料引用，未随公开版收录）；固定提交：[`25b7985f3b2dc37a84f4a7387ccd3c9f0e5b1595`](https://github.com/microsoft/ai-agents-for-beginners/tree/25b7985f3b2dc37a84f4a7387ccd3c9f0e5b1595)

## 1. 课程现在是什么

当前 README 标题是“18 Lessons to Get Started Building AI Agents”，实际仓库包含 `00-course-setup` 加 `01`–`18`。2026 年 7 月课程完成了一次大迁移：从 GitHub Models/旧 API 转向 Microsoft Agent Framework（MAF）和 Azure OpenAI Responses API，并新增可扩展部署、本地 Agent 与安全收据章节。最新代码把 `agent-framework-core` 固定为 `1.10.0`，Foundry/OpenAI integrations 固定在 `~1.10.0`，主模型示例换成 `gpt-5-mini`。证据见 `CHANGELOG.md`（原本地资料引用，未随公开版收录）、`requirements.txt`（原本地资料引用，未随公开版收录） 和 [当前 README](https://github.com/microsoft/ai-agents-for-beginners)。

课程有一份很有用的 `STUDY_GUIDE.md`（原本地资料引用，未随公开版收录）：建议新手按 01–06 学，之后根据 tools、RAG、workflow、production、local 等目标分流，并贯穿一个“课程助理 Agent”小项目。它比主 README 的课程表更能解释各课如何组合。

## 2. 逐课正文、代码与练习

| 课次 | 正文范围 | 代码/作业 | 面经关联与阅读重点 |
|---|---|---|---|
| 00 Course Setup | 浅克隆/稀疏克隆、Codespaces；Python 3.12+、可选 .NET 10+、Azure CLI；Foundry hub/project/model；`az login` 无密钥认证；`.env`；Azure AI Search；Azure OpenAI；MiniMax、Novita、Foundry Local；Bing connection。 | 安装 `requirements.txt`（原本地资料引用，未随公开版收录），创建 Foundry 项目与模型部署；未要求执行付费 API。 | 先分清“公开教材免费”和“运行主路径需要 Azure subscription/模型资源”。正文：`00-course-setup/README.md`（原本地资料引用，未随公开版收录）。 |
| 01 Intro to AI Agents | Agent 定义、类型、适用/不适用场景；direct response、tool call、memory、planning 等基础组件；agentic pattern 与 framework。 | Python notebook、.NET 示例；可部署后用 smoke test。没有正式作业。 | 为 `loop/tool/context` 建词汇，但不如 HF Unit 1 那样逐 token 拆 loop。正文：`01-intro-to-ai-agents/README.md`（原本地资料引用，未随公开版收录）。 |
| 02 Explore Agentic Frameworks | 框架为何提供模型、工具、状态、协作与实时反馈；区分 MAF（客户端 framework）与 Microsoft Foundry Agent Service（托管服务）；比较两种使用场景。 | 两个 Python notebook（Foundry 与 Azure OpenAI）和 .NET 示例。 | 对“框架和托管 Agent 服务有什么区别”给出可面试的结构；也为 Harness/运行时拆层。正文：`02-explore-agentic-frameworks/README.md`（原本地资料引用，未随公开版收录）。 |
| 03 Agentic Design Patterns | Agent Space/Time/Core 三个设计维度；将复杂旅行 Agent 拆成角色、步骤、能力与用户旅程。 | Python/.NET 旅行示例；无评分作业。 | 更偏产品/架构草图，具体失败恢复和权限还没有进入。正文：`03-agentic-design-patterns/README.md`（原本地资料引用，未随公开版收录）。 |
| 04 Tool Use | 工具模式、function/tool schema、执行逻辑、路由、消息处理、validation/error handling、state；Responses API function calling；MAF 与 Foundry toolset；SQLite 查询和 Code Interpreter；SQL 应配置只读角色。 | Python notebook、.NET 代码；SQLite tool 例子；可部署后 smoke test。 | 直接对应工具 schema、意图选工具、参数校验和 SQLite 权限。正文：`04-tool-use/README.md`（原本地资料引用，未随公开版收录）。 |
| 05 Agentic RAG | 区分传统 RAG 与 Agentic RAG；Agent 拥有查询重写、迭代检索、多工具、memory/self-correction；列失败模式、agency 边界、governance。 | Python/.NET notebook，默认可用内存知识库，可选 Azure AI Search；可部署后 smoke test。 | 适合回答“为什么 RAG 要 Agent 化”，但 chunk/召回/重排评测深度有限。正文：`05-agentic-rag/README.md`（原本地资料引用，未随公开版收录）。 |
| 06 Trustworthy Agents | system message framework；任务/指令攻击、关键系统访问、资源过载、知识库投毒、级联错误；input filters、turn limits、limited environment、fallback/retry；human-in-the-loop。 | 两个 notebook：system message 与 pre-action approval/risk tier/audit log。 | 对写操作边界和人工审批建立第一层机制；风险分级细节主要在 notebook，不只在 README。正文：`06-building-trustworthy-agents/README.md`（原本地资料引用，未随公开版收录）。 |
| 07 Planning Design | 目标分解、structured output、Pydantic subtask model；planner 与多个执行 Agent；iterative planning/re-plan。 | Python/.NET 旅行规划示例。 | 对任务分解与结构化计划强；没有 durable checkpoint 或 crash resume。正文：`07-planning-design/README.md`（原本地资料引用，未随公开版收录）。 |
| 08 Multi-Agent | 何时需要多 Agent；specialization、scalability、fault tolerance；communication、coordination、visibility、HITL；group chat、handoff、collaborative filtering；refund process。 | 多个 Python/.NET workflow notebook，覆盖 basic/sequential/concurrent/conditional；作业要求设计 customer support 多 Agent，附 solution 和 2 题 knowledge check。 | 与“单 Agent 还是多 Agent、怎么路由、怎么观测”高度对应。正文：`08-multi-agent/README.md`（原本地资料引用，未随公开版收录）。 |
| 09 Metacognition | 课程最长正文（1434 行）：self-reflection、planning、corrective RAG、pre-emptive context、goal bootstrap、LLM rerank/relevance、intent-aware search、code-as-tool、环境感知、SQL-as-RAG、反思后调整策略。 | 单个 Python notebook；README 内含大量可复制 Python 片段。 | 覆盖 query/intent、rerank、SQL、反思；内容广但松散，动态 SQL 例子用字符串拼接，不是生产 SQL 安全模板。正文：`09-metacognition/README.md`（原本地资料引用，未随公开版收录）。 |
| 10 Agents in Production | traces/spans；生产观测价值；latency、cost、request errors、显式/隐式反馈、accuracy、automated eval；OpenTelemetry；offline/online eval 闭环；连续 loop、multi-agent 不稳定、fallback、模型路由、cache。 | 费用报销 observability/eval notebook；没有独立作业。 | 与 `eval/model consistency/production` 强相关；强调 offline eval 是上线前最低门槛。正文：`10-ai-agents-production/README.md`（原本地资料引用，未随公开版收录）。 |
| 11 Agentic Protocols | MCP 的 host/client/server/tools/resources/prompts；A2A 的 Agent Card/Executor/Artifact/Event Queue；NLWeb 和 MCP endpoint。 | MCP、A2A notebooks；GitHub MCP + Chainlit app/配置文件；mcp-agents 示例。 | 能讲协议角色，不等于已解决鉴权、租户隔离或工具信任。正文：`11-agentic-protocols/README.md`（原本地资料引用，未随公开版收录）。 |
| 12 Context Engineering | prompt vs context；system/user/tool/retrieved/memory 等 context 类型；write/select/compress/isolate；scratchpad、summarization、sub-agent isolation；context poisoning、distraction、confusion、clash。 | chat summarization notebook、vacation-agent scratchpad。 | 对 context 面经最直接；没有用固定长任务测摘要漂移和恢复。正文：`12-context-engineering/README.md`（原本地资料引用，未随公开版收录）。 |
| 13 Agent Memory | working、short-term、long-term、persona、episodic/workflow、entity、structured RAG memory；Mem0、Cognee、RAG storage；memory optimization/self-improve。 | 两个 notebook：MAF memory 与 Cognee。 | 分类较完整；隐私、遗忘、污染检测、版本和并发写冲突仍浅。正文：`13-agent-memory/README.md`（原本地资料引用，未随公开版收录）。 |
| 14 Microsoft Agent Framework | Agent/thread/message、thread serialize/deserialize、自定义 message store、Mem0；workflow sequential/concurrent/conditional/handoff/HITL/middleware；把 LangChain/LangGraph Agent 托管到 Foundry `/responses`。 | 7 个 notebooks + `hotel_booking_workflow_sample.py` + `14-langchain-hosted-agent.py`。 | 最接近 Harness/编排实作核心；能展示 state persistence 和 middleware，但主路径仍绑定 MAF/Foundry。正文：`14-microsoft-agent-framework/README.md`（原本地资料引用，未随公开版收录）。 |
| 15 Computer Use Agents | Browser-Use、Playwright/CDP、vision、Pydantic extraction；Agent 与 actor 的取舍；页面不可信；域名/动作/时间预算；观察与动作分离；登录、发信、购买、删除、改设置前显式审批；遇模糊状态停止。 | Airbnb 搜索 notebook；5 题 knowledge check；Project Opal 案例把 Skills 描述为可复用 `.md` 指令。 | 这套课对“模糊问题/写操作边界”最具体的一课。正文：`15-browser-use/README.md`（原本地资料引用，未随公开版收录）。 |
| 16 Deploying Scalable Agents | prototype vs production；client-hosted/Hosted Agent/workflow；生命周期和 eval release gate；stateless、external state、model routing、cache、bounded concurrency；OTel；成本；RBAC、HITL、MCP、network/private endpoints；smoke tests。 | 一个 production customer-support notebook；8 题 knowledge check；作业增加 refund tool + approval，测 routing/cache 计数并解释真实流量验证；部署后 smoke test。 | 课程生产化核心，对 scaling、身份、状态、失败、成本和质量形成完整框架。正文：`16-deploying-scalable-agents/README.md`（原本地资料引用，未随公开版收录）。 |
| 17 Creating Local Agents | SLM 适用场景；Foundry Local + Qwen function calling；local tools、Chroma local RAG、local MCP；cloud/local hybrid。 | local engineering assistant notebook；knowledge check；作业给 assistant 增工具/检索；challenge 设计 hybrid routing。 | 提供无云/离线替代，但需要本机硬件和模型下载；不具备云 Responses API 全部状态能力。正文：`17-creating-local-ai-agents/README.md`（原本地资料引用，未随公开版收录）。 |
| 18 Securing Agents | Ed25519 + JCS 的 tool-call cryptographic receipt；hash args/result；verify tampering；链式 receipt；明确“证明了什么/没证明什么”；human approval receipt 绑定同一 canonical action、policy version、key registry 与 expiry。 | 两个 notebook、sample receipts；5 题 knowledge check；4 节 practice；两个 stretch challenges；production checklist。 | 对高风险写操作、审计和人类批准给出课程中最严格的证据模型；但 receipt 不能替代输入验证、policy 或身份基础设施。正文：`18-securing-ai-agents/README.md`（原本地资料引用，未随公开版收录）。 |

## 3. Study Guide 给出的学习路径

`STUDY_GUIDE.md`（原本地资料引用，未随公开版收录） 建议第一次接触者顺序完成 01–06，再按目标选择：

- Tool Agent：04 → 05/07/14
- RAG：05 → 04/06/12
- workflow：07 → 08/09/14
- multi-agent：08 → 07/09/11
- production：06/10 → 12/13/16/18
- local/offline：17 → 04/05/11
- protocol/browser：11/15 → 10/18

它还提供一个课程助理 capstone：检索仓库课程、给 citation、规划阅读顺序、建议练习、保留偏好、记录 trace/approval。这个项目足以串起 tool、RAG、planning、context、memory、observability、trust，但课程没有替学生提供完整评分 rubric；需要自己定义成功率、轨迹约束、成本和坏例回归。

## 4. 作业与验证密度

- 01–07 主要是正文 + notebook，正式作业稀少。
- 08 有明确 multi-agent 设计作业和答案。
- 10 的 notebook 是生产观测实践，但 README 没有独立交付标准。
- 15 有 knowledge check，最重要的实践是设计“先观察、后审批动作”的边界。
- 16、17 有 knowledge check + assignment；16 还要求 routing/cache 计数与真实流量验证说明。
- 18 有 knowledge check、分段练习、篡改测试和 stretch challenge，作业设计最扎实。
- `tests/`（原本地资料引用，未随公开版收录） 只有 01、04、05、16 的部署 smoke-test catalogs；它证明仓库提供“部署是否应答”的第一道门，不代表 18 课都有自动回归，也不代表输出质量已经验证。

## 5. 视频范围

主 README 写“每课有文字、短视频、代码”，但课程表只有 01–13 有 YouTube 链接，14–18 的 Video 列为空。本地检索到 13 个 YouTube 链接。本研究没有逐个观看、下载或转录这些视频；课程分析基于 README、STUDY_GUIDE、每课正文、notebook/代码和测试配置。

