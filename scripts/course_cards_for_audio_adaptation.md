# Agent课程口播事实卡

核对日期：2026-10-03。卡片按新口播稿的20组资源排列，供改稿、字幕和简介链接复核；这是事实提要，不是口播稿，也不是学习体验评价。依据仅限本地课程研究材料，没有重新大范围联网。课程与项目只做过不同范围的静态资料审阅，不能写成全部学完、全部实测或全部免费。

## 按资源形态分组

| 口播组 | 资源形态 | 口播组 | 资源形态 |
|---:|---|---:|---|
| 1、7 | 中文教材/项目指南 | 2–6、8–10、13–18、20 | 课程、系列或学习路径 |
| 11 | Anthropic Academy多门课程入口 | 12 | OpenAI官方学习路线与文档 |
| 19 | Berkeley公开课与研究讲座 |  |  |

## 第一组：先弄懂Agent怎么工作

### 1. Datawhale《从零开始构建智能体》（Hello-Agents）｜教材

- **学什么：**16章分五部分，覆盖Agent与LLM基础、ReAct/规划/反思、框架、记忆与RAG、上下文、MCP/A2A/ANP、评估及综合项目。
- **合适谁 / 可举例：**想读中文系统教材、已有一些Python和模型API基础的人。第一章天气查询后再搜景点，可说明工具请求、实际执行和Observation回填的分工；第4章有ReAct代码。
- **前提与边界：**公开教材与代码仓库；部分例子需要模型、搜索、数据库或其他API凭证。研究基于固定提交的文本/代码静态审阅，不代表运行成功或读完社区全部项目。
- **原链接 / 研究依据：**[GitHub教材](https://github.com/datawhalechina/hello-agents)；[课程结构与学习路径](../research/agent_courses/providers/datawhale/curriculum.md)、[证据范围](../research/agent_courses/providers/datawhale/evidence.md)。

### 2. DeepLearning.AI《Agentic AI》｜课程

- **学什么：**Andrew Ng主讲；五个模块覆盖工作流、反思、工具使用、评估与优化、规划和多Agent协作。官网目录信息记为中级、31节视频、7个代码示例、约7小时45分。
- **合适谁 / 可举例：**已经知道一些Agent名词、想学任务怎样拆分并按失败原因改进的人。Research Agent从直接写作演变成列提纲、搜索、草稿、评估和改写，是代表例子。
- **前提与边界：**官方标为Intermediate；有Python与模型调用基础会更适合跟代码。课程页与社区目录、视频转录的获取范围不同；没有据此声称完成平台内作业或运行全部代码，价格和登录后的访问范围未核实。
- **原链接 / 研究依据：**[官方课程](https://www.deeplearning.ai/courses/agentic-ai)；[课程章节地图](../research/agent_courses/providers/deeplearning_ai/curriculum.md)、[获取范围与证据](../research/agent_courses/providers/deeplearning_ai/evidence.md)、[短课补充中的课程信息](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)。

### 3. Hugging Face《Agents Course》｜课程

- **学什么：**从Agent定义、工具和Thought–Action–Observation循环开始，再分别学smolagents、LlamaIndex和LangGraph；之后用晚宴助理做Agentic RAG，并以GAIA子集作为最终项目入口。
- **合适谁 / 可举例：**有Python/LLM基础，想学基本循环并比较多种框架的人。Alfred晚宴助理组合宾客资料检索、天气和搜索工具；LangGraph章节用条件边分流邮件。
- **前提与边界：**课程有公开网页和代码；跑模型、Space或提交GAIA作业可能需要账号、推理资源或外部环境。中文页面可读，但欢迎页部分信息旧于英文目录；本轮未跑完notebook/Space或完成最终项目。
- **原链接 / 研究依据：**[英文课程](https://huggingface.co/learn/agents-course/en/unit0/introduction)；[中文入口](https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction)；[章节地图](../research/agent_courses/providers/huggingface/curriculum.md)、[来源与范围](../research/agent_courses/providers/huggingface/evidence.md)。

### 4. Google × Kaggle《5-Day AI Agents Intensive》（2025版）｜自学课程指南

- **学什么：**五天主题是Agent入门、工具与MCP、会话和记忆、可观测性与评测、A2A和生产部署；包含Gemini/ADK代码实践与capstone入口。
- **合适谁 / 可举例：**希望沿着五个主题和相应实验集中入门的人。可以举工具调用加人工批准、跨会话记忆或最终Notebook/Colab/GitHub提交。
- **前提与边界：**2025年直播活动已结束，材料转为Kaggle自学指南；指南要求Kaggle账号（账号需手机验证），代码实验可能要Google AI Studio API key。2026 Vibe Coding版是另一版目录，新增Skills、安全等，不能与2025版拼成同一课程。
- **原链接 / 研究依据：**[2025自学指南](https://www.kaggle.com/learn-guide/5-day-agents)、[2026版](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding)；[厂商课程核验](../research/agent_courses/additional_vendor_courses.md)、[扩充选择表](../research/agent_courses/expanded_course_choices.md)。

### 5. Vanderbilt / Coursera《AI Agents and Agentic AI in Python》｜三门课系列

- **学什么：**Jules White主讲的Python Agent系列，课程组合包括Python Agent实现、Prompt Engineering for ChatGPT、Python Agent架构；架构内容涉及工具发现/函数调用、多Agent、共享记忆、分阶段执行和可逆动作。
- **合适谁 / 可举例：**想用Python手写和理解Agent部件的人。可举“怎样发现工具、怎样组织共享记忆、怎样让多个Agent分步协作”。
- **前提与边界：**基本Python能力是官网列明的要求。它是三门组合，提示工程课不等于一门Agent编程课；报名、作业和证书的完整访问费用要以Coursera账号页面为准。
- **原链接 / 研究依据：**[Coursera系列](https://www.coursera.org/specializations/ai-agents-python)；[框架与大学课程补充](../research/agent_courses/additional_framework_university_courses.md)。

### 6. Microsoft《AI Agents for Beginners》｜开源课程

- **学什么：**18课加环境准备，覆盖Agent框架、工具、Agentic RAG、可信与安全、多Agent、规划、上下文、记忆、生产评估、协议和部署。
- **合适谁 / 可举例：**已有小应用、想用目录补齐工程主题的人。第6课展示执行前审批/风险等级/审计记录；多Agent章节有客服流程示例。
- **前提与边界：**仓库公开；当前研究快照（2026年7月迁移后）使用Microsoft Agent Framework与Azure OpenAI Responses API。主配置涉及Python 3.12+及Azure/Foundry资源；另有本地或其他提供方路径。配置模型资源可能产生费用，不能把公开仓库等同免费运行环境。
- **原链接 / 研究依据：**[官方GitHub课程](https://github.com/microsoft/ai-agents-for-beginners)；[逐课与代码地图](../research/agent_courses/providers/microsoft/curriculum.md)、[README和证据目录](../research/agent_courses/providers/microsoft/evidence.md)。

## 第二组：围绕一个项目或框架学习

### 7. Datawhale《Generic Agent 使用指南》｜中文项目指南

- **学什么：**按应用指南、原理篇、案例篇组织；从安装和使用进入浏览器能力、记忆与技能，再讲Agent循环、工具集、分层记忆、上下文压缩和案例。
- **合适谁 / 可举例：**想先用一个具体Agent，再回头拆解其结构的中文读者。可举“先看记忆如何保存，再读分层记忆/上下文压缩的架构章节”。
- **前提与边界：**项目说明面向无基础读者，读实现有基本Python会更方便。GitHub和在线正文公开；项目自标Beta，这是单个项目的使用与架构指南，不是通用框架横评；项目方对效率的描述未独立验证。
- **原链接 / 研究依据：**[GitHub项目与目录](https://github.com/datawhalechina/hello-generic-agent)、[在线正文](https://datawhalechina.github.io/hello-generic-agent/)；[开放课程补充](../research/agent_courses/additional_open_courses.md)、[扩充选择表](../research/agent_courses/expanded_course_choices.md)。

### 8. freeCodeCamp频道发布、Bappy主讲《Agentic AI – Complete Course for Beginners》｜长视频与代码

- **学什么：**约24小时16分视频；异步Python与Pydantic之后进入LangChain单/多Agent、LangGraph工作流，以及RAG、记忆、人机介入、监控和部署项目。
- **合适谁 / 可举例：**有基本Python、想跟长视频看代码和项目逐步展开的人。代码仓库包含Advanced RAG、异步编程、多Agent和LangGraph项目目录。
- **前提与边界：**视频由Bappy授课、freeCodeCamp.org频道发布，不应称为freeCodeCamp自编课。视频和代码公开；API、数据库、模型调用和云部署可能需要账号或费用，未运行项目。
- **原链接 / 研究依据：**[YouTube课程](https://www.youtube.com/watch?v=Zy7EXDONlTY)、[代码仓库](https://github.com/entbappy/Complete-Agentic-AI-Course)；[开放课程补充](../research/agent_courses/additional_open_courses.md)。

### 9. LangChain Academy《Introduction to LangGraph – Python》｜课程

- **学什么：**由State、Node、Edge和条件路由进入消息处理、状态保存、记忆、人工介入、并行、子图、长期记忆与部署；官方页记录55节、约6小时视频。
- **合适谁 / 可举例：**已会模型与工具调用、想理解程序如何控制步骤、状态和人机交接的人。示例在tools节点执行前暂停，确认后再继续；另有SQLite外部记忆和Research Assistant。
- **前提与边界：**README要求Python 3.11–3.13、Jupyter及模型/API凭证；官方页标注课程免费，但不代表API、部署或外部模型免费。静态检查过课程仓库和notebook，没有运行。
- **原链接 / 研究依据：**[官方课程](https://academy.langchain.com/courses/intro-to-langgraph)、[课程仓库](https://github.com/langchain-ai/langchain-academy)；[章节地图](../research/agent_courses/providers/langchain/curriculum.md)、[获取范围](../research/agent_courses/providers/langchain/evidence.md)。

### 10. LangChain Academy《Project: Ambient Agents with LangGraph》｜项目课

- **学什么：**六个模块围绕邮件管理助手，覆盖LangGraph基础、构建、评测、人工介入、记忆和部署。
- **合适谁 / 可举例：**希望用一项具体应用把多个工程部件串起来的人。邮件处理任务可以引出何时自动继续、何时转人工，以及如何评测和记忆。
- **前提与边界：**官网将课程标为免费；代码、模型和邮件服务的账号/运行要求仍需另查。课程案例未逐项执行，不能说已跑通自动处理邮箱。
- **原链接 / 研究依据：**[官方课程](https://academy.langchain.com/courses/ambient-agents)、[官方项目课程说明](https://academy.langchain.com/collections/project)；[框架工程与大学课程补充](../research/agent_courses/additional_framework_university_courses.md)。

## 第三组：厂商自己的课程、路线与文档

### 11. Anthropic Claude Academy：Claude Platform 101、Building with the Claude API、Introduction to MCP｜三门独立课程

- **学什么：**Platform 101介绍平台、Agent loop、工具、Skills、MCP和上下文；Claude API课程从请求、提示与评测延伸到工具循环、RAG和MCP实现；MCP课程讲客户端、服务端、工具、资源和提示模板。
- **合适谁 / 可举例：**想理解Anthropic接口约定、或准备使用Claude API/MCP做项目的人。Platform 101的Agent loop页举天气工具往返；API课程的Agents and tools页以保修信息缺失时追问购买日期为例。
- **前提与边界：**它们是三门课程，不是一门完整通用Agent课。2026-10-03快照有90个公开教学文字页（13/67/10），视频没有下载或逐课观看；运行API/MCP项目需环境、API key，调用费用另计，测验/徽章正文未获取。
- **原链接 / 研究依据：**[Platform 101](https://academy.claude.com/courses/claude-platform-101)、[Claude API课程](https://academy.claude.com/courses/building-with-the-claude-api)、[MCP课程](https://academy.claude.com/courses/introduction-to-model-context-protocol)；[Anthropic课程地图](../research/agent_courses/providers/anthropic/curriculum.md)、[逐课索引](../research/agent_courses/providers/anthropic/lesson_index.md)、[获取边界](../research/agent_courses/providers/anthropic/evidence.md)。

### 12. OpenAI《Building agents》学习路线与Agents SDK文档｜官方参考

- **学什么：**路线从Agent定义、最小工具Agent和运行循环，走到状态、多Agent handoff、agent-as-tool、人工审批、trace和评估。
- **合适谁 / 可举例：**项目明确使用OpenAI Agents SDK，想按具体接口查实现的人。Quickstart用History tutor和函数工具；编排文档对比handoff与manager把专家当工具。
- **前提与边界：**这是路线和开发文档，不是按章节完成的课程，也没有课程证书。研究快照有12篇页面正文完整、6个链接只取到导航/错误；未运行SDK/API。模型版本、API可用性与费用以当前官方页面为准。
- **原链接 / 研究依据：**[Building agents track](https://developers.openai.com/tracks/building-agents)、[Agents SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk)、[Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)；[学习路线地图](../research/agent_courses/providers/openai/curriculum.md)、[证据边界](../research/agent_courses/providers/openai/evidence.md)。

## 第四组：针对具体开发问题的专题

### 13. LangChain Academy《Foundation: Introduction to Deep Agents》｜课程

- **学什么：**五模块讲Agent构建、执行环境、上下文管理、任务委派和综合项目；目录涉及MCP、checkpointer、人工介入、文件系统、沙箱、上下文卸载、Skills、记忆和子Agent。
- **合适谁 / 可举例：**已有基本工具循环，想看支持Agent运行的程序怎样管理文件、上下文和子任务的人。综合项目有销售助手和本地部署。
- **前提与边界：**官网标为免费，模型和运行环境成本另计；Python材料可读，目录有TypeScript准备课但仓库实现并非全都对齐。按目录静态审阅，未验证部署。
- **原链接 / 研究依据：**[官方课程](https://academy.langchain.com/courses/foundation-introduction-to-deepagents)、[代码仓库](https://github.com/langchain-ai/lca-deepagents)；[框架工程与大学课程补充](../research/agent_courses/additional_framework_university_courses.md)。

### 14. LangChain Academy《Introduction to Agent Observability & Evaluations》｜课程

- **学什么：**运行观测、测试与评估、提示词开发、人工反馈和生产观测；包含数据集、评估器、实验、成对比较、标注队列和在线评估。
- **合适谁 / 可举例：**已经有Agent，希望用一组固定问题比较改动前后的结果、定位失败发生在哪一步的人。
- **前提与边界：**课程围绕LangSmith；账号额度和外部模型费用需要另查。当前课程标题和旧URL不完全一致，录制字幕按当前标题标注；未运行课程实验。
- **原链接 / 研究依据：**[官方课程（旧URL）](https://academy.langchain.com/courses/intro-to-langsmith)；[框架工程与大学课程补充](../research/agent_courses/additional_framework_university_courses.md)。

### 15. Hugging Face《MCP Course》｜协议专题课程

- **学什么：**Unit 1讲术语、架构、通信、SDK、clients、HF server和Gradio集成；后续目录有Gradio/Continue/Tiny Agents、GitHub Actions、Slack通知和PR Agent项目。
- **合适谁 / 可举例：**已经理解工具调用，想学习host、client和server如何通过MCP连接的人。可举Gradio服务接入客户端或PR工作流连接GitHub Actions。
- **前提与边界：**MCP是与Agents Course分开的课程；目录和仓库可查，但没有逐页审阅、运行服务或确认各项目当前兼容性。连接协议不自动完成授权、规划或写操作审批。
- **原链接 / 研究依据：**[官方英文课程](https://huggingface.co/learn/mcp-course/en/unit0/introduction)；[MCP补充分析](../research/agent_courses/providers/extras/analysis.md)。

### 16. NVIDIA DLI：RAG课程与Agentic AI应用课程｜两个不同目录入口

- **学什么：**《Building RAG Agents with LLMs》公开目录包括LLM接口、LangChain/LCEL、对话状态、长文切分与摘要、embedding、护栏、向量RAG和LLM-as-a-Judge，目标案例是研究论文集问答；《Building Agentic AI Applications with LLMs》简介提到用LangGraph与NVIDIA NIM构建长程推理等应用。
- **合适谁 / 可举例：**前者适合有Python基础、想做文档/论文检索助手的人；后者可作为NVIDIA生态Agent应用方向的候选。
- **前提与边界：**RAG讲师版标8小时、要求中级Python及入门深度学习，PyTorch经验建议具备。自学/讲师版本和页面价格有冲突；历史PDF曾列免费，当前页面有$90自学版与联系询价讲师版。第二门公开详情不足，不能作完整目录评价。
- **原链接 / 研究依据：**[RAG讲师课](https://www.nvidia.com/en-au/training/instructor-led-workshops/building-rag-agents-with-llms/)、[Generative AI学习路径](https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/)、[Agentic AI课程](https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/)；[厂商课程核验](../research/agent_courses/additional_vendor_courses.md)。

### 17. IBM《Agentic AI in Practice》｜学习路径

- **学什么：**一条路径包含1门课程、9个教程、四段内容：Agent基础；CrewAI/LangChain；自定义工具、ReAct和LangGraph；领域多Agent与RAG。
- **合适谁 / 可举例：**想从一个厂商路径里挑具体应用的人。目录列出CrewAI客服、数学工具Agent、医疗AG2/AutoGen、PydanticAI客服和LangGraph+Docling Agentic RAG等例子。
- **前提与边界：**IBM页面标为Express Learning / No cost，但未列统一先修条件，也未展示所有教程的完整环境或代码。资产栏的30至180 hours单位含义不明，不宜当学习时长。
- **原链接 / 研究依据：**[IBM路径](https://www.ibm.com/training/learning-path/agentic-ai-in-practice-1058)；[厂商课程核验](../research/agent_courses/additional_vendor_courses.md)。

### 18. DeepLearning.AI三门合作讲师短课｜三个独立课程

- **学什么：**《AI Agents in LangGraph》从手写Agent到搜索、持久化、流式输出和人工介入，项目为Essay Writer；《Multi AI Agent Systems with crewAI》讲角色、工具、顺序/并行/层级协作和记忆；《Building Coding Agents with Tool Execution》讲生成并运行代码、文件操作和沙箱。
- **合适谁 / 可举例：**分别适合想学LangGraph流程、业务多Agent分工、或Coding Agent代码执行的人。后两者项目例子有客服/活动策划、CSV分析/Next.js生成。
- **前提与边界：**它们是三门单独短课，不是Andrew Ng主讲的《Agentic AI》子章节；分别由Harrison Chase与Rotem Weiss、João Moura、Tereza Tizkova与Francesco Zuppichini主讲。页面列1:32、2:41、1:21；中级Python/基本编程要求依课程而异。代码例子不代表本次运行验证，API与E2B沙箱可能产生费用。
- **原链接 / 研究依据：**[LangGraph短课](https://www.deeplearning.ai/courses/ai-agents-in-langgraph)、[crewAI短课](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai)、[Coding Agents短课](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution)；[DLAI短课补充](../research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md)。

## 第五组：大学公开课与研究讲座

### 19. Berkeley《LLM Agents MOOC》与《Agentic AI》系列公开课｜研究讲座

- **学什么：**已保存F24、SP25和F25不同学期入口。F24大纲覆盖推理、ReAct/WebShop、多模态Agent、RAG、DSPy、SWE-agent/OpenHands、企业工作流、机器人、评测和安全。
- **合适谁 / 可举例：**有基础、想围绕具体研究问题扩展视野的人。可挑编程Agent评测或安全讲座，再沿课件和推荐阅读继续查。
- **前提与边界：**不同学期课程不能拼作一个目录；本地研究主要深读F24大纲，没看完所有讲座、完成测验或运行Lab。公开课件/录像链接不保证外链、课堂与实验都能完整访问。
- **原链接 / 研究依据：**[F24](https://rdi.berkeley.edu/llm-agents-mooc/f24)、[SP25](https://rdi.berkeley.edu/llm-agents-mooc/sp25)、[F25](https://rdi.berkeley.edu/agentic-ai/f25)；[课程结构](../research/agent_courses/providers/berkeley/curriculum.md)、[证据边界](../research/agent_courses/providers/berkeley/evidence.md)。

### 20. CMU 11-768《AI Agents》（Fall 2026）｜研究生课程

- **学什么：**工具使用、长上下文、规划、记忆、训练、安全、人机交互及编码/GUI Agent；作业方向有coding-agent harness、评测框架和Agent训练。
- **合适谁 / 可举例：**有较强Python、AI/ML与语言模型背景，想接触研究生层面问题的人。可用“搭harness、设计eval、实现训练方法”说明它与应用入门课的差别。
- **前提与边界：**截至2026-10-03学期正在进行。课程站公开日程、部分课件/录像链接，但不等于完整MOOC，作业和课堂访问以课程站为准；没有完成作业或观看全部讲座。
- **原链接 / 研究依据：**[课程网站](https://www.cmu-agents.com/)、[录像播放列表](https://www.youtube.com/playlist?list=PLSN0qpDfUvTM)、[课程目录和适用起点](../research/agent_courses/additional_open_courses.md)、[扩充选择表](../research/agent_courses/expanded_course_choices.md)。

## 改稿时的边界提醒

- 20组资源里包括课程、教材、指南、开发文档和大学公开讲座；不要概括为20门同等形式的课程，也不要说“全免费”。
- 第一人称感受、完成作业、复现成功、模型花费与证书体验，必须以录制者实际经历为准。本轮材料最多支持静态目录/正文/仓库审阅。
- NVIDIA页面标价互相有差异；不要引用单个旧PDF的“免费”推断所有版本。Google 2025/2026、Berkeley不同学期、DeepLearning.AI主课/三门短课需保留名称和版本区别。
- 脚本说“Anthropic官方课程”是三门课程组合；“OpenAI学习路线和Agents SDK”是文档路线，不是完整课程；“IBM Agentic AI in Practice”是课程与教程路径。
