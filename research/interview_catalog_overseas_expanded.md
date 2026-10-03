# 海外 Agent / Applied AI / AI coding / LLM Engineer 面经扩展目录

> 研究日期：2026-10-02（Asia/Shanghai）。本文件只收录在 `platform_overseas.md` 中没有重复出现的直接链接。优先保留能看到候选人具体轮次、题目或项目的材料；页面只有招聘广告、官方流程说明、泛泛的“如何准备”或普通 MLE 题目的材料不计入核心面经。

## 证据标签与统计

- **B｜候选人一手、已完成**：作者/发帖人明确说自己参加过面试，并给出已经完成的轮次或结果。
- **B-video｜候选人一手视频**：视频作者明确说自己完成过面试，但公开描述没有逐家公司展开。
- **B-comment｜准备帖中的一手完成回顾**：主帖是准备/提问，评论里另一个候选人补充了自己已完成的经历；不把主帖误算成完成面经。
- **B-adjacent｜邻近领域一手完成**：AI lab、ML infra 或通用 AI 岗位，和 Agent 应用开发有距离，单列，不计核心 Agent 应用数。
- **D｜第三方/匿名平台候选人报告**：PracHub、Jointaro、Exponent、Glassdoor 等平台的候选人报告或匿名记录；有直接页面，但不等同于作者本人可核验的一手文章。
- **C｜准备/提问/未完成**：正在约面、询问面试范围、只完成准备阶段，或没有完成结果。
- **A｜官方流程**：招聘方的 JD、官方面试指南或流程页；本次没有新增 A 行，已有官方资料仍见基础目录。

### 去重后的数量

| 集合 | 本文件新增来源数 | 计数口径 |
|---|---:|---|
| B 核心一手、已完成且有具体轮次 | **8** | 适合直接并入核心总表 |
| B-video 核心补充 | **1** | 一条跨公司 FDE 第一人称视频，算 1 个来源，不按公司拆成多条 |
| B-comment 核心补充 | **1** | OpenAI 准备帖内的另一位候选人已完成回顾，和准备主帖分开标注 |
| B-adjacent 邻近领域一手、已完成 | **2** | Anthropic ML infra / 通用 SWE，单列，不算 Agent 应用核心 |
| **新增去重的第一人称已完成记录合计** | **12** | `8 + 1 + 1 + 2`；其中核心主题相关为 10 条，邻近领域为 2 条 |
| D 第三方/匿名平台报告 | **10** | 独立列出，不并入第一人称数量 |
| C 准备/提问/未完成 | **4 个纯 C 来源** | 另有 1 个来源同时含 B-comment，见上表，不重复计数 |
| A 官方流程 | **0** | 不把官方流程当作面经 |

> 合并时，如果主表只接受“作者自己写的独立面经页面/视频”，先采用 B 的 8 条和 B-video 的 1 条；B-comment 另列为“评论中的完成回顾”。如果“第一人称已完成”按证据而不是页面类型计算，则本文件总数是 12 条。

## B｜核心：候选人一手、已完成并公开了具体轮次

