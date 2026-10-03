# Agent 应用开发面经综述：研究范围与阅读地图

研究截止：2026-10-02（中国标准时间）。这是一份持续更新的公开资料综述，面向准备 Agent 应用开发、AI Coding、RAG/工具系统、Agent Harness 等岗位的毕业生和转型开发者。它不声称收尽互联网上的所有面经：私密群、登录墙、已删除内容、付费专栏和未被索引的帖子无法完整覆盖。

## 1. 收什么，不收什么

**核心样本**：作者自述参加过具体公司或团队的实习、校招或社招面试，并提供岗位、轮次、问题或项目追问的公开内容。中文和英文材料均收录；只保留能回到原页面的直链。

**辅助样本**：明确标注的二手整理、模拟面试、培训视频、公开岗位说明与官方工程资料。它们用于补充检索入口、解释岗位或设计自己的实验，不计入“亲历面经”数量。

**暂不计入**：只有“某厂必考”标题而没有来源的题库；搜索摘要无法核验正文的帖子；把多个公司的题目混排、无法区分经历与自拟题的文章；纯模型训练或纯算法岗位中与 Agent 应用开发没有清楚关联的内容。

## 2. 每条资料的核对字段

| 字段 | 记录方式 |
|---|---|
| 来源 | 平台、原帖直链、作者/UP 主、访问日期 |
| 发生背景 | 公司/团队、岗位原名、实习/校招/社招、地点、轮次、面试日期；缺失则写“未说明” |
| 证据类型 | 第一人称已完成面试、第一人称准备帖、二手整理、教学/模拟、官方岗位、官方工程资料 |
| 可见范围 | 原帖全文、公开段落、视频页面元数据、搜索摘要、需登录、失效 |
| 内容 | 只概括公开可见的追问主题；保留项目/算法/系统设计/编码等环节差异 |
| 媒体材料范围 | 已查看正文、仅有页面元数据/简介、需实际观看/转写，或仅待核验 |

一条匿名面经最多支持“这个投稿者说自己在这个场景遇到了这些问题”。它不支持“某公司统一这样考”或通过率推断。岗位 JD 说明工作内容，不说明面试题。视频若只查到标题、简介和章节，不能据此断言其正文内容。

## 3. 四条岗位路线

| 路线 | 常见交付物 | 面经中应单独索引的追问 | 需要避免混淆的地方 |
|---|---|---|---|
| Agent 应用/全栈 | 场景、工具、检索、状态、前后端和上线 | 项目贡献、业务边界、RAG、Tool/Skill、失败恢复、评测、并发 | 不能把工作流编排等同于模型算法研究 |
| Code Agent / Harness | 长任务执行器、上下文、沙箱、工具和可观测性 | Agent loop、状态恢复、上下文压缩、权限、trace、AI coding | 对应岗位常要求更强工程能力，海外社招经验不能当应届考纲 |
| Agent 基础设施/平台 | 服务、租户隔离、部署、身份、成本和可靠性 | 后端/分布式基础、系统设计、工具执行、观测与容量 | 单个学生 Demo 不能证明生产规模，但可做最小失效实验 |
| Agent 算法/研究 | 规划、训练、数据、模型和评测方法 | 论文/实验、SFT/RL、评测集、模型与规划取舍 | 模型训练题不应混入应用开发入门清单 |

## 4. 按面试环节建目录

