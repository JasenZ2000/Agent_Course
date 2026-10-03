# Anthropic 官方 Agent 教材：内容与静态学习体验分析

研究快照：2026-10-03（北京时间）。本分析基于本地保存的 Claude Academy 公开课程文字、Anthropic 工程文章和 Claude Agent SDK 文档；没有观看课程视频、运行示例、调用付费 API 或完成测验。下文的“体验”指静态阅读体验。

## 资料类型与结论

Anthropic 的公开材料不是单一课程，而是三层：Claude Academy 的 90 篇公开课文（Platform 101 13 篇、Building with the Claude API 67 篇、MCP 10 篇），面向构建者的工程文章，以及把 Claude Code 能力作为库运行的 Agent SDK 文档。三者的教学任务不同：课程负责从请求和工具搭起基础；工程文章讨论生产取舍与失败模式；SDK 文档解释具体运行时接口、权限和会话。

从静态阅读看，强项是例子密、概念紧贴 API 操作，而且 Agent 主线没有停留在“模型会规划”：它把工具执行、返回结果、重复调用、状态、上下文、检验和人类确认连在一起。短板是 67 篇 API 教学切得很细，阅读者需要自己把碎片串成一个可上线应用；页面标题和示例使用的模型名、API beta、定价或参数可能随时间改变；正文包含教学占位和合成结果，不能据此认定代码已在当前环境跑通。

## 课程与工程材料怎样形成一条主线

Academy 的主体路径大致是：API 请求和多轮消息 → 提示与结构化输出 → 工具调用和循环 → RAG 与混合检索 → MCP → 工作流/Agent 取舍 → 评测与上下文。Platform 101 先给出术语地图，再用 managed agents 和 Claude Code 连接到托管服务与开发工具。课程因此兼有平台入门、API 教程和产品能力介绍；不能把全部 90 篇都当成一门从零开始的通用 Agent 工程课。