| 日期 | 公司 / 岗位 / 级别 | 面试状态与结果 | 访问状态 | 具体主题 | 直接来源 |
|---|---|---|---|---|---|
| 2026-04-23 | Google / Forward Deployed Engineer / 级别未写 | **已完成**；结果未写 | Medium 正文可读 | AI/ML 实战轮要求设计类似创意写作 Agent 的智能系统；追问行为、推理、输出结构、权衡和评估；另有 DSA、Googleyness、recruiter screen | [候选人 Ajay Kumar 的一手回顾](https://medium.com/@trivajay259/i-interviewed-for-googles-forward-deployed-engineer-role-and-it-was-one-of-the-most-intense-12f2e676e91c) |
| 约 2026-04（页面显示 6mo） | Aiden AI / AI Engineer（帖文标题亦写 AI/ML Engineer）/ 级别未写 | **已完成并拿到 offer** | LinkedIn 帖文正文可读，登录提示不影响主体内容 | Hackathon 做 Multi-Agent Document Intelligence（AutoGen）；技术轮项目和后端；现场 DSA + GenAI：RAG、LLM integration、embedding、vector DB；经理/HR | [候选人 Chandra Kethan Sivarathri 的 LinkedIn 回顾](https://www.linkedin.com/posts/chandrakethan-sivarathri_aidenai-interviewexperience-softwareengineer-activity-7440412087337775104-5o8k) |
| 2024-12-11 | ZS / LLM Engineer / 级别未写 | **已完成**；结果未写 | GeeksforGeeks 全文可读 | Notebook RAG app、vector DB；最长重复子串、链表环；MMLU/HELM/HumanEval/BigBench；top-k/top-p/temperature、CoT、attention/encoder/decoder；AWS Bedrock、hybrid RAG、multimodal agents、MoE/LLAVA | [候选人一手面经（GeeksforGeeks）](https://www.geeksforgeeks.org/interview-experiences/zs-llm-engineer-interview-experience/) |
| 约 2025-12（Reddit 页面为相对日期） | Goldman Sachs / Applied AI Engineer / 级别未写 | **CoderPad 已完成**，先等待决定，后更新为拒绝；初帖是准备问题，更新部分是完成经历 | Reddit 帖子和更新可读 | 实际 CoderPad 主要是一道 DP；发帖人说明测试用例和 edge cases 已处理。这条保留是因为岗位本身是 Applied AI，但题目内容不应被夸大为 Agent 面 | [候选人 Applied AI Engineer 更新帖](https://www.reddit.com/r/leetcode/comments/1pexaw3/applied_ai_engineer_goldman_sachs_interview/) |
| 2026-04-12（LeetCode 页未显示日期；镜像索引标注该日） | EPAM Systems / Senior AI Engineer / Senior | **已完成三轮**；结果未写 | LeetCode 正文可读 | RAG 与 Agentic AI 技术深挖：financial RAG、多跳/跨文档/表格、GraphRAG、adaptive retrieval、HITL、异步；评估 recall/precision/MRR/faithfulness/grounding；hands-on + system design：FastAPI/Pydantic、重试/超时、MLflow、AKS、LangGraph ReAct/reducer、LangSmith | [候选人一手经历（LeetCode Discuss）](https://leetcode.com/discuss/post/7876633/epam-systems-senior-ai-engineer-intervie-4l0h/) |
| 约 2026（页面未显示日期） | Teradata / Senior AI Engineer / Senior，6.5 YOE | **已完成至少两轮**；结果未写 | LeetCode 正文可读 | DSA（Minimum Window Substring）；系统设计 RAG、规模化组件与 trade-off；同时说明日常 AI 工作 | [候选人一手经历（LeetCode Discuss）](https://leetcode.com/discuss/post/7704844/) |
| 页面未显示日期（访问日 2026-10-02） | Google / SWE 3 (L4), ML / L4 | **电话屏 + onsite loop 已完成**，进入 team match/HC，最终结果未写 | LeetCode 正文可读 | BFS；ML system design 设计 Q&A bot，从 baseline 到 RAG 和扩展；Googliness | [候选人 SnigdhaSrivatsava 的一手经历](https://leetcode.com/discuss/post/7016988/) |
| 约 2026（页面未显示日期） | Intuit / SWE-2 / 中级 | **已完成并被选中** | LeetCode 正文可读 | TPI + 四轮 onsite；用 Python Flask/Docker 做 localized LLM API；DB/graph DB；AI 轮考测试与指标、RAG、system prompt、temperature；另有 HM | [候选人一手经历（LeetCode Discuss）](https://leetcode.com/discuss/post/7313117/intuit-interview-experience-for-swe-2-se-6t8a/) |

### B-video｜核心补充：一手视频但缺少逐家公司颗粒度

| 日期 | 公司 / 岗位 / 级别 | 面试状态与结果 | 访问状态 | 具体主题 | 直接来源 |
|---|---|---|---|---|---|
| 2026-08-18 | ElevenLabs、Palantir、Google、OpenAI 及 AI startups / Forward Deployed Engineer / 级别未写 | **作者称自己完成了 15 场 FDE 面试**；视频描述没有逐一给出各公司结果 | YouTube 页面及描述可访问；完整轮次需播放视频 | 真实 FDE 面试中反复出现 technical problem solving/coding、system design、AI、沟通、客户问题；适合作为跨公司目录入口，不应拆成 15 条公司面经 | [Anu Sharma：I gave 15 Forward Deployed Engineer Interviews](https://www.youtube.com/watch?v=VnIDWlOzb6s) |

## B-comment｜核心补充：准备帖里嵌入的已完成回顾

| 日期 | 公司 / 岗位 / 级别 | 面试状态与结果 | 访问状态 | 具体主题 | 直接来源与限制 |
|---|---|---|---|---|---|
| 约 2026-09 | OpenAI / Applied AI；评论中另称 AI Deployment Engineer / L6（Principal/Staff） | **评论作者称自己已完成 loop，约两周走完**；主帖本人只是准备/提问 | Reddit 主帖可读；完成回顾位于评论/搜索定位内容，不把主帖当作已完成面经 | coding 是真实工作任务：用 live API 构造 LLM loop，可用 agent/IDE（评论作者使用 Codex）；不是传统 LeetCode | [OpenAI SWE 面试准备帖及评论](https://www.reddit.com/r/leetcode/comments/1qmyhnm/advice-for-preparing-for-openai-swe-interview/)。**归类：主帖 C，评论 B-comment；评论级信息不要和主帖作者身份合并。** |

## B-adjacent｜邻近领域一手：保留但不计入核心 Agent 应用数

| 日期 | 公司 / 岗位 / 级别 | 面试状态与结果 | 访问状态 | 具体主题 | 直接来源 |
|---|---|---|---|---|---|
| 页面未显示日期（约 2026） | Anthropic / ML Infrastructure / 约 5 YOE，级别未写 | **电话屏已完成，之后被拒** | LeetCode 正文可读 | AI safety；web crawler BFS；multithreading/thread pool/asyncio | [Anthropic ML infrastructure 一手经历](https://leetcode.com/discuss/post/7530004/)。这是 AI lab/infra 经验，未出现 Agent 应用设计，不能并入核心 Agent 轮次。 |
| 2026-06-02（文中称面试发生于 2025） | Anthropic / SWE / L4 | **已完成并称收到 offer** | Medium 会员文章，公开预览正文可读，完整内容受会员限制 | readable code、并发、debugging、系统权衡、安全导向的产品判断；没有可核验的 LLM/Agent 应用题细节 | [Anthropic L4 SWE interview experience](https://medium.com/@trivajay259/anthropic-swe-interview-experience-l4-remote-acf3f58268b8)。保留作 AI lab 邻近样本，不算核心 Agent/LLM Engineer 数。 |

## D｜第三方转载、匿名平台或聚合候选人报告

以下链接有具体轮次，仍单列为 D：页面由平台编辑、匿名投稿或聚合多个候选人，不能与 B 类作者一手文章等量合并。

| 面试日期 / 页面日期 | 公司 / 岗位 / 级别 | 状态 | 访问状态 | 具体主题 | 直接来源 / 证据性质 |
|---|---|---|---|---|---|
| 面试 2026-05；发布 2026-08-25 | Distyl / AI Engineer / Senior+ | 结果未明确 | PracHub 公开页面摘要可读 | 允许使用 AI 的 take-home；Whisper streaming、多说话人和速度；LLM chatbot streaming、rate-limit fallback、扩展；部署、版本管理 | [PracHub Distyl Senior+ AI Engineer report](https://prachub.com/interview-experiences/distyl-seniorplus-ai-engineer-interview-experience-a-whisper-streaming-take-home-then-system-design-and-a-deploy-deep-dive)。第三方整理。 |
| 2025-07-01 | Mistral AI / AI Engineer / 级别未写，Paris | **No offer** | Jointaro 候选人报告页面可访问 | state of AI；PyTorch multi-head self-attention/causal mask；LLM fundamentals 与 FSDP、ZeRO、tensor/pipeline/data parallel；pair programming/debugging | [Jointaro Mistral AI AI Engineer report](https://www.jointaro.com/interviews/companies/mistral-ai/experiences/ai-engineer-paris-july-1-2025-no-offer-negative-1ac7b2a9/)。平台候选人报告。 |
| 约 2025（页面写一年前） | Scale AI / Forward Deployed Engineer / 级别未写，美国 | **Offer；难度高** | Exponent 经验页可访问 | referral；hard OA；recruiter、nontechnical/coding；onsite 含 credo、coding、system design、debug 大型 repo、HM；用 SWE bar 判断 FDE fit | [Exponent Scale AI FDE report](https://www.tryexponent.com/experiences/scale-ai-forward-deployed-engineer-interview-f232b4?returnPath=%2Fexperiences)。第三方候选人报告。 |
| 约 2026（页面写八个月前） | Scale AI / New Grad SWE / L3 | **Rejected** | Exponent 经验页可访问 | HackerRank、tech screen、system design + debugging；准备建议涉及 RAG、token cost、cache/DB；实际 debug modular code | [Exponent Scale AI New Grad SWE report](https://www.tryexponent.com/experiences/scale-ai-software-engineer-interview-b83485)。岗位是 SWE，只有部分 AI backend 主题，保留但不算 FDE/Agent 面经。 |
| 面试 2026-03；发布 2026-08-24 | Scale AI / Software Engineer / 级别未写 | 结果未明确 | PracHub 公开页面摘要可读 | 多文件 codebase debug；调用 LLM API、prompt、response validation、生产问题；system design、behavioral | [PracHub Scale AI SWE report](https://prachub.com/interview-experiences/scale-ai-software-engineer-interview-debug-a-real-codebase-then-an-llm-api-round)。第三方整理。 |
| 页面未显示日期 | LangChain / Deployed Engineer / 级别未写 | 结果未明确 | Exponent 经验页可访问 | agents、coding assistants、observability、evaluation、客户采用；适合 FDE/Deployed Engineer 主题目录 | [Exponent LangChain Deployed Engineer report](https://www.tryexponent.com/experiences/lang-chain-forward-deployed-engineer-interview-8c2ffb)。第三方候选人报告。 |
| 面试 2026-06；发布 2026-08-25 | LangChain / Software Engineer / Senior+ | 结果未明确 | PracHub 公开页面摘要可读 | take-home 优化 benchmark/S3 JSON API；LangSmith observability system design：tokens、metrics、latency、alerts、anomaly、late events、duplicates | [PracHub LangChain Senior+ SWE report](https://prachub.com/interview-experiences/langchain-seniorplus-software-engineer-interview-experience-take-home-optimization-then-three-onsite-rounds-in-one-day)。第三方整理。 |
| 面试 2026-07；发布 2026-08-24 | Google / Forward Deployed Engineer / 级别未写 | **候选人未通过/发帖表达挫败** | PracHub 公开页面摘要可读 | agentic system design：扩展、安全、无限循环；coding 从 meeting/parking 变为 2D DP | [PracHub Google FDE report](https://prachub.com/interview-experiences/google-forward-deployed-engineer-interview-experience-agentic-system-design-and-a-coding-round-that-turned-into-2d-dp)。第三方整理。 |
| 约 2026-09（页面写一月前） | Google / Forward Deployed Engineer / L4 或 mid-level | **结果进行中** | Exponent 经验页可访问 | abstract system design，强调澄清需求；只保留岗位和轮次层面的公开信息 | [Exponent Google FDE report](https://www.tryexponent.com/experiences/google-forward-deployed-engineer-interview-1019ab)。第三方经验页，不与 Google FDE Medium 一手回顾合并。 |
| 页面更新 2026-09-24；包含 2026-07/08/09 多条匿名记录 | Perplexity AI / Software Engineer、Infrastructure Engineer、Staff SWE / 多级别 | **页面内结果混合：no offer、positive、declined 等** | Glassdoor 聚合页可访问；匿名条目不一定能看到作者身份 | 可见记录包括 coding、system design、LLM application 经验（tokenizer、state machine、in-memory filesystem）、infrastructure/deep dive；条目日期和级别各异 | [Glassdoor Perplexity AI Interview Questions](https://www.glassdoor.com/Interview/Perplexity-AI-Interview-Questions-E8515634.htm)。匿名聚合页，不能当作单一候选人的完整面经。 |

## C｜准备/提问/未完成：单独保留，不能当作完成面经

| 日期 | 公司 / 岗位 / 级别 | 当前状态 | 访问状态 | 公开内容 | 直接来源 |
|---|---|---|---|---|---|
| 页面未显示日期（约 2026） | Anthropic / Software Engineer，级别未写 | **进行中，未完成 onsite** | LeetCode 正文/摘要可读 | CodeSignal OA；recruiter 的 why Anthropic/mission；phone screen 为 Stack Trace；发帖人询问后续准备 | [Anthropic OA + Coding 准备帖](https://leetcode.com/discuss/post/7559983/) |
| 2026-05-21 | Google / Forward Deployed Engineer / L4-L5 | **准备/询问他人经历**；没有可核验的完整轮次回顾 | Reddit 主帖可读 | 发帖人询问 FDE L4/L5 面试经验；评论只提供零散 recruiter/no-update 信息 | [Google FDE interview asking thread](https://www.reddit.com/r/FAANGrecruiting/comments/1tjt9if/google_forward_deployed_engineer_interview/) |
| 2026-07 | Accenture / Custom Software Engineer：AI Agents & Workflow Integration / 级别未写 | **主帖是即将参加 Skills Interview**；评论含零散回顾，未形成同一人的完整已完成面经 | Reddit 帖子可读 | JD 提到 Google ADK、LangChain/LangGraph、CrewAI/AutoGen、RAG/vector DB/eval/observability/MCP/cloud；评论提到 LLM、RAG、hallucination、prompt injection、agents 等 | [Accenture AI Agents interview thread](https://www.reddit.com/r/accenture_india/comments/1uyq6it/accenture_custom_software_engineer_interview_ai/)。主帖 C；评论只作线索，不计 B。 |
| 页面未显示日期 | Qualified Health PBC / Senior Backend/Platform Engineer / Senior | **即将 onsite，发帖人询问系统设计范围** | LeetCode 帖子可读 | GenAI healthcare/agentic workflows、LLM platform、monitoring/security/PHI；没有已完成结果 | [Qualified Health PBC agentic workflow prep](https://leetcode.com/discuss/post/8378543/) |

## A｜官方流程与重复项处理

- 本次**没有新增官方流程行**。OpenAI interview guide、Amazon/Google/Microsoft/Anthropic 的官方 JD 或招聘流程已经在 `platform_overseas.md` 中；它们说明官方流程，不能替代候选人面经。
- 已发现但没有再写入本文件的重复/低相关材料包括：基础目录已经收录的 OpenAI Applied Engineering Reddit、Anthropic/Glassdoor、OpenAI 面试视频；普通 LinkedIn AI Engineer、Google L4 AI/ML clustering、通用 Amazon SDE、通用 Perplexity SWE coding 等。它们没有被误并入 Agent 应用开发核心计数。
- `Goldman Sachs Applied AI Engineer` 保留在 B 是因为发帖人后来明确更新了已完成的 CoderPad 和拒信；但其实际题目主要是 DP，所以主题栏明确标成“Applied AI 职位、coding-heavy”，不把它包装成 Agent 设计面经。
- `Google SWE 3 (L4) ML` 只因公开内容明确出现 Q&A bot/RAG system design 才保留；普通聚类、概率、模型训练等 MLE 面经不在本目录核心计数中。