1. **简历与项目深挖**：任务是什么、个人负责哪一段、为什么选这一方案、数据和指标是什么、失败时如何修复。先查[牛客小红书 Agentic 全栈实习生自述](https://www.nowcoder.com/feed/main/detail/e5e9311a623940eead6ec98c65e7f9e8?sourceSSR=subject)和[牛客三场 Agent 后端复盘](https://www.nowcoder.com/discuss/919608103723622400?sourceSSR=post&weFlow=true)。
2. **Agent 系统设计**：单 Agent/workflow/多 Agent，工具 schema，状态与 Memory，RAG，权限，异常和人工接管。用[Anthropic 的 Agent 工程说明](https://www.anthropic.com/engineering/building-effective-agents)统一术语，再看具体面经提出过什么问题。
3. **评测与调试**：测试任务如何构造，最终结果与轨迹如何一起判断，成本/延迟/成功率如何取舍。[Anthropic 的 Agent eval 说明](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)可作方法依据。
4. **编码与计算机基础**：真实代码库、测试、数据结构/算法，以及数据库、并发、网络和系统排障。国内多条面经把这些与 Agent 项目放在同一场谈；海外的[Meta AI coding 第一人称自述](https://leetcode.com/discuss/post/7335102/)也提醒 AI 辅助下仍需解释自己的工程判断。
5. **岗位/业务差异**：实时多模态 Agent、企业知识、搜索、广告、编码助手各有额外约束。目录要先标岗位，再讲技术，不把题目机械合并。

### 可复用的问题标签

这套标签用于整理面经，不代表出现次数或重要性排序。一个问题可同时落入多个标签。

| 标签 | 面经里应记录的具体追问 | 适合用什么证据回答 |
|---|---|---|
| `project` | 做了什么、本人贡献、为什么选这条路、业务约束 | 项目数据流、代码提交、实验记录 |
| `loop` | Agent 与 workflow 的边界、规划与执行、停止条件 | 同一任务的两种运行轨迹 |
| `tool` | Tool/Function/MCP/Skill、schema、异常、重试、幂等 | 工具契约和故意失败的调用日志 |
| `context` | 长短期记忆、上下文压缩、跨轮状态、恢复 | checkpoint、摘要前后结果、回放 |
| `rag` | 分块、召回、重排、引用、知识更新、权限过滤 | 固定语料、检索指标和错误答案 |
| `eval` | 评测集来源、任务成功率、轨迹、Bad Case、回归 | 测试集版本、评分规则和失败分类 |
| `security` | Prompt injection、敏感操作、审批、沙箱 | 越权输入、拒绝日志、人工确认记录 |
| `production` | 延迟、成本、并发、观测、部署、降级 | 压测、trace、成本表和回滚流程 |
| `coding` | 现场编码、读已有代码、修测试、复杂度 | 测试结果、diff 与人工解释 |
| `fundamentals` | 数据结构、数据库、网络、OS、语言细节 | 可运行代码或准确的问题分解 |
| `model-research` | 训练/微调/对齐、规划算法、论文与实验 | 数据、基线、消融及复现条件 |
| `behavior` | 跨团队合作、失败复盘、用户价值和取舍 | 一件具体经历的行动和结果 |

本综述按五个大类汇总；详细标签用于进一步检索和主题分析。

## 5. 这批材料初步能说明什么

这里的归纳来自定向收集的公开样本，主要用于了解岗位主题与课程内容之间的关联；它不是按岗位随机抽样得到的“高频题统计”。

| 观察 | 支持它的具体材料 | 相关能力主题 |
|---|---|---|
| 国内应用/全栈样本常把 Agent 项目和传统工程基础连着追问 | [牛客小红书 Agentic 全栈实习自述](https://www.nowcoder.com/feed/main/detail/e5e9311a623940eead6ec98c65e7f9e8?sourceSSR=subject)、[三场 Agent 后端复盘](https://www.nowcoder.com/discuss/919608103723622400?sourceSSR=post&weFlow=true) | 并发、数据库、异常处理 |
| 具体项目比术语列表更容易被连续追问 | [牛客蚂蚁智能体应用实习自述](https://www.nowcoder.com/feed/main/detail/376b964b0d154881bcfe3c46fe1a0e2a?sourceSSR=post)、[牛客小红书一面](https://www.nowcoder.com/feed/main/detail/f1ed02bfdae04730837753b62e0d58b9?toCommentId=22874357) | 项目贡献、状态管理、并发 |
| 海外 AI coding 个案强调在现有代码和测试中做工程判断 | [Meta 候选人自述](https://leetcode.com/discuss/post/7335102/)、[Anthropic 工程岗候选人公开复盘](https://www.linkedin.com/posts/ashutosh-kumar-singh951_recently-i-gave-an-interview-with-anthropic-activity-7426682262643150848-c2Hp) | 代码库阅读、测试与修改验证 |
| 官方岗位和工程资料共同指向可评测、可靠的 Agent 系统 | [OpenAI Codex 应用工程岗位](https://openai.com/careers/applied-ai-engineer-codex-core-agent-san-francisco/)、[Anthropic Agent eval 工程文档](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 任务成功条件与操作边界 |

以上行与行之间不能直接比较“哪个地区更重视什么”：岗位级别、团队、发布时间和平台发帖习惯都不同。海外样本中资深岗位较多，应与国内实习/校招样本分开理解。

## 6. 本轮覆盖与可见缺口

这次三路并行扩充在原有清单之外，新增了 **22 条牛客**与 **4 条 V2EX** 的第一人称相关来源；其中 V2EX 多是求职复盘，颗粒度低于逐轮面经。海外另新增 **8 条独立页面的一手完成经历**、**1 条第一人称视频**与 **1 条评论中的已完成经历**，另有 **2 条 AI lab/ML infra 邻近经历**单列。海外还保存了 10 条第三方/匿名报告和 4 条纯准备帖，它们不并入一手数量。计数口径是“新增、去重的来源 URL”，一篇帖子记录多场面试仍只算一条来源；不同证据等级不能相加成“真实面试次数”。详见[国内扩充目录](interview_catalog_china_expanded.md)与[海外扩充目录](interview_catalog_overseas_expanded.md)。

| 平台/地区 | 已有可用覆盖 | 仍缺什么 |
|---|---|---|
| 牛客 | 字节、百度、小红书、蚂蚁、阿里云、拼多多、B 站等应用/后端/Coding Agent 面经；项目、RAG、状态、评测和传统工程基础都有具体追问 | 作者背景、岗位 JD、面试发生时间经常不完整；不能据帖子多寡推断公司实际招聘权重 |
| V2EX | 从传统开发转 AI 应用、前端/后端面试和岗位讨论 | 多数不是逐轮题单，适合职业路径和信息缺失案例 |
| Bilibili / YouTube | 可核对页面元数据、作者自述、简介和公开章节；有少量第一人称视频与大量培训综述 | 本轮没有逐条观看或转写，标题里的“真题/高频”未独立验证；某些搜索结果对应的视频已经失效 |
| 小红书 / 微信 | 保留可追踪的帖子 ID、题名或原文链接 | 当前环境原站登录/超时/抓取失败；正文、作者和问题未核验，不计入已核验样本 |
| 海外论坛/博客 | Google FDE、Meta AI coding、Amazon Applied Scientist、OpenAI Applied AI 评论、EPAM/Intuit 等具体个人经历；官方岗位可交叉核对工作内容 | 一手 Agent 专岗样本仍少，senior/社招多；Blind/Glassdoor 常有登录墙或匿名二手转述 |

**覆盖率不可估计。** 没有公开的“所有面试”总体，也无法知道未发帖的面试。后续要继续扩充，应优先补少量高质量缺口：国内非牛客平台的一手可读原帖、海外 Agent 应用专岗的候选人独立复盘、每份面经对应的具体岗位 JD，以及公开视频的实际转写。

## 7. 第一轮材料入口

- 此前收集的校招岗位与牛客面经（原本地资料引用，未随公开版收录）
- Bilibili 视频目录（原本地资料引用，未随公开版收录）
- 牛客、小红书、知乎、掘金、公众号（原本地资料引用，未随公开版收录）
- 海外面经、讨论、视频与官方资料（原本地资料引用，未随公开版收录）
- 跨平台先看顺序（原本地资料引用，未随公开版收录）

- [新增中国平台第一人称面经](interview_catalog_china_expanded.md)
- [新增海外第一人称与第三方报告](interview_catalog_overseas_expanded.md)

## 8. 样本的使用边界

本资料按岗位路线和面试环节组织公开样本，适用于查找项目、Agent 系统设计、评测和编码基础等相关主题。样本范围与来源可信度见逐条链接；不同证据等级不应合并为“高频题”统计。

## 9. 官方 Agent 教材如何辅助面经准备

本节把 Anthropic 与 OpenAI 官方资料当作概念、代码路径和系统边界的参考，不将它们算作面经，也不推断某公司按官方文档出题。快照范围、课程结构和未取得正文项分别见[Anthropic 课程分析](agent_courses/providers/anthropic/analysis.md)、[OpenAI 路线分析](agent_courses/providers/openai/analysis.md)与[方法说明](agent_courses/methodology.md)。

对照公开样本时能看到几类相邻追问：字节 Agent 汇总帖涉及意图分类、RAG、路由、MCP/Skill/Harness；百度 Coding Agent 复盘涉及 ReAct、工具、Skills 注入/隔离、权限与沙箱；千问 AI 研发自述涉及 Agent/workflow、路由、循环终止、工具 JSON、Skill 和 Harness；拼多多 Agent 二面涉及任务隔离、评测覆盖、并发和线程安全 LRU。可分别查[字节 AI Agent 开发岗面经-01](interview_catalog_china_expanded.md)、[百度秋招 Coding Agent 三轮自述](interview_catalog_china_expanded.md)、[千问 AI 研发一面](interview_catalog_china_expanded.md)、[拼多多 Agent 二面](interview_catalog_china_expanded.md)的逐条原始链接。它们是具体作者的公开自述，不是统一考纲统计。

## 10. 操作边界：Agent 可以做什么，何时需要停下来

把工具权限按风险讲清楚，比笼统回答“加 guardrail”更可检验：

| 操作级别 | 例子 | 运行策略 |
|---|---|---|
| 只读 | 搜索文档、读取用户有权限访问的记录 | 校验调用身份与资源范围，限制返回字段和数据量，记录查询 |
| 可逆的本地变更 | 草稿文件、暂存配置、临时沙箱命令 | 限定 workspace/sandbox；执行后展示 diff 或结果；保留撤回点 |
| 外部副作用 | 发邮件、退款、发布内容、修改工单/数据库 | 在每次具体工具执行前复核身份、目标和参数；需要时暂停待批准；设计幂等键和审计记录 |
| 高风险/破坏性 | 删除、执行任意 shell、访问生产数据或凭据 | 默认拒绝或收紧 allowlist；明确业务授权范围；高风险动作要求更强的人类确认或专门策略服务 |

面试回答可按“谁请求 → 哪个资源 → 做哪种动作 → 用何种授权检查 → 是否可撤销 → 失败/重复会怎样 → 留下什么记录”展开。用户输入里的指令不应提升工具权限；工具执行侧必须独立校验作用域。OpenAI 文档中的 input/output/tool guardrail 是自动验证机制，人工审批会让 run pause；guardrail 本身不等于身份认证、RBAC 或数据库行级权限。parallel guardrail 可能与主模型工作重叠；若风险要求先拦截，应选择阻断模式。文档还限定 agent-level input check 只运行在链首、output check 只运行在最终输出的 agent；敏感写操作要在具体 tool 边界校验。

## 11. Harness：把“模型会用工具”讲成一个工程系统

一个可讨论的 Harness 至少包含：

1. **运行循环**：收任务、调用模型、解析工具请求、执行工具、追加结果、停止/继续；约束最大步数、超时和取消。
2. **工具契约与执行器**：schema、描述、权限、参数校验、错误格式、重试、幂等与结果大小。
3. **状态和上下文**：跨轮消息、会话持久化、工具输出裁剪/检索、checkpoint、摘要和恢复策略。
4. **编排**：固定步骤用 workflow；类别清楚时分流；结果依赖未知或需要规划时给 Agent 选择下一步；多 Agent 要定义交接所有权。
5. **边界控制**：sandbox、数据权限、敏感动作审批、输入/输出/工具级 guardrail、隔离租户。
6. **可观测与评测**：每次 run 的模型/工具/路由/审批事件，结果 grader、轨迹 grader、失败分类、成本/延迟和回归集。

面试不要只报组件名字；画出一个 request 从入口到最后 tool result 的时序图，然后指出异常在哪一层处理。Anthropic 的 [Agent SDK loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)、[permissions](https://code.claude.com/docs/en/agent-sdk/permissions)、[hooks](https://code.claude.com/docs/en/agent-sdk/hooks) 与长任务 [harness 文章](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)能作概念锚点；OpenAI 的 [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)把 loop、sessions、stream、interruption 和 continuation 连在一起。

## 12. 重构编排层与框架取舍

“重构编排层”本身是一个项目动作：当路由规则、工具执行、会话状态和审批散落在提示词或 API handler 中，以最小改动把它们抽成可单独测试、可观测的流程边界。面试官可能继续问：哪类变化触发重构、如何保持用户可见行为、旧状态如何迁移、分流错误如何回归、是否能快速回滚。只说“为了可维护性重构”没有展示判断证据。

一种实际决策顺序：

1. 任务步骤完全确定时先写普通函数/状态机/workflow，少依赖模型自行规划。
2. 不同意图需要不同模板或处理服务时，使用有界标签、显式兜底和分流评测。
3. 下一步取决于中间结果时，引入 Agent loop，并明确结束条件和允许的工具。
4. 子任务需要独立对用户负责时用 handoff；只需调用受限子能力、最后由 manager 组织答案时用 Agent-as-tool。
5. 需要共享状态、条件边、循环、持久化 checkpoint 和人工中断时，可评估 LangGraph 这类图编排方式；在 OpenAI Agents SDK 里可按 runner、handoff 和 `as_tool` 组织。两者的状态和执行模型不同，不能只对 API 名称做一一替换。

判断是否值得增加框架/Agent 数量，要拿 Bad Case、状态迁移复杂度、调试成本和操作风险作依据。Anthropic [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)的“从最简单方案开始”与 OpenAI [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)的责任归属选择，是回答这类问题的官方参考；它们没有提供 LangGraph 的完整教学，LangGraph 细节仍需在自己的项目和指定版本文档中验证。

## 13. Query 意图分流与澄清

先说清 query 的含义：它可以指用户自然语言输入，也可能是检索查询，或 SQL。讨论路由前先固定输入、意图集合和业务后果；不要因为所有输入都叫 query 就假定同一种分类器。

可解释的用户意图流程是：

```text
原始输入 → 归一化/抽取实体 → 有界意图分类 → 置信度/缺字段检查
                              ├─ 明确且低风险 → 专用 workflow 或只读 tool
                              ├─ 信息缺失/多义 → 追问或展示选项
                              ├─ 涉及副作用 → 授权与审批流程
                              └─ 越界/低置信度 → 拒绝或人工队列
```

Anthropic Academy 的 `routing-workflows` 用“Python functions”归到 Educational 后选择模板，演示的是内容任务的意图分类；`agents-and-tools` 里的“90 天保修何时到期”缺少购买日期，演示的是必须先澄清实体字段。生产路由还需测试多意图、拒绝、低置信度、改写、注入式输入和数据权限过滤；不能用模型分类结果直接授予退款或数据库写权限。

面试可主动补充：用规则处理确定实体/格式、用模型处理语义模糊分类；限定返回的 enum/schema；为边界输入设置澄清分支；对误路由定义混淆矩阵、召回率/精确率或按业务风险加权的成本。比“prompt 让模型选工具”更能说明可测性。

## 14. Tool、Skill、MCP 和 LangGraph 等概念的映射

| 概念 | 简洁定义 | 面试中常见混淆 |
|---|---|---|
| Tool / function tool | Agent 可以按 schema 请求调用的一项动作；宿主执行后回传结果 | 模型生成 tool call 不等于已完成执行；需处理校验、授权、超时和副作用 |
| Skill | 程序规约、步骤、资源和可选脚本组成的可加载工作方法 | Skill 通常教“如何做”；Tool 才是实际调用的动作。不同厂商 Skill 包装和加载约定不同 |
| MCP | 让客户端和外部服务按协议交换 tools/resources/prompts 等能力 | MCP 解决互操作，不替应用做用户授权、租户隔离或危险操作确认 |
| Agent loop / Harness | 运行模型、工具、上下文、状态、停止/恢复与边界控制的宿主系统 | Agent 不能只按模型本身定义；框架 runner 是 Harness 的一种实现 |
| LangGraph | 用状态图、节点、边、循环和 checkpoint 表达流程的编排框架 | 它可承载 Agent 和 workflow；不等于一个模型，也不自动解决权限或数据库容量 |
| Handoff / Agent-as-tool | Handoff 转移控制权；as-tool 由 manager 调用子 agent 并保留控制 | 两者输出责任、后续对话归属和 trace 都不同 |

练习用自己的项目把六项各指向具体代码：哪一处是路由、哪一处是 tool contract、Skill 从何处加载、MCP server 暴露什么、checkpoint 存什么、哪个 agent 对最终回复负责。术语背诵不如一条可回放的执行轨迹。

## 15. SQLiteSession 与“100k 请求”问题

OpenAI 的 Running agents 指南用 `SQLiteSession("conversation_123")` 演示如何把一次会话历史保存并在下一轮恢复。这说明 SDK 支持一种本地 session 后端，不足以得出“SQLite 就能/不能承接生产 100k 请求”的结论。面试中第一步应追问“100k”指什么：累计用户数、会话数、每天请求数、每秒峰值、并发 run，还是每次工具状态写入？它们是不同负载。

然后把需求转成测量条件：请求到达分布、读写比例、每 session 写入频率、状态大小和保留周期、强一致要求、进程/容器数量、部署拓扑、备份与恢复时间、审批中断的最长保存时间。若只是一个开发机上的十万条短记录，存储容量与高并发多副本事务是不同问题；高写并发、跨主机共享、严格恢复目标或租户隔离通常会促使团队选用具备连接池/横向部署/事务管理能力的托管数据库。具体阈值必须用目标 workload 压测，不根据一个整数猜测。

建议答题框架：

1. 用 `tenant_id + conversation_id` 等明确键做数据隔离和索引；说明敏感字段、过期清理、加密/备份策略。
2. 让 run 状态和副作用结果具备幂等/去重标识；checkpoint 应能恢复到“工具是否已执行、是否待批准”，不能只存聊天文本。
3. 明确并发冲突处理、写入事务、重试行为、锁等待、故障恢复与备份演练。
4. 用压测复现目标峰值，观察 p95/p99 延迟、锁/连接等待、错误率和恢复表现，再决定是否维持 SQLite 或迁移。

不要给“100k”一个脱离负载条件的固定数据库答案；也不要把 SQLiteSession 演示理解成 OpenAI 对生产存储的背书。面经里关于线程安全缓存、并发和数据库追问可以作相邻练习，但每条公开帖仍只代表作者个人经历。

## 16. 复习时可自测的具体问题

1. 用时序图说明一轮 tool call 从模型响应到函数执行、结果回填和停止的全过程。
2. 哪些工具是只读的？哪些会产生副作用？如何验证调用人有权对目标资源执行动作？
3. 缺少日期/用户/商品等关键实体时，何时澄清，何时检索，何时拒绝？
4. 固定流程为什么继续用 workflow；什么 Bad Case 证明要引入 Agent loop？
5. 为什么用 handoff 而不是 manager-as-tool？谁产出最终答复，下一轮由谁控制？
6. Skill、Tool 与 MCP 分别解决哪层问题？安全边界落在哪里？
7. 如何定义一次 Agent run 的成功？只看最终答案是否会漏掉越权路径或碰巧成功？
8. SQLiteSession 在 demo 中证明了什么？要评估“100k 请求”还缺哪些流量和恢复数据？

准备上述问题时，先从已有面经原帖确认作者实际提到什么，再用官方文档补概念，并用自己的一个小项目、失败轨迹和评测数据作回答证据。课程覆盖不是个人掌握证明；任何“我做过”的说法都要能指出实现、输入输出和验收结果。
