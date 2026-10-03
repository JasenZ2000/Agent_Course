# 中国平台 Agent / AI Coding / RAG / Harness 面经扩展目录

> 研究日期：2026-10-02（Asia/Shanghai）  
> 本文件只新增条目，不改写 Agent/research/platform_china_social.md、Agent/research/graduate_interview.md。已将其中出现过的原帖直链去重。范围包括 Agent 应用开发、Coding Agent、AI Coding、RAG、Memory、MCP/Skill/A2A、Harness、评测和相邻后端工程问题。

## 0. 证据等级、去重和访问边界

| 等级 | 定义 | 可用于视频的方式 |
|---|---|---|
| **A** | 原帖正文在本次访问中可读；作者明确以候选人/求职者第一人称叙述一次或多次面试，并能核对公司、岗位或面试时间中的大部分字段 | 可以概括为“该作者自述”；不能外推为公司统一题单 |
| **A\*** | 原帖可读且明显是作者亲历，但年份、招聘阶段、公司/团队或轮次有字段缺失；或是第一人称求职复盘而不是逐轮题目记录 | 可作一手补充，缺失字段必须写“未明/年份未明” |
| **B** | 原帖可读，但为公开讨论、模拟面试、教程、二次整理或一手回复的混合线程；不能确认每道题对应一次真实面试 | 只当主题线索，不能称“面经原题” |
| **C** | 只在公开索引/报告中看到标题、日期或 ID；原站在本次访问中登录重定向、超时或正文不可读 | 只能列入待核验目录，不复述题目内容 |

去重规则：对 Agent/research/platform_china_social.md 和 Agent/research/graduate_interview.md 中已出现的牛客、小红书、知乎、掘金直链做了精确 URL 去重。本文件的“新增一手数量”按新增原帖 URL 计数，不按一帖内的面试轮次数计数。

日期规则：页面只写“8.25”“今天”等相对日期时，不擅自补年份；如果页面发布时间能确定年份但面试日期没有年份，分别记录。岗位阶段只有作者标签或标题支持时才写“实习/校招/社招”，否则写“未明”。

---

## 1. 牛客：新增、正文可核验的一手原帖

这些链接均不在前两份已有清单中。读到范围说明本次实际看到的公开正文；遇到页面局部加载或搜索摘要补充，会明确标注。

