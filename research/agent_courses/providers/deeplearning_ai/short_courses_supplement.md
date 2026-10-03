# DeepLearning.AI 三门 Agent 短课补充

研究日期：2026-10-03。只审阅 DeepLearning.AI 官方课程目录页中的课程简介、讲师、适用对象和章节目录。**没有完整转录课程，也没有运行 Notebook、完成课程练习或测验。**下文提到的练习来自官方页面列出的课程项目和 “Code Example” 标记，不代表本次实作验证。

## 课程速览

| 官方课程页 | 讲师（按课程页列名） | 页面标示 | 适合谁 |
|---|---|---|---|
| [AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph) | Harrison Chase（LangChain 联合创始人、CEO）；Rotem Weiss（Tavily 联合创始人、CEO） | Intermediate；1 小时 32 分；9 节视频；6 个代码示例 | 有中级 Python 基础，想用 LangGraph 构建更可控 Agent 的开发者。 |
| [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai) | João Moura（CrewAI 创始人、CEO） | Beginner；2 小时 41 分；18 节视频；7 个代码示例 | 学过一些提示工程、会基本编程，想把 LLM 用于工作流程的人。 |
| [Building Coding Agents with Tool Execution](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution) | Tereza Tizkova（E2B Growth）；Francesco Zuppichini（E2B Machine Learning Engineer） | Intermediate；1 小时 21 分；9 节视频；5 个代码示例 | 熟悉 Python 和 LLM、想让 Agent 编写并执行代码的 AI 开发者；了解 Agent 有帮助，但课程页称非必需。 |

## 具体内容与练习

### AI Agents in LangGraph

从 Python 和 LLM 手写一个 Agent，再把它改造成 LangGraph 流程。目录列有 LangGraph 组件、Agentic Search、持久化与流式输出、人机协作，最后用 Essay Writer 串起研究和写作流程。页面描述的具体动手点包括接入 Tavily 搜索、跨会话保存与恢复状态，以及把人工介入放入流程。

适合想看清 Agent 如何拆成节点和流程、需要控制状态或加入人工检查的学习者。页面要求中级 Python 知识。

### Multi AI Agent Systems with crewAI

由单 Agent 的角色、目标和工具配置，扩展到多个 Agent 分工与协作。代码示例涉及文章研究与写作、客服自动化、客户拓展、活动策划、财务分析、求职材料定制；页面还介绍顺序、并行和层级式协作，以及短期、长期和共享记忆、错误处理护栏。

适合想通过具体业务任务入门多 Agent 设计、愿意用 CrewAI 框架动手的人。课程页标为 Beginner，但建议已经接触提示工程并具备基本编程能力。

### Building Coding Agents with Tool Execution

重点是让 Agent 写出并执行 Python 代码，管理文件，再根据错误反馈继续尝试；还比较本地、容器和云沙箱，并用 E2B 云沙箱隔离生成的代码。目录和课程简介列出两个项目方向：用 Pandas 分析 CSV 并通过 Gradio 聊天界面回答问题；在沙箱中编辑多个文件、生成 Next.js 应用，并用运行时摘要处理长上下文。

适合要做能实际操作代码与文件的 Coding Agent、且具备 Python 和 LLM 基础的学习者。它把焦点放在代码执行和执行环境，不是泛讲所有类型的 Agent。

## 和 Andrew Ng 主讲的《Agentic AI》如何搭配

[Agentic AI](https://www.deeplearning.ai/courses/agentic-ai) 是另一门 DeepLearning.AI 课程，官方页明确列 **Instructor: Andrew Ng**。课程页标示 Intermediate、7 小时 45 分、31 节视频、7 个代码示例；目录与简介涵盖反思、工具使用、规划、多 Agent 工作流，以及评估和优化。

按官方简介与目录比较，《Agentic AI》更适合作为理解 Agentic Workflow 设计模式与评估思路的主线；三门短课分别落到 LangGraph 的流程与状态控制、CrewAI 的多 Agent 协作、以及 Coding Agent 的代码执行和沙箱。可把它们当成专题补充，按项目兴趣选择。讲师应逐门按课程页标注：这三门短课并非 Andrew Ng 主讲；在本组课程里，Andrew Ng 主讲的是《Agentic AI》。

## 可用于口播的三句

- “DeepLearning.AI 上不只有一门 Agent 课：Andrew Ng 主讲的《Agentic AI》讲设计模式和评估，另外还有框架和项目导向的短课。”
- “想做多 Agent 业务流程，可以看 João Moura 主讲的 crewAI；想控制状态、加搜索和人工检查，可以看 Harrison Chase、Rotem Weiss 主讲的 LangGraph。”
- “如果你关注的是能写代码、操作文件并在沙箱里运行的 Coding Agent，可以接着看 Tereza Tizkova 和 Francesco Zuppichini 的这门课。”

## 官方来源

- [AI Agents in LangGraph — DeepLearning.AI](https://www.deeplearning.ai/courses/ai-agents-in-langgraph)
- [Multi AI Agent Systems with crewAI — DeepLearning.AI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai)
- [Building Coding Agents with Tool Execution — DeepLearning.AI](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution)
- [Agentic AI — DeepLearning.AI](https://www.deeplearning.ai/courses/agentic-ai)
