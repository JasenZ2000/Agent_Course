# Anthropic Claude Academy 与 Agent SDK：课程地图

盘点日期：2026-10-03。Claude Academy 当前公开课程页面和本地正文索引见[完整逐课索引](lesson_index.md)。本文件按教学主题重排，方便选择阅读顺序；不是逐课复述，也不是视频转写。

## 公开课程总览

| 官方课程 | 有正文的教学页 | 教学主线 | 推荐起点 |
|---|---:|---|---|
| [Claude Platform 101](https://academy.claude.com/courses/claude-platform-101) | 13 | 平台组成、API、模型选择、Agent loop、工具、Thinking、Skills、MCP、上下文、Managed Agents、Claude Code | 初学者的概念地图 |
| [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | 67 | 请求与提示、生成控制、Prompt eval、Tool use、RAG、MCP 实作、Claude Apps/Code 集成、工作流与 Agent | 已会一种编程语言、准备做 API 项目的人 |
| [Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol) | 10 | MCP 客户端、工具、Inspector、资源、提示模板和复习 | 需要自己连接/实现 MCP Server 或 Client 的人 |
| **合计** | **90** | 公开课文字页面；不含测验与徽章页 | 视频时长见逐课索引，非学习总时长 |

## 按能力递进的课程路径

### 1. 先建立平台和 Agent 词汇

建议先读 Platform 101 的这些页面：

- 平台层次、第一次 API 请求、模型选择；
- Agent loop、工具调用、extended thinking 与 server-side built-in tools；
- Skills、MCP、context management；
- Managed Agents 的定义与首次构建；
- 用 Claude Code 从 stub 生成应用代码。

这组只有 13 个页面，适合先弄懂“模型给出工具请求”与“宿主执行工具并把结果送回模型”之间的分工。课程以 Claude 平台为例，理解原理后还需映射到其他 API 的具体术语和状态模型。

### 2. 从 API 语法走向可重复行为

Building with the Claude API 前段先解释请求、消息状态和常用生成控制，再进入 Prompt Engineering 与 Prompt Evaluation：

- 首次请求、API key、多轮消息、system prompt；
- temperature、streaming、structured data；
- 通过数据集、grader 和迭代比较 Prompt；
- 对比 model grader、code grader 和人工 grader。

典型闭环是把目标和输入做成测试集，运行 prompt，按明确标准评分，检查 Bad Case 后改 prompt，再在相同数据集上比较。生成式合成数据有助于补充边界样例，仍需人工核查代表性和正确标签。

### 3. 工具调用与 Agent 控制循环

接下来的教学由简入繁：先介绍工具函数和 schema，随后解释多内容块消息、tool result、多个工具、错误处理和多轮循环；再介绍 fine-grained tool calling、内置文本编辑与 web search 工具。

这一段的重要学习点不是“模型会选择工具”，而是宿主程序如何接收 `tool_use`、校验输入、实际执行、把 `tool_result` 与调用 ID 对应，再判断要继续调用还是停止。学完后可以尝试做一个只读查询工具和一个有副作用但必须确认的工具，观察两种权限边界有什么差别。

### 4. 检索增强与上下文形态

RAG 部分覆盖问题导入、分块策略、文本 embedding、完整检索流程、实现、BM25 和多索引检索。随后扩展 extended thinking、图像/PDF、引用、prompt caching、code execution 和 Files API。

教学例子包含精确 Incident ID 查询、向量检索与词法检索并行、RRF 汇总，以及 PDF/图像中的内容处理。RRF 页的部分方法保留伪代码式空循环，读者需要自己补齐实现、去重、评估 Recall/Precision 和引用定位；不能照抄作生产实现。

### 5. 用 MCP 组织跨应用工具、资源和提示

Building with the Claude API 的 MCP 小节加上独立 10 页 MCP 课程，覆盖：协议介绍、客户端、Tool Schema、Inspector、客户端实现、Resource 定义与读取、Prompt 定义与调用、应用集成和复习。

推荐先看 Platform 101 MCP 建立“工具、Skill、MCP 的差别”，再沿独立 MCP 课程自己画一遍 Client 请求 Server 的时序。MCP 把接口互操作做成协议，但业务身份、用户授权、危险操作确认和服务端权限仍由应用设计。

### 6. 选择 workflow 或 Agent，最后看长任务

API 课程后段从 workflow 的 parallelization、chaining、routing 转入 agents-and-tools、environment inspection 和 workflows-vs-agents。推荐阅读顺序是固定链式任务 → 明确类别的路由 → 需要按中间结果自行决定下一步的 Agent → 查看可用执行环境与风险 → 判断何时回到确定性 workflow。

独立工程文章继续往生产系统推进：简单 composable workflow、短工具接口、上下文挑选、评测维护、managed agent 的 session stream、harness 为跨多次上下文切换保存状态。它们是配套工程文章，不记入 90 篇课程页。

## 可作为第一次小项目的 10 个页面例子

| 教学页 | 页面里的例子 | 能练的能力 | 复现时要补什么 |
|---|---|---|---|
| [The agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained) | 天气查询工具返回 Austin “95F, sunny” | stop reason 分支、tool call/result 往返 | 换成真实只读 API，验证参数错误和失败 |
| [Generating test datasets](https://academy.claude.com/courses/building-with-the-claude-api/generating-test-datasets) | AWS Python/JSON/Regex 输出评测数据 | 数据集结构、合成输入 | 清洗标签、加难例、固定版本和样本数 |
| [Routing workflows](https://academy.claude.com/courses/building-with-the-claude-api/routing-workflows) | 把主题分为教育、娱乐、喜剧、vlog、评论、故事 | 有限类别意图识别和专用模板 | 加“不确定/多意图/越界”分支，统计误路由 |
| [Agents and tools](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools) | 90 天保修缺少购买日期时先问用户 | 澄清而非猜测、字段完整性 | 明确日期时区、购买凭证、无记录回退 |
| [Skills](https://academy.claude.com/courses/claude-platform-101/skills) | 状态报告格式作为 `SKILL.md` 规约 | 流程知识与动作能力分离 | 检查 Skill 来源、权限、脚本副作用 |
| [Context management](https://academy.claude.com/courses/claude-platform-101/context-management) | Compliance agent 只按需查建筑规范 | just-in-time context | 比较检索结果与全文常驻的质量、费用 |
| [BM25 lexical search](https://academy.claude.com/courses/building-with-the-claude-api/bm25-lexical-search) | 精确查 `INC-2023-Q4-011` | 标识符匹配和 hybrid retrieval | 测向量、词法与融合的 Recall@k |
| [A Multi-Index RAG pipeline](https://academy.claude.com/courses/building-with-the-claude-api/a-multi-index-rag-pipeline) | 向量/BM25 排名经 RRF 合并 | 排名融合 | 补全代码、缺失文档的惩罚和去重 |
| [Fine grained tool calling](https://academy.claude.com/courses/building-with-the-claude-api/fine-grained-tool-calling) | 流式输出工具参数并处理无效 JSON | 增量解析与校验 | 测半截 JSON、超时、取消和幂等 |
| [Building your first managed agent](https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent) | Agent、environment、session、event stream | 托管运行生命周期 | 记录恢复、事件排序、成本和异常中断 |

## 配套工程阅读顺序

1. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)：先选择最简单可控的构件，需要时逐步加复杂度。
2. [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)：把高层任务拆成描述清晰、接口可用的工具。
3. [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 与 [Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)：补齐上下文预算与评测闭环。
4. [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) 和 [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)：研究跨窗口任务状态、计划/生成/评估分工。
5. [Managed Agents](https://www.anthropic.com/engineering/managed-agents)：理解执行环境、durable session 和管理面分离。

具体正文快照和版本边界见[evidence.md](evidence.md)；本目录中的[分析](analysis.md)负责评价结构和可迁移性。
