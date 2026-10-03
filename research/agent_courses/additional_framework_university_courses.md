# 新增课程：框架工程与大学在线课程

核验日期：2026-10-03。仅审阅官方公开简介、目录和仓库README；未观看全课、取得付费作业或运行项目。适用判断来自目录比较，不是亲测评价。本文补充原有LangGraph入门课，新增课程本身有不同教学主线。

## 1. LangChain Academy：Foundation — Introduction to Deep Agents

[官方课程](https://academy.langchain.com/courses/foundation-introduction-to-deepagents)；[官方代码仓库](https://github.com/langchain-ai/lca-deepagents)。官网标为免费课程；模型与运行环境成本另查。

五模块依次讲Agent构建、执行环境、上下文管理、任务委派和综合项目。目录直接出现MCP、checkpointer、人工介入、文件系统、沙箱、摘要与上下文卸载、Skills、记忆、动态子Agent；综合部分包含销售助手与本地部署。

已有基础循环知识，想理解harness、Skill、执行环境或子Agent的人，可以优先审阅。这比原有Introduction to LangGraph更接近用户关心的开发面经术语，但这些术语仍是具体实现中的约定。仓库提供Python材料；目录有TypeScript准备课，README同时有相关实现待补说明，不能保证两种语言内容完全对齐。

口播入口：“工具能调用以后，文件放在哪、上下文太长怎么办、任务怎么交给子Agent？这一门就顺着这些问题讲。”

## 2. LangChain Academy：Introduction to Agent Observability & Evaluations

[官方课程](https://academy.langchain.com/courses/intro-to-langsmith)。页面当前标题与旧URL不同，录制时按当前标题标注。

目录主线是运行观测、测试与评估、提示词开发、人工反馈、生产观测。具体入口包括数据集、评估器、实验结果、成对比较、标注队列和在线评估。适合已经有一个Agent，想建立失败记录与回归评测的人；教学围绕LangSmith，需要另外检查账户额度及外部模型费用。

视频可以用“换了提示词以后，怎么知道真的变好”引入。它与构建Agent的课程是不同专题，不应让刚学Python的观众同时开始两套。

## 3. LangChain Academy：Project — Ambient Agents with LangGraph

[官方课程](https://academy.langchain.com/courses/ambient-agents)；[官方课程列表对项目的说明](https://academy.langchain.com/collections/project)。目录有六模块：LangGraph基础、构建Agent、评测、人工介入、记忆、部署，官网标为免费课程。

项目围绕邮件管理，适合希望跟着一项任务把开发流程串起来的人。可以与基础图课程比较：一套沿框架概念推进，一套沿具体应用推进。课程代码、账号配置和邮件集成尚未逐项验证；不能称已跑通邮件自动处理。

视频入口：“如果单看节点和边比较抽象，可以换一个邮箱助手项目，看看评测、人工检查和记忆怎样进入同一份程序。”

## 4. Vanderbilt / Coursera：AI Agents and Agentic AI in Python

[三门课系列](https://www.coursera.org/specializations/ai-agents-python)，Jules White主讲。课程组合含：Python Agent实现、Prompt Engineering for ChatGPT、Python Agent架构。官网要求基本Python能力。

可确认主题包括手写框架组件、工具发现与函数调用、文件探索和文档生成；架构课进一步涉及多Agent、共享记忆、分阶段执行和可逆动作。适合希望沿课程顺序学习Python实现、而不是一开始就套用框架的开发者。这里介绍的是课程目标，尚未核验全部代码与实际工程可靠性。

平台显示免费报名和订阅入口；这不能证明完整作业与证书免费，最终访问范围以账号页面为准。

## 5. 同校的AI Agent Developer：作为替代组合，不重复计课

[六门课系列](https://www.coursera.org/specializations/ai-agents)。与上述三门系列有重叠，另包含领导者入门、ChatGPT数据分析和可信生成式AI等内容。希望补概念与工具使用可以对照；专注应用开发的人应先看Python核心课的实际目录。

综述中可以给出两种组合的区别，不能把它们加起来说成九门独立Agent课程，也不能把所有Prompt或ChatGPT课程算作Agent编程课。

## 对原视频的补充位置

- Deep Agents：放在状态编排之后，专门回答harness、文件系统、Skills和子Agent。
- Observability & Evaluations：单列评测专题，补“能运行之后如何判断质量”。
- Ambient Agents：作为跟做完整应用的项目选择。
- Vanderbilt：与Datawhale、HF和吴恩达放在一起比较基础学习方式；突出Python手写实现。
- 六门组合：仅在资源表作为替代路径备注，不增加独立课程数量。