| # | 原帖直链 | 公司 / 岗位 / 阶段 | 面试日期；发布日期；轮次 | 主题标签与实际读到范围 | 第一人称 / 访问状态 |
|---:|---|---|---|---|---|
| 1 | [法本信息 AI Agent 开发](https://www.nowcoder.com/feed/main/detail/d8f5de441b7a4f7ba32164ef37cce1fc) | 法本信息；AI Agent 开发；招聘阶段未明（页面未说明校招/实习/社招） | 面试 2026-07-24；帖 2026-07-30；轮次未明 | #CodingAgent #Harness #RAG #Memory #ContextEngineering #评测。读到本地 Coding Agent 全链路、模型后端抽象、工具定义/注册/发现/调用、失败恢复、上下文压缩与摘要漂移、Memory 污染、重复工具检测、Harness、eval、回滚/重试。 | **A**；作者周之若贤直接以面试复盘口吻记录；正文可读，岗位和日期可核对。 |
| 2 | [字节跳动 AI Agent 开发岗面经-01](https://www.nowcoder.com/discuss/922659050167226368?sourceSSR=home) | 字节跳动；AI Agent 开发；其中含实习记录，具体批次/阶段按小节而异 | 帖中可核对 2026-08-20、08-19、08-18、08-16、08-14、08-13 等；帖约 2026-08-28；一面/多轮汇总 | #Agent架构 #RAG #多Agent #MCP #Skill #Harness #AI编程 #安全。读到规划/记忆/工具/执行、意图分类、RAG 全流程、PDF/表格解析、Query Rewrite/HyDE/Hybrid/GraphRAG、状态机、SSRF/CSRF、ReAct、路由、指标、ASR/多模态、Spec Coding/Harness 和 AI Coding。 | **A\***；作者林小白zii以个人汇总帖记录，但一帖集合多条面经，不能确认每一段均为同一候选人的同一岗位；正文可读。 |
| 3 | [字节跳动 AI Agent 开发岗面经-03](https://www.nowcoder.com/discuss/922659809084571648?sourceSSR=home) | 字节跳动；AI Agent 开发；招聘阶段未明 | 帖中可核对 2026-08-03、07-31、07-24、07-15、07-14、07-10、03-14 等；帖约 2026-08-28；多轮汇总 | #RAG #OCR/ASR #多Agent #LangGraph #评测 #工具安全 #AI编程 #后端。读到 RAG 存储/召回、OCR/ASR、多模块与多 Agent 取舍、Memory/效果评估、LangGraph/AgentExecutor、RRF、工具安全与循环、PostgreSQL MVCC、iOS/全栈 AI Coding、Prompt/Context。 | **A\***；作者为个人汇总，正文可读；轮次与候选人归属需以各小节为准。 |
| 4 | [百度秋招 Agent 一面二面三面（Coding Agent，三面挂）](https://www.nowcoder.com/feed/main/detail/b9521e2b51e04afeac0a3a32e13f4da9) | 百度；后端/Agent、Coding Agent；**秋招/校招** | 2026-08-18、08-21、08-24；帖 2026-09-02；一面/二面/三面 | #CodingAgent #ReAct #Tool #Context #Skill #权限 #沙箱 #算法。读到 ReAct、工具/上下文/向量检索、Prompt、Agent 与单 LLM、Coding Agent 设计、Skills 选择/注入/隔离/并发/秘密、HTTPS/URL 链、cgroup 和算法题。 | **A**；作者炒肉多，员工页显示后端实习背景，正文直接写三轮经历和结果；页面可读。 |
| 5 | [快手电商后端实习一面凉面](https://www.nowcoder.com/feed/main/detail/78fc3b815b4a4b3bb27d642fb53da16b) | 快手电商；后端实习；**实习** | 面试 9.9（正文未明确年份）；帖约 2026-09；一面 | #CodingAgent #ReAct #工具选择 #上下文压缩 #Memory #权限 #Checkpoint。读到 Coding Agent 项目追问、完整 ReAct、数千工具管理、主/子 Agent 通信、大工具输出落盘/摘要、Context metadata、危险命令拦截、子 Agent 权限、Memory 持久化/顺序/检索、checkpoint/状态机；另有 H100 最大子数组。 | **A\***；作者唐唐龙第一人称复盘；直链正文可读，面试年份和精确发布日期未稳定显示。 |
| 6 | [深圳兆珑科技一面](https://www.nowcoder.com/feed/main/detail/9105798696924c61a0447d0ef53eb6bc) | 深圳兆珑科技；岗位未明确（Java 求职背景）；阶段未明 | 面试 6.8（年份未写；帖发布时间 2026-06-08）；一面 | #VibeCoding #SpecCoding #OpenSpec #CodingAgent #Memory #Tool边界。读到 Vibe Coding、Spec/OpenSpec、AI 生成代码的测试/性能、Coding Agent Memory pipeline、工具边界和冲突偏好；正文含作者答案与面后反馈。 | **A\***；作者门头沟学院 Java 求职者以第一人称记录；搜索结果与页面正文可交叉核对，部分正文加载不稳定。 |
| 7 | [5.14 华清未央一面](https://www.nowcoder.com/feed/main/detail/0205abe68a0141aabaee6bb08ba4902e) | 华清未央；岗位未明；阶段未明 | 面试 5.14（年份未写）；帖 2026-05-30；一面 | #Agent #LangChain #LangGraph #RAG #Memory #AI编程。读到 Agent 项目、LangChain/LangGraph、RAG、混合记忆/向量库、记忆过期、AI Coding、Coding Agent 机制和模型知识；作者自述未通过。 | **A\***；正文可读且为第一人称，但岗位阶段和面试年份不明。 |
| 8 | [小厂 agent 复盘](https://www.nowcoder.com/feed/main/detail/a23c13d17e12492ebbe4c812215802ab) | 某小厂；Agent 开发；阶段未明 | 面试 4/20（年份/轮次未明确）；帖约 2026-04-20；一面复盘 | #LangGraph #LangChain #循环 #多Agent #可观测性。读到 LangGraph 与 LangChain 取舍、循环、多 Agent、可观测性和控制；“补充”部分包含作者面后准备内容，已与当场问题分开。 | **A\***；作者吃不饱的芹菜很有担当，第一人称；正文可读，但需避免把补充准备题说成实际面试题。 |
| 9 | [凌脉｜AI 应用开发实习面经](https://www.nowcoder.com/feed/main/detail/76f5be8b8bd5420b94d32a66e26a7ad9) | 凌脉；AI 应用开发实习生；**实习** | 面试 2026-07-11；帖 2026-08-05；技术一面（约 21 分钟） | #RAG #Qdrant #Redis #Harness #ToolSchema #安全 #ContextBudget #AI编程。读到 RAG、Qdrant/Redis、Harness、工具 schema/安全参数、workspace 边界、审批、重复工具、上下文预算、敏感日志和 AI Coding；评论补充 prefix caching/call hash/sliding window。 | **A**；作者 GdAfterN 第一人称；正文可读，评论与主帖已区分。 |
| 10 | [安软｜AI 应用开发实习面经](https://www.nowcoder.com/feed/main/detail/40920533fad14136bff01c3928c7e953) | 安软；AI 应用开发实习生；**实习** | 面试 2026-07-25；帖 2026-08-05；技术一面（约 28 分钟） | #AI编程 #Agent #Context #RAG评测 #Redis #IO多路复用 #数据库。读到 AI Coding、模型选择、Context 管理、自建 Agent、RAG 评测、Redis、IO 多路复用和数据库追问。 | **A**；作者 GdAfterN 以第一人称记录；正文首次打开可读，后续访问偶有超时。 |
| 11 | [千问 AI 研发一面凉经](https://www.nowcoder.com/feed/main/detail/ebf0ec03e5ee4fa8a140cc8d247b1e20) | 千问；AI 研发；**秋招/校招标签** | 面试 9.16（年份未在小节明确）；帖 2026-09-21；一面 | #AgentvsWorkflow #路由 #循环终止 #LangChain #LangGraph #ToolJSON #Skill #Harness #Python。读到 Agent 与 Workflow、幻觉与固定/动态路由、循环终止、LangChain/LangGraph、工具 JSON/参数错误、边界条件、Skill、Harness、Python 和 AI Coding 状态机。 | **A**；作者在抱佛脚的芝士很完美，正文直接写面试过程；页面可读。 |
| 12 | [拼多多 Agent 二面](https://www.nowcoder.com/feed/main/detail/f5e7351df8364147ac8da085b99d9d18) | 拼多多；Agent 相关岗位；**秋招标签** | 面试 8.25（约 40 分钟，年份未在正文明确）；帖 2026-09-04；二面 | #任务隔离 #评测覆盖 #业务流程 #LangChain #LangGraph #并发 #LRU。读到任务隔离、准确性/Agent 评测覆盖、业务流程、框架取舍和线程安全 LRU。 | **A**；作者在抱佛脚的芝士很完美，第一人称；正文可读。 |
| 13 | [佰聆数据助理 AI 应用开发工程师实习一面](https://www.nowcoder.com/discuss/906897383676538880?sourceSSR=dynamic) | 佰聆数据；助理 AI 应用开发工程师；**实习** | 面试 2026-07-14；帖 2026-07-15；一面 | #LangGraph #LangChain #结构化输出 #Skill #MCP #RAG #A2A #SubAgent #Context。读到 JSON 输出校验、Skill 与 Prompt/MCP、检索、微调学习率、A2A/SubAgent、Prompt/Context 管理和前端协议。 | **A**；作者魔仙堡的小莫仙w，正文为第一人称面经；页面可读。 |
| 14 | [B站 Agent 二面（评论含一面）](https://www.nowcoder.com/discuss/919630524673458176?sourceSSR=dynamic) | B站；Agent 方向；实习背景，岗位性质未在主贴完整说明 | 面试 8.13（主贴）；帖 2026-08-19；二面；评论记录 8.11 一面 | #A2A #Memory #Hooks #评测 #Workflow #Agent #CodingAgent #CI/CD。读到 A2A 适用性、Memory 系统、已有方案与自研、非编码 Agent、确定性输出、hooks、badcase/eval、Workflow 与 Agent、代码题；评论的一面含 Agent 项目、云、cgroup、A2A、CI/CD、compacting。 | **A**；作者 Bk7 第一人称；主贴与评论可读，评论内容应单列为“补充一面”。 |
| 15 | [深信服 AI Agent 一面](https://www.nowcoder.com/feed/main/detail/83326f3bcc5546b2b556373ad29a6d71) | 深信服；研发工程师背景；招聘阶段未明 | 面试 2026-08-21；帖约 2026-09；一面 | #CodingAgent #VLM #评测 #RL平台 #Harness #Codex。读到 PI 设计、Coding Agent、VLM benchmark、RL 平台/资源、模型与 Harness 评测、Codex。 | **A\***；作者吴好人第一人称，学校/研发工程师身份可见；本次主要读到公开题目段，页面正文加载不稳定，不能补写未读部分。 |
| 16 | [百度地图后端一面](https://www.nowcoder.com/feed/main/detail/e67a2d9e59b04ac28f8ccce362803fcb) | 百度地图；后端；实习/秋招阶段未明 | 面试 8.3；帖 2026-08-28；一面 | #RAG #召回评测 #BM25 #向量库 #Memory #高并发。读到相似度/topK/阈值、BM25/向量动态权重、自建框架、Memory 存储、开源复用、PGVector/Qdrant、API 关键词适配和高 QPS 优惠券系统。 | **A\***；作者 Python 求职者第一人称；搜索摘要和公开页面可核对主要字段，原页间歇不可读。 |
| 17 | [滴滴数开二面](https://www.nowcoder.com/feed/main/detail/630bb86ca8224183ad3de301a69ec199?sourceSSR=dynamic) | 滴滴；数据研发工程师；社招/实习阶段未明（作者身份为数据开发实习员工） | 面试 8.31；帖 2026-09-04；二面 | #RAG评测 #数据问答Agent #Skill #模型选择 #成本。读到 RAG 项目召回评估/落地、个人数据问答 Agent 与公司产品、Skill 质量、模型选择、AI 使用方式和预算。 | **A**；作者以第一人称记录；页面可读，阶段只按作者员工身份保守标注。 |
| 18 | [上海华力一面](https://www.nowcoder.com/feed/main/detail/deedd6c1b80a4fc6a60ea2d4a967861b?sourceSSR=dynamic) | 上海华力；智能制造系统工程师；**秋招/校招标签** | 面试 2026-09-17；帖 2026-09-17；一面 | #Agent架构 #知识库 #向量数据库 #Java后端。读到 Agent 架构、知识库、向量数据库选择、项目真实性和 Java 后端。 | **A**；作者小红不是绿第一人称；正文可读。 |
| 19 | [某小厂 AI Agent HR+技术面](https://www.nowcoder.com/feed/main/detail/10b2fcaf73d2401f8636bd0459e1cd08) | 某小厂；AI Agent / LLM 应用 / RAG；招聘阶段未明 | 面试 2026-09-04；帖 2026-09-04；HR+技术面 | #RAG #PDF解析 #分块 #召回 #Embedding成本 #Transformer #BM25。读到模型选择/项目挑战、RAG 数据规模、600GB–1TB 金融 PDF 的解析/分块/召回/Embedding 成本、Transformer/Attention/Cosine/BM25。 | **A**；作者牛客826994329号第一人称；页面正文可读。 |
| 20 | [海信秋招 AI 面](https://www.nowcoder.com/feed/main/detail/c7649a55d82b4728b966e74894029f1a) | 海信；数据开发；**秋招/校招** | 面试 2026-09-14；帖 2026-09-14；AI 面 | #数据Agent #Prompt #RAG指标 #数据开发。读到数据分析 Agent、Prompt 优化（作者自述提升 27%）、RAG 指标定义纠正和英语问题。 | **A**；作者 AAA野生原子弹批发第一人称；正文可读。 |
| 21 | [去哪儿 AI 面：Agent 应用开发-测试开发](https://www.nowcoder.com/feed/main/detail/4ef227c6b7c74394b487fbfa37c0f941?sourceSSR=enterprise) | 去哪儿；Agent 应用开发-测试开发；阶段未明 | 面试 2026-08-30；帖 2026-09-02；AI 面 | #Agent应用 #测试开发 #Java #Redis #部署 #Jenkins #AI工具。读到 Java、Redis、部署/Jenkins、测试和 AI 工具/模型使用；这是 AI 面记录，不把它误写成技术官面完整流程。 | **A\***；作者有头脑还高兴第一人称；正文可读。 |
| 22 | [字节 Agent 开发一面（实习）](https://www.nowcoder.com/feed/main/detail/6506d4b4addf447c8e2c135b5088cdc8) | 字节跳动；Agent 开发；**实习** | 面试日期未写；帖 2026-03-19；一面 | #Agent框架 #Memory #Context压缩 #RAG #MCP #Skill #OpenClaw #A2A #FastAPI #算法。读到框架/组件、记忆与上下文压缩、RAG、MCP/Skill 实现与渐进披露、FastAPI、OpenClaw、A2A、项目深挖和螺旋矩阵。 | **A\***；作者 w3b 以第一人称写实习一面；正文可读，面试日期未公开。 |

### 牛客条目的共同主题（样本归纳）

- **Coding Agent / Harness：** 任务状态、checkpoint、暂停/恢复、上下文压缩、工具权限、workspace 隔离、危险命令、子 Agent 权限和人工审批。
- **RAG 与评测：** 分块、混合召回、Rerank、RRF、阈值/topK、召回评测、线上 log 转 eval、Embedding 成本、数据更新和 Bad Case 回归。
- **工具协议：** Function Calling、MCP、Skill、A2A、SubAgent、schema/参数校验、重复工具、幂等和副作用。
- **传统工程：** Java/Python、Redis、MySQL/PostgreSQL、线程安全、MVCC、IO 多路复用、Linux/cgroup、Jenkins、算法题。

这些是 22 个新增牛客 URL 的交叉主题，不是任何公司的统一考纲。

---

## 2. V2EX：公开讨论中的一手复盘和回复

V2EX 条目不是牛客式的结构化面经，仍保留“作者实际说了什么”和“缺什么”两个边界。下表前四条是作者自己的求职/面试经历，可计为 A\* 一手补充；后两条是公开问答，只有回复者自述，不计入新增 A 数量。

| 原帖直链 | 公司 / 岗位 / 阶段 | 面试日期；发布日期；轮次 | 实际读到范围与主题 | 证据 |
|---|---|---|---|---|
| [从传统开发跳槽到 AI 应用开发](https://v2ex.com/t/1182394) | 多家公司；Python 后端转 AI 应用/Agent；**社招转岗** | 2025-12-31 发布；作者写“前 10 次 AI 面试失败，后有 2 个外包 offer”，未逐一给日期/轮次 | 第一人称职业复盘：面试官主要追问项目、技术选择、替代方案、性能和 Bad Case；从传统后端转 RAG/AI 应用的求职过程。没有逐轮题单，适合做“面经样本的字段缺失”案例。 | **A\***；正文可读，作者 WithoutSugarMiao 自述；不是单一公司完整面经。 |
| [前端求内推：DingTalk / Liblib 面试经历](https://global.v2ex.com/t/1192192) | DingTalk、Liblib；前端/AI 应用方向；阶段未明 | 2026-04-10 发布；作者未给具体面试日/轮次，DingTalk 提到二面 | 第一人称记录 DingTalk 二面 RAG 流程/评估、GraphRAG、Agent 质量/Memory，以及 Liblib 的 AI Coding/Vibe Coding 场景。 | **A\***；作者直接写自身面试经历，正文可读；公司和主题可核对，日期/岗位层级缺失。 |
| [想搞 AI 的小老板是真离谱](https://www.v2ex.com/t/1213610) | 某小型创业公司；AI Agent 开发；社招/阶段未明 | 2026-05-18 发布；面试日期/轮次未给 | 第一人称叙述 AI Agent 开发面试中被问“万亿参数模型部署”等，技术细节很少。只可作为岗位期望失配的案例，不能提炼题库。 | **A\***；正文可读，信息量低。 |
| [面试小 tip：用开源当缝合怪居然看不上自研](https://www.v2ex.com/t/1214616) | 某公司；AI 应用/后端；阶段未明 | 2026-05-22 发布；面试日期/轮次未给 | 第一人称失败面试复盘：LangChain/知识图谱与 RAG、自研 Java 框架等；作者讨论面试官对“开源拼装”和自研深度的看法。 | **A\***；正文可读，缺公司/轮次；不能把作者观点写成行业标准。 |
| [AI agent 工程师的岗位面试一般都考什么](https://www.v2ex.com/t/1198531) | Agent 工程师；公司和阶段未明 | 2026-03-16 发布；回复者未给面试日期/轮次 | OP 与回复者公开讨论 prompt/context/tool、MCP/Skill、上下文压缩、Memory、RAG、模型基础、缓存/延迟/成本、限制、eval；一位回复提到 Claude Code/Cursor/OpenCode 的比较问题。 | **B**；是多人的公开讨论，回复者有一手口吻但没有可核验公司/轮次；不计 A。 |
| [Agent 面试一般面什么啊](https://www.v2ex.com/t/1212999) | Agent 岗；公司/阶段未明 | 2026-05-15 发布；回复未给面试日期/轮次 | OP 有 AI-native 经验；回复提到项目深挖、RAG、Harness、Context、Memory、多 Agent、评测。 | **B**；回复者自述但字段不完整；不计 A。 |

---

## 3. B 站：个人复盘和教材化讲解

B站搜索结果里大量是“面试八股/真题讲解/培训题库”，没有候选人身份和面试事件，不能当一手面经。下面这条搜索索引提供了个人经历线索，但另一轮直接页面与公开 API 复核发现视频已不可用，因此降为 C、仅保留失效记录；详见 视频研究（原本地资料引用，未随公开版收录）。

| 视频直链 | 页面题名 / 发布信息 | 公司 / 阶段 / 轮次 | 实际读到范围 | 证据与限制 |
|---|---|---|---|---|
| [腾讯 AI Agent 暑期实习一面](https://www.bilibili.com/video/BV1EFGs6YEZi/) | 搜索索引标题“腾讯AIAgent暑期实习一面”；索引发布时间 2026-05-25，摘要写“202604 面试” | 腾讯；AI Agent 暑期实习；一面 | 仅搜索索引能看到 Agent/RAG/部署/微调等主题和上传者自述；直接页面显示“视频去哪了呢？”，公开 API 返回错误码 62002。 | **C，失效线索**；不能观看或转写，不能把摘要当成已核验面经；不计新增 A。 |

明确排除：BV1M6Mg6NEzK（字节 AI Agent 后端一面真题）、BV1H6846REH4、BV1Nkgn6hEug、BV16Sud6UEE3、BV1eRbr6mEJE、BV16TXpBhEkR 等页面主要是题库/教程/营销式“高频真题”，没有可核验候选人面试事件，因此不计面经。

---

## 4. 小红书：新增公开索引直链（正文未核验）

小红书原帖在本次访问中统一出现登录重定向 error_code=300017 或超时。下面的 ID 和题名来自公开的 [小红书 AI Agent 开发岗位面试调研报告](https://holynova.github.io/ai-agent-interview-report/xiaohongshu-ai-agent-interview-report.html) 的来源链接。该报告自述于 2026-07-10 生成并抓取 164 个去重结果、48 篇详情笔记；它是第三方索引，不能替代原帖。为避免把标题当成正文，所有条目都标为 C，第一人称状态写“未知”。已有清单中的 699c49...、69e4ff...、6a4f1b... 不重复列出。

| # | 原帖直链（search_result） | 索引题名 | 索引日期 | 公司 / 岗位（只按标题） | 主题线索（不等同正文） | 访问状态 |
|---:|---|---|---:|---|---|---|
| 1 | [美团｜AI Agent开发工程师面经](https://www.xiaohongshu.com/search_result/688d81180000000025016420) | 美团｜AI Agent开发工程师面经✅ | 2025-08-02 | 美团；AI Agent 开发工程师 | Agent 应用开发/面试 | 登录重定向，未读正文、作者、轮次；**C，第一人称未知** |
| 2 | [字节跳动 AI Agent 三轮技术面拿下 2-2](https://www.xiaohongshu.com/search_result/6a03b843000000000803d1a9) | 字节跳动 ai agent 三轮技术面拿下2-2 | 2026-05-13 | 字节跳动；AI Agent；三轮技术面 | Agent 技术轮次 | 超时；正文/作者未核验；**C，第一人称未知** |
| 3 | [2026 大模型 Agent 面试全攻略（下）](https://www.xiaohongshu.com/search_result/69b4f22b000000002300777d) | 2026大模型Agent面试全攻略（下） | 2026-03-14 | 公司未明；攻略 | Agent 面试汇总 | 超时；疑似整理文，不计一手；**C** |
| 4 | [字节跳动 AI 应用开发一面已过](https://www.xiaohongshu.com/search_result/6a4631320000000007029754) | 字节跳动ai应用开发一面已过 | 2026-07-02 | 字节跳动；AI 应用开发；一面 | 应用开发面试 | 登录重定向；正文/作者/问题未核验；**C，第一人称未知** |
| 5 | [第一次正式面试：多 Agent（未通过）](https://www.xiaohongshu.com/search_result/6a4cc903000000001503ef59) | 第一次正式面试 多agent(未通过) | 2026-07-07 | 公司未明；多 Agent；一面或技术面未知 | 多 Agent 项目/面试 | 登录重定向；**C，第一人称未知** |
| 6 | [字节 Agent 面试问 RAG 架构](https://www.xiaohongshu.com/search_result/6a38aa2f000000001503d551) | 字节Agent面试问RAG架构，我第一句就被打断 | 2026-06-22 | 字节跳动；Agent；轮次未明 | RAG 架构 | 超时；正文不可读；**C，第一人称未知** |
| 7 | [小红书 AI Agent 开发一面](https://www.xiaohongshu.com/search_result/69d214f10000000023004de5) | 小红书 AI Agent开发一面 | 2026-04-05 | 小红书；AI Agent 开发；一面 | Agent 应用/工程 | 超时；**C，第一人称未知** |
| 8 | [百度 AI Agent 开发一面](https://www.xiaohongshu.com/search_result/69db3df9000000001d01c80f) | 百度 AI Agent开发一面 | 2026-04-12 | 百度；AI Agent 开发；一面 | Agent 开发 | 超时；**C，第一人称未知** |
| 9 | [腾讯 AI 应用开发一面](https://www.xiaohongshu.com/search_result/69d9d3c8000000001a021c89) | 腾讯 ai应用开发一面 | 2026-04-11 | 腾讯；AI 应用开发；一面 | 应用开发 | 登录重定向；**C，第一人称未知** |
| 10 | [字节跳动 Agent 开发岗二面](https://www.xiaohongshu.com/search_result/6a1ab93a0000000035029e6f) | 字节跳动Agent开发岗二面 | 2026-05-30 | 字节跳动；Agent 开发；二面 | Agent 开发二面 | 超时；**C，第一人称未知** |
| 11 | [阿里云一面直接 AI Coding](https://www.xiaohongshu.com/search_result/69ccbf59000000002102db43) | 阿里云一面直接ai coding | 2026-04-01 | 阿里云；AI Coding；一面 | AI Coding/现场编程 | 超时；**C，第一人称未知** |

这些是“可追踪的新增原帖 ID”，不是正文证据。若未来浏览器登录且页面稳定，可把 C 条目升级为 A/B；在此之前不要在视频中引用具体题目。

---

## 5. 知乎、掘金：相关但非一手面经

这两类平台本次新增结果以教程、模拟面试、题目归纳和职业路线为主，保留直链方便后续找主题，但不计入新增一手数量。

| 平台 / 直链 | 日期 / 作者信息 | 内容与主题 | 证据 |
|---|---|---|---|
| [知乎：面试 AI Agent 岗位时，哪些问题能快速区分新手和高手？](https://www.zhihu.com/question/2049047173677987500/answer/2062637529636124587) | 2026 页面；回答者身份可见 | Agent 架构、工具、RAG、工程能力和面试判断的归纳，带推广性质；没有一场可核验面试事件。 | **B，二次整理/观点，不计 A** |
| [知乎：Agent 难点与面试路线](https://www.zhihu.com/question/2002427334347728106/answer/2042649660544774225) | 2026 页面；回答者身份可见 | 从 Agent 难点、学习路线和岗位准备角度整理主题；非个人逐轮面经。 | **B，方法论/推广，不计 A** |
| [知乎专栏：2026 年最新 AI Agent 面试（05）——RAG 基础应用](https://zhuanlan.zhihu.com/p/2063918418823230700) | 搜索结果显示 2026；本次正文 403 | RAG 基础与面试题方向；只能核对题名，不能核对文章正文。 | **C，正文未读，不计 A** |
| [掘金：AI Agent 面试模拟——RAG 追问](https://juejin.cn/post/7628074971524628515) | 2026-04-13；作者写与朋友模拟面试 | 作者模拟面试朋友，覆盖 RAG 项目讲解、分块、召回、重排和评测；不是求职者真实面试。 | **B，模拟面试** |
| [掘金：帮朋友模拟一场 RAG 项目面试](https://juejin.cn/post/7628818034996379674) | 2026-04-16；作者说明帮助朋友 | RAG 项目表述、追问和改进建议；可用于答题结构，不是原始面经。 | **B，模拟面试** |
| [掘金：AI Agent 面试表达/模拟框架](https://juejin.cn/post/7627818680535793716) | 2026；作者整理 | Agent 组件、项目追问和表达框架；教程/题库。 | **B，二次整理** |
| [掘金：RAG benchmark / 个人实验](https://juejin.cn/post/7689091429971902499) | 2026-09-26 | 个人 RAG 实验、检索与评测；不是面试事件。 | **B，相关项目资料** |

已有文件中的掘金 764964...、763473...、763193... 未在此重复。

---

## 6. 新增数量、标签汇总和限制

### 6.1 数量

- **新增牛客 A/A\* 原帖：22 条 URL。** 其中约 18 条能同时核对公司/岗位或阶段以及面试日期/轮次的大部分字段；其余是正文可读但年份、岗位层级或页面加载不完整的 A\*。
- **新增 V2EX A\* 一手职业/面试复盘：4 条 URL。** 它们是个人求职经历，但信息颗粒度不等同牛客逐轮面经。
- **可明确计作新增一手（A/A\*）的 URL 合计：26 条。** 按 URL 计数；一帖内的多场面试只算 1 条来源。
- B站失效线索 1 条、V2EX 混合讨论 2 条、知乎/掘金 7 条、小红书索引 11 条作为 B/C 辅助目录，**均不计入一手数量**。

### 6.2 主题标签

#CodingAgent、#Harness、#ContextEngineering、#Memory、#Checkpoint、#RAG、#HybridRetrieval、#Rerank、#Eval、#BadCase、#MCP、#Skill、#A2A、#SubAgent、#ToolSchema、#权限与安全、#VibeCoding、#AI编程、#Java/Python后端、#并发与数据库。

### 6.3 访问限制

1. 小红书 11 条新增来源只拿到公开索引的标题/ID/日期；原站在本次环境全部登录重定向或超时，不能据此复述问题，更不能假设是第一人称。
2. B站相关搜索结果多数是培训题库/教程；本文件保留的一个个人经历与讲解混合的线索已在直接页面/API 复核中失效，降级为 C。
3. 知乎、掘金新增内容主要是观点、题库或模拟面试；没有把“高频题”营销措辞当统计证据。
4. 部分牛客 feed/main/detail 页面有间歇性超时；表格只写成功读到的公开段落，未读的评论/付费区没有补写。TikTok 等已有文件中的付费专栏也没有重复采集。
5. “年份未明”“招聘阶段未明”“轮次未明”均保留原状。公开视频发布日、帖子发布日和面试发生日分开记录。
6. 这些来源是公开用户投稿样本，不代表公司统一流程；视频口播应使用“该帖记录了/这组样本出现”，不要使用“某公司必考”。
