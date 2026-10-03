# OpenAI Building Agents 路线与指南地图

盘点日期：2026-10-03。本地完整正文的文件清单和获取状态见 source/web_manifest.json（原本地资料引用，未随公开版收录），静态阅读评价见 [analysis.md](analysis.md)，获取限制见 [evidence.md](evidence.md)。OpenAI 的“Building agents”是一张学习路线与延伸指南集合，不是有一组可完成章节/作业/证书的完整线上课程。

## 建议学习顺序

| 阶段 | 推荐材料 | 学习目标 |
|---|---|---|
| 1. 认识概念与选择抽象层 | [Building agents track](https://developers.openai.com/tracks/building-agents)、[Agents overview](https://developers.openai.com/api/docs/guides/agents)、[Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) | 明白 agent 定义、Responses API 和 Agents SDK 分别承担什么；确定要显式管理 loop 还是采用 SDK runner |
| 2. 建立最小 Agent | [Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)、[Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents) | 定义 instructions/model/tools；创建 History tutor 并调用简单函数工具 |
| 3. 看清运行时 | [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)、[Results and state](https://developers.openai.com/api/docs/guides/agents/results) | 了解 runner loop、run result、multi-turn session、continuation、stream 和 interruption |
| 4. 拆分专家与决定责任归属 | [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | 判断 specialist 应接管用户对话，还是由 manager 把 specialist 当子能力调用 |
| 5. 处理边界与人工介入 | [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | 比较 input/output/tool guardrail 的位置，添加副作用前审批并从暂停状态恢复 |
| 6. 观察和评估运行过程 | [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability)、[Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | 检查完整 trace，并评估最终产物和 agent 轨迹 |
| 7. 根据目标选择模型与供应商 | [Models and providers](https://developers.openai.com/api/docs/guides/agents/models) | 按任务、延迟、成本和接口支持比较模型/Provider；版本选择需用当前官方页面核对 |

## 12 篇完整正文覆盖的主题

下列 12 页在 2026-10-03 本地快照里标为 `extracted_body_complete`，但它们仍是文档页面，不是 12 节实操课。

| 页面 | 主要内容 |
|---|---|
| [Building agents track](https://developers.openai.com/tracks/building-agents) | Agent 定义、模型和构建方式选择、工具、编排、评测与路线链接 |
| [Agents overview](https://developers.openai.com/api/docs/guides/agents) | Agents SDK 与 API 选择概览 |
| [Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) | SDK 用途、组件与推荐阅读顺序 |
| [Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart) | tutor、函数工具、handoff、trace 的入门路径 |
| [Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents) | Agent 配置、说明、输入/输出、tool 和 specialist 设计 |
| [Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents) | run loop、多轮 session、continuation、streaming 与异常/暂停处理 |
| [Results and state](https://developers.openai.com/api/docs/guides/agents/results) | 最终输出、最后控制 Agent、history/session/state 的延续 |
| [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | handoff 转移控制权、agent-as-tool 由 manager 保持控制 |
| [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | 输入/输出/工具校验、并行或阻断模式、审批中断与恢复 |
| [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability) | tracing、集成及观测入口 |
| [Models and providers](https://developers.openai.com/api/docs/guides/agents/models) | 模型、Provider 与传输策略 |
| [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | Trace grading、评测器与回归检查 |

## 建议的 8 个小实验

1. **历史 tutor**：先只定义输入、行为和输出，不加工具；记录最小请求路径。
2. **函数工具**：添加读取型工具并核验参数、无效输入和异常如何返回。
3. **双专家路由**：把题目分到 History tutor 或 Math tutor，固定一批正例、模糊例和越界例。
4. **handoff / agent-as-tool 对照**：同一个“总结账单并建议退款”任务，分别让退款专家接管和让 manager 调用专家；对比最后回复责任与 trace。
5. **Guardrail 时序**：同一个不允许的问题，比较并行检查与 `runInParallel: false` 的阻断检查，记录主模型是否已经启动、成本和延迟。
6. **写操作审批**：给取消订单或更新资料加审批，测试批准、拒绝、等待超时、用户中断与恢复。
7. **Session 恢复**：保存跨 turn 状态，中断之后继续；对比手工 history、SDK session 和 continuation 的数据所有权。
8. **Trace grader**：为“是否正确分流、是否调用正确工具、是否审批、结果是否正确”分别定分，故意制造一条路径错误但最终输出碰巧正确的 case。

## 路线边界

本轮没有完整获取 Function calling、Structured outputs、Conversation state、Compaction、Tools 和 docs MCP 页的正文；它们在课程整体路线中很重要，但当前快照中不能对这些页作逐段内容分析。遇到需要完整理解的任务，应从 OpenAI 官方路线页进入这些单独指南，再核对本地 `web_manifest` 是否补充了可读正文。