工程文章把课堂中略过的生产问题补回来。 [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) 讨论先选简单可控工作流、按任务需要增加复杂度；[Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents) 关注工具边界和输出设计；[Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 讨论上下文选择；[Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) 讨论评测设计与维护；长任务文章进一步处理跨上下文窗口的进度交接。它们适合作为课程的第二层阅读，不是 Academy 课程章节，也不应把文章例子说成课程作业。

## 可核对的具体教学例子

以下例子来自保存的课程正文，供后续讲解或复现选题使用。列表中的“示例”是文本里展示的内容，不代表我已经执行过代码。

1. **天气工具与循环**：[Agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained) 将 `get_weather` 声明为含 `city` 的 JSON Schema 工具，再由本地 `run_tool` 返回硬编码的 “95F, sunny”；程序按 `end_turn` 和 `tool_use` 分支，把 assistant 调用与 tool result 追加回消息。循环讲得很直观，天气数据是 mock。
2. **AWS 代码提示词评测**：[Generating test datasets](https://academy.claude.com/courses/building-with-the-claude-api/generating-test-datasets) 把目标限定为 AWS 相关 Python、JSON 或正则输出，并让较快模型生成三个测试输入。它展示数据集生成步骤，但三个合成 case 只能作教学起点，不能代替有代表性的验收集。
3. **评分器拆分**：[Model based grading](https://academy.claude.com/courses/building-with-the-claude-api/model-based-grading) 与 [Code based grading](https://academy.claude.com/courses/building-with-the-claude-api/code-based-grading) 分别示范模型判断和确定性检查；适合追问哪些条件可以写成程序断言、哪些语义质量需要人工校准。
4. **主题意图分流**：[Routing workflows](https://academy.claude.com/courses/building-with-the-claude-api/routing-workflows) 先将 “Python functions” 归到 Educational，再选择教育类脚本模板；输入 “surfing” 可走娱乐类。页面按多个内容类型讲路由：分类 → 选择专用处理管线，能说明“query intent”可以决定后续提示与工具。
5. **缺信息时澄清**：[Agents and tools](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools) 让 Agent 处理“90 天保修何时到期”，但购买日期未知；它应先问日期，而不是猜测。该例可用于区分信息不足与工具不足。
6. **可组合的基础工具**：同一篇 [Agents and tools](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools) 对照 `bash`、`read`、`write`、`edit`、`glob`、`grep` 这类一般能力与专用“重构代码”按钮，并举出视频处理 Agent 组合 FFMPEG、图像生成、语音合成和发布工具。抽象边界扩大了组合空间，也增加了授权和验证责任。
7. **Skill 的渐进加载**：[Platform 101 Skills](https://academy.claude.com/courses/claude-platform-101/skills) 把流程规约放入 `SKILL.md`，先提供 Skill 的名称/描述，相关时再加载正文；API 示例还把 Skill 附到 container，并启用 code execution。这个例子说明 Skill 传授做事步骤，工具提供可执行动作；也说明 API 机制不能脱离运行容器谈。
8. **四种上下文模式**：[Context management](https://academy.claude.com/courses/claude-platform-101/context-management) 并列 just-in-time retrieval、server-side compaction、prompt caching 和 memory tool。课程将缓存说成复用稳定前缀的预处理、降低重复输入成本；缓存不会替用户释放 context window 容量。Memory tool 的文件或数据库存储由调用方负责。
9. **BM25 找精确 ID**：[BM25 lexical search](https://academy.claude.com/courses/building-with-the-claude-api/bm25-lexical-search) 用 `INC-2023-Q4-011` 说明向量相似度会找语义近似但未必包含编号的段落，词法检索则有利于精确标识符。它提出与向量结果合并的方向。
10. **RRF 混排**：[A Multi-Index RAG pipeline](https://academy.claude.com/courses/building-with-the-claude-api/a-multi-index-rag-pipeline) 用向量和 BM25 的排名演示 Reciprocal Rank Fusion。示例代码的 `enumerate(all_results)` 等处仍是占位，不含完整的结果收集、去重与排序实现；该课适合学概念，不能直接作为完成的检索库。
11. **MCP 三种原语**：[Introduction to MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp) 及后续页面按工具、资源、提示模板讲 Server/Client 交互，借助 Inspector 检查服务器。它把协议使用拆成可观察步骤，而不是只讲“MCP 能连工具”。
12. **托管 Agent 的构件**：[Building your first managed agent](https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent) 逐步创建 Agent、环境、Session，先开事件流再发起任务，并消费流事件。它突出托管运行时把脑与执行环境分开，但访问、状态、成本和故障处置还要结合产品文档理解。

## 系统性、静态阅读体验和工程深度

课程的系统性主要体现在“同一接口逐步加能力”。API 部分从单次请求进入多轮对话、system prompt、流式响应、结构化数据，然后才加入工具、多个 tool block、结果回传、错误处理和循环；再扩展到检索、MCP、Agent 与 workflow。这样的顺序便于把一次模型调用看成一个更大的控制循环，也适合按小节停下来写代码。

静态阅读的限制也来自模块化：主题跨课程重复出现，例如 MCP 同时在 Platform 101、API 课程和独立 MCP 课程里讲；这能提供不同深度，却要求读者判断哪些是概览、哪些是实现。课程索引提供官方时长，但这些数字是网页标注的影音时长，不是完整学习或复现实验耗时。文字正文不像字幕转写，视频尚未观看，因此无法判断讲师停顿、演示细节、互动题和实际课堂节奏。

工程文章和当前 SDK 指南适合补足操作边界。SDK 的 [permissions](https://code.claude.com/docs/en/agent-sdk/permissions)、[hooks](https://code.claude.com/docs/en/agent-sdk/hooks)、[user input](https://code.claude.com/docs/en/agent-sdk/user-input)、[agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)、[sessions](https://code.claude.com/docs/en/agent-sdk/sessions) 和 [secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment) 让开发者看到工具执行前后的控制点、会话恢复与风险模型。静态阅读依旧不等于已验证当前 SDK 行为，实施时需按目标版本核对。

## 与 Agent 面经的对应

本地面经样本多次触及 Tool/Skill/MCP、路由、Agent loop、任务隔离、状态恢复、权限、评测、LangGraph、数据库与并发。Anthropic 材料能支撑术语基础和若干取舍问题：Agent vs workflow、抽象工具组合、输入不全时追问、路由器给定类别、RAG 检索、评测集和评分器；工程文章与 SDK 文档能进一步引出 harness、上下文交接、hook/权限和 trace。

需要另做项目才能回答的问题包括：工具幂等和超时后的重复执行、授权模型与租户隔离、并发和压测、跨进程恢复、LangGraph 状态图与原生 SDK 的实际取舍、模型/工具失败后的回滚，以及评测分数是否对应真实用户结果。面经中提到一种框架不等于课程已覆盖其实现细节；课程也没有提供生产流量指标作为“高频面试答案”。详见[面经综述](../../../agent_interview_review.md)。

## 先修、成本与主要缺口

读者至少需要会读 Python 或 TypeScript，理解 HTTP/JSON、函数调用、异步请求与基本数据结构。仅看 Platform 101 可以建立概念词汇，但若要跟 API 代码，需要开发环境、Anthropic Console/API key，并承担实时模型调用费用；课程静态文字没有替读者验证额度、账单或模型可用性。MCP 项目还要求理解进程/网络传输、环境变量和工具协议。

这批材料更强于产品/API 采用与基础构件教学，较弱于跨供应商迁移、严谨的安全测试、数据库/队列选型、生产容量、成本基线、长任务回归集及完整端到端作业验收。应该把概念文章和代码实现结合阅读，再用本地可控的小任务补上测试、失败路径和可观测性。
