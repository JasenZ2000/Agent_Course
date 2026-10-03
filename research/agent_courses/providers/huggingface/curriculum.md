# Hugging Face Agents Course：逐章正文与练习地图

研究日期：2026-10-03（Asia/Shanghai）  
课程主页：[英文](https://huggingface.co/learn/agents-course/unit0/introduction)｜[简体中文](https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction)  
本地源码：`source/`（原本地资料引用，未随公开版收录）；固定提交：[`b3946b1d09d29c65736e219d48a8a736a2c52154`](https://github.com/huggingface/agents-course/tree/b3946b1d09d29c65736e219d48a8a736a2c52154)

## 1. 课程主线

课程不是一套单框架速成教程。它先建立 Agent、LLM、消息、工具和 Thought–Action–Observation 循环，再分别讲 `smolagents`、LlamaIndex、LangGraph，随后用同一个晚宴助理案例做 Agentic RAG，最后以 GAIA 子集作公开评测。三个附加单元补函数调用微调、可观测性/评测和游戏 Agent。

英文目录以 `units/en/_toctree.yml`（原本地资料引用，未随公开版收录） 为准；中文目录以 `units/zh-CN/_toctree.yml`（原本地资料引用，未随公开版收录） 为准。两者的主课章节齐全，但中文欢迎页存在过期信息，不能把中文页当作课程政策的唯一依据。

## 2. 逐章结构

| 单元 | 正文真正讲了什么 | 实践、测验与交付物 | 阅读时应抓住的工程问题 |
|---|---|---|---|
| Unit 0：欢迎与入门 | 课程路径、前置知识、账号、Discord、认证、推荐节奏；Onboarding 还给出在 HF 推理额度不足时改用 Ollama 和 `LiteLLMModel` 的本地路径。 | 无代码作业；完成账号/社区/组织关注等准备。英文当前写认证“无截止日期”。 | 课程免费与代码运行费用要分开；中文仍写 2025-07-01 截止，已过期。见 `unit0/introduction.mdx`（原本地资料引用，未随公开版收录） 与 `onboarding.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 1.1：什么是 Agent | 给出正式定义：Agent 是利用 AI 模型与环境交互、完成用户目标的系统；把系统拆为“模型大脑”和“能力/工具身体”；用从 processor、router、tool caller、multi-step 到 multi-agent 的连续 agency 光谱解释“多自主才算 Agent”。 | 6 题不计分小测。 | 这是课程最适合做定义锚点的章节；它把 router 和 loop 放在同一连续谱上，也明确 Action 不等于 Tool。见 `what-are-agents.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 1.2：LLM 基础 | token、next-token prediction、Transformer/attention、prompt、训练阶段、模型调用方式，以及 LLM 在 Agent 中如何承担文本推理。 | 静态图、动画和示例；没有训练作业。 | 对完全没学过 LLM 的读者是快速复习，不足以替代系统的 Transformer 课程。见 `what-are-llms.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 1.3：消息与特殊 token | system/user/assistant 消息、base 与 instruct 模型、chat template 如何把对话拼成模型所需 prompt。 | 在线 chat-template viewer；代码展示 tokenizer 的模板应用。 | 对“同一消息为何换模型后表现不同”给出了底层格式解释，但没有跨模型回归测试方法。见 `messages-and-special-tokens.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 1.4：工具 | Tool 的名称、描述、typed arguments、输出、callable；模型只生成调用文本，Agent 才负责解析、执行并把 Observation 回填；用 decorator/反射自动生成工具说明，末尾介绍 MCP。 | 手写 `calculator`、通用 `Tool` 类和 `@tool` 思路；5 题小测。 | 工具 schema 与执行 loop 解释完整；缺少幂等、副作用、权限和审批的系统设计。见 `tools.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 1.5：Agent loop | 以 Alfred 查天气为例拆 Thought → Action → Observation → updated thought → final action；另讲 ReAct、CoT、Action 的 JSON/function call/code 三种表现，以及模型必须在完整 Action 后停止生成。 | `dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） 从裸 `InferenceClient` 手写 stop/parse/execute/append loop；展示一次“模型幻觉天气，必须真的执行函数”的失败。 | 与面经中的 `loop`、停止条件、工具反馈、轨迹调试直接对应。课程警告执行模型生成代码有风险，但没有把风险延伸成完整审批协议。 |
| Unit 1.6：第一个 smolagents Agent | 在 Space 中配置 `HF_TOKEN`，用 `DuckDuckGoSearchTool`、自定义工具、`CodeAgent`、system prompt，并把工具/Agent 推到 Hub。 | 动手搭建派对助理；加载 Hub 工具时示例用了 `trust_remote_code=True`；最终 Unit 1 测验可领取基础证书。 | 可展示从 schema 到运行 Agent 的最短闭环；真实项目需额外审计远程代码、密钥、网络和写操作。见 `tutorial.mdx`（原本地资料引用，未随公开版收录） 与 `final-quiz.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 2 总览 | 说明何时框架能减少重复实现，课程并列三条路径，而非宣称只有一个正确框架。 | 无独立作业。 | 比较框架时应沿状态、控制流、工具、记忆、可观测性比较，不能只比 API 长短。见 `unit2/introduction.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 2.1：smolagents | `CodeAgent` 与 JSON `ToolCallingAgent`；decorator/class 两种工具；默认工具、Hub/Space/LangChain/MCP 导入；DuckDuckGo 和自建知识库检索；manager + web/data 子 Agent；视觉/浏览器 Agent；OpenTelemetry/Langfuse。 | 两组小测和最终测验；多 Agent 练习要求查各大城市到指定地点的货运飞行时间、核对来源并画图。 | loop、tool、sandbox、可授权 imports、多 Agent 分工讲得具体；示例仍多为 notebook/单进程，没有 durable state、并发隔离或恢复。入口见 `smolagents/introduction.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 2.2：LlamaIndex | RAG 五阶段：load、index、store、query、evaluate；`FunctionTool`、`QueryEngineTool`、Toolspec/MCP；stateless Agent 与显式 `Context`；AgentWorkflow 的 event、loop、branch、state；多 Agent workflow。 | 两组小测；代码逐步建 VectorStoreIndex、FaithfulnessEvaluator、workflow state。 | 对 QueryEngine、RAG-as-tool、状态对象讲得清楚；没有系统展开 chunk benchmark、权限过滤、在线索引更新和检索回归集。入口见 `llama-index/README.md`（原本地资料引用，未随公开版收录）。 |
| Unit 2.3：LangGraph | State、Node、Edge、StateGraph；邮件分类图用 LLM 判 spam/legitimate，再经 conditional edge 路由到丢弃或回复；文档分析图加入工具和 ReAct；Langfuse trace 与 graph visualization。 | 5 题测验；运行合法邮件/垃圾邮件两个输入并观察路径。 | 与意图分类、状态机、显式编排最贴近。正文自己承认第一个邮件图“没有工具，因此不能算 Agent”，这个边界值得展示。入口见 `langgraph/introduction.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 3：Agentic RAG 用例 | 晚宴助理 Alfred 读取 `unit3-invitees` 数据集，建 guest retriever，再接 DuckDuckGo、天气、Hub stats 工具；分别提供 smolagents、LlamaIndex、LangGraph 实现；最后比较三者的记忆接法。 | 在公开 HF Space 中按模块组织代码；端到端例子覆盖 guest 查询、天气、研究者资料和多工具组合。 | 是课程把工具、RAG、编排和 memory 汇总成一个项目的核心单元。语料小且固定，示例含 email 等字段；没有访问控制、数据更新、召回指标和 PII 治理。见 `agentic-rag/invitees.mdx`（原本地资料引用，未随公开版收录）、`tools.mdx`（原本地资料引用，未随公开版收录）、`agent.mdx`（原本地资料引用，未随公开版收录）。 |
| Unit 4：最终项目 | 介绍 GAIA 的多步、工具、多模态任务与三档难度；课程取 Level 1 validation 中 20 题，提供取题、取附件、提交答案 API；答案按 exact match 评分。 | 复制 Final Assignment Space，公开 `agent_code`，提交 `task_id/submitted_answer`，上学生榜，之后领取结业证书。 | 这是明确可量化的终局作业，但 leaderboard 本身提示可绕过验证；exact match 也只评最终答案，不等于轨迹安全、成本和权限正确。见 `what-is-gaia.mdx`（原本地资料引用，未随公开版收录）、`hands-on.mdx`（原本地资料引用，未随公开版收录）。 |
| Bonus 1：函数调用微调 | function calling 的消息/特殊 token 表示；为 `google/gemma-2-2b-it` 增加能力；介绍 LoRA，再进入 notebook 微调。 | 训练/适配模型，属于计算资源更重的选修。 | 适合想理解模型侧 tool-use 的学生；对只做 Agent 应用工程不是必修。入口见 `bonus-unit1/introduction.mdx`（原本地资料引用，未随公开版收录）。 |
| Bonus 2：可观测性与评测 | trace/span，成本、延迟、属性、用户反馈、LLM-as-a-judge；offline/online eval；Langfuse + OpenTelemetry；把 GSM8K 前 10 条建成 dataset run，对比模型/工具/prompt。 | 可观测性 notebook 和 5 题测验。 | 能回答“看最终答案还是看轨迹”；但示例评测主要是输出/仪表板，没有工具权限、side-effect correctness 和长任务恢复评分。见 `what-is-agent-observability-and-evaluation.mdx`（原本地资料引用，未随公开版收录） 与 `monitoring-and-evaluating-agents-notebook.mdx`（原本地资料引用，未随公开版收录）。 |
| Bonus 3：Pokémon Agent | 游戏中 LLM/Agent 的现状、`poke-env`、Showdown、`LLMAgentBase`、战斗 Agent 与 Space 对战。 | 复制 Pokémon Space，加入自己的 Agent 并发起对战。 | 展示长时决策与环境反馈，但和企业 Agent 生产栈关联较弱。入口见 `bonus-unit3/introduction.mdx`（原本地资料引用，未随公开版收录）。 |

## 3. 推荐的静态阅读顺序

### 路线 A：零 Agent 经验、已有 Python 基础

1. Unit 1 的 `what-are-agents`、`tools`、`agent-steps-and-structure`、`actions`、`observations`。
2. `dummy-agent-library`，手工看懂一次循环后再进框架。
3. Unit 2 三框架只先选一个：代码型任务选 smolagents；RAG 数据应用选 LlamaIndex；显式状态机/路由选 LangGraph。
4. Unit 3 看三种实现如何解决同一晚宴问题。
5. Bonus 2 与 Unit 4，补评测和最终任务。

### 路线 B：面试导向

1. Agent 定义与 agency 光谱。
2. Tool schema、Action/Tool 区别、stop-and-parse。
3. Thought–Action–Observation/ReAct loop。
4. LangGraph 邮件分类与 conditional routing。
5. LlamaIndex QueryEngine、RAG-as-tool、Context。
6. smolagents manager/sub-agent 与安全 imports。
7. Bonus 2 的 trace、offline/online eval；Unit 4 的 GAIA exact match。
8. 再用本项目的差距清单补审批、数据库、并发、部署与恢复。

### 路线 C：只做静态阅读

正文的概念链仍然完整：定义 → loop → 工具 → 三框架 → RAG → eval。静态阅读能判断课程覆盖和 API 形态，不能据此声称 notebook、Space、外部 API 或证书流程在本机已成功运行。本研究没有执行任何付费推理、训练或提交。

## 4. 练习密度和知识检查

- Unit 1 有两组小测、一个正式 Unit 1 Quiz、手写 loop 和一个 Space Agent。
- smolagents 有两组小测和最终测验；LlamaIndex 有两组小测；LangGraph 有一组 5 题测验。
- Unit 3 是一个贯穿式案例，不是带 rubric 的独立作业。
- Unit 4 是最明确的终局项目：20 道 GAIA Level 1 子集、exact match、公开代码链接和榜单。
- Bonus 2 有完整仪表化/数据集评测 notebook；Bonus 1、Bonus 3 都需要额外算力或外部服务环境。

课程声称每章约一周、每周 3–4 小时；这对“阅读主干”合理，对完整跑三框架、微调、Langfuse、GAIA 和游戏 Agent 明显偏乐观。该判断来自实际正文体量和外部依赖，不是运行计时结果。

