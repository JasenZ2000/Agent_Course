# DeepLearning.AI Agentic AI 章节地图

官方课程页：[Agentic AI](https://www.deeplearning.ai/courses/agentic-ai)。官方社区公开索引列出五个课程模块。下表按该模块索引整理，并用本地视频转录中的标题/内容补充；可见转录标题不保证与平台的每个 lesson 槽位一一对应。

| 模块 | 主题 | 本地可读转录与代表内容 |
|---|---|---|
| 1 | Introduction to Agentic Workflows | Welcome、What is agentic AI?、Degrees of autonomy、Benefits、Applications、Why not just direct generation?、Task decomposition、Planning workflows、Creating and executing LLM plans、Planning with code execution、Evaluating agentic AI。Research Agent 由直接写作演变为提纲、搜索、草稿、编辑和重写；另举订单邮件、发票和电子表格分析。 |
| 2 | Reflection Design Pattern | Reflection to improve outputs、Evaluating the impact of reflection、Using external feedback。对邮件/代码先生成，再批评并修订；通过执行代码取得异常信息，展示外部反馈为何比纯自评更有帮助。 |
| 3 | Tool use | What are tools?、Tool syntax、Creating a tool、Code execution、MCP。讲模型返回工具调用请求、参数 schema、工具执行后把结果回填；示例有当前时间、网页搜索、SQL 数据库、计算和 GitHub MCP Server。 |
| 4 | Practical Tips for Building Agentic AI | Evaluations、Error analysis、More error analysis examples、How to address problems、Component-level evaluations、Chart generation workflow、Latency/cost optimization、Development process summary。讲端到端与组件评测、gold set、代码裁判/模型裁判、失败归因、测量后优化。 |
| 5 | Patterns for Highly Autonomous Agents | Agentic design patterns、Multi-agentic workflows、Communication patterns for multi-agent systems、Conclusion。以营销材料为例，拆分 researcher、designer、writer 角色，并对比顺序通信与 manager-led hierarchy。 |

本地保存 31 个视频转录文件及各自的标题、字数、SHA-256 与原 lesson URL，见 source/videos/transcript_manifest.json 和 source/videos/transcripts/。标题总索引见 [evidence.md](evidence.md)。课程站 lesson 页面正文未在这份归档中保存；这一章节地图是“社区目录加可读转录”的研究地图，不代表课程所有测验和练习均已获得。
