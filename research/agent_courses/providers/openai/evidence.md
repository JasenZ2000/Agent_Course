# OpenAI Agent 学习材料：来源与证据边界

研究快照：2026-10-03（北京时间）。本页说明本地这批 OpenAI 官方页面的抓取范围，以及哪些内容能支持课程分析。正文内容和抓取清单位于本目录的 `source/` 下。

## 完整正文页面：12 篇

`source/web_manifest.json` 对应本轮选定的 18 个网页目标。其中 **12 项** acquisition 标记为 `extracted_body_complete`，**6 项**为 `navigation_or_error_only`。完整正文的 12 项是：

1. [Building agents](https://developers.openai.com/tracks/building-agents)
2. [Agents overview](https://developers.openai.com/api/docs/guides/agents)
3. [Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk)
4. [Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)
5. [Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)
6. [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)
7. [Results and state](https://developers.openai.com/api/docs/guides/agents/results)
8. [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)
9. [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)
10. [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability)
11. [Models and providers](https://developers.openai.com/api/docs/guides/agents/models)
12. [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)

每条记录包含官网 URL、页面标题、抓取行数、正文起始行、缺失正文行、对应检索结果路径、本地 text 路径和 SHA-256。被标为完整正文的依据是本次保存范围内没有缺失的正文行；它表示所选正文已提取，不表示所有官方文档、动态交互、外链代码库或媒体都已离线保存。

## 导航、重定向或提取错误：6 项

以下页面只保存页面导航/错误信息，本次不将它们作为完整正文来分析：

| 官方页面 | 快照状态 |
|---|---|
| [Compaction](https://developers.openai.com/api/docs/guides/compaction) | `navigation_or_error_only` |
| [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state) | `navigation_or_error_only` |
| [Function calling](https://developers.openai.com/api/docs/guides/function-calling) | `navigation_or_error_only` |
| [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | `navigation_or_error_only` |
| [Using tools](https://developers.openai.com/api/docs/guides/tools) | `navigation_or_error_only` |
| [docs MCP resource](https://developers.openai.com/resources/docs-mcp) | 重定向到 `/learn/docs-mcp`，未取得目标正文 |

Building agents track 和其他完整页面会提及这些概念或链接，但不能将这些“被提及”扩写成已静态阅读了缺失指南的具体实现细节。

## HTTP 403 和替代正文获取

`source/manifest.json` 保留了多条直接请求官方 `.md` 文档返回 HTTP 403 的记录，状态为 `failed` / `not_acquired`。这些是请求事实，不能当作文档正文。之后通过官方网页的公开正文行提取补回其中 12 个页面的可读文字；原始 HTML 并没有因此取得。OpenAI 来源的 `source/web_retrieval/` 存有工具返回的页面行片段和抓取上下文；`source/text/` 存有按行保留的可读正文。每份 text 开头注明原链接和“public web tool line extraction; original HTML not acquired”。

因此准确表述为：“已对 12 篇官方路线/指南保存完整的可见正文行，并保存 6 项未获完整正文的状态。”不应表述成“抓取了 OpenAI 全套文档原 HTML”或“课程全部离线可用”。

## 访问范围和体验边界

材料均来自官网公开页面。没有登录 OpenAI 控制台、创建 API key、执行 SDK 代码、调用模型、运行评测、创建 Trace、实测 SQLite 持久化或完成外部代码实验。所有学习体验描述是静态文字阅读判断；页面中展示的输出、trace、路由成功和 cost/latency 取舍均按官方示例说明处理，没有独立重现。

API、SDK、模型名称、默认值与控制台能力会更新。本文是截至抓取时的研究快照，不替代目标版本的官方 API Reference、SDK 类型或实际运行结果。

## 本地目录索引

| 内容 | 本地文件 |
|---|---|
| 12 完整项 + 6 导航/错误项汇总 | `source/web_manifest.json` |
| 最初 `.md` 请求状态，包括 HTTP 403 | `source/manifest.json` |
| 逐页可读正文 | `source/text/` |
| Web 页面行提取原始结果 | `source/web_retrieval/` |

跨来源的方法定义见[方法与证据标准](../../methodology.md)。
