# Hugging Face Agents Course：证据、采集范围与复核日志

研究日期：2026-10-03（Asia/Shanghai）

## 1. 采集元数据

| 字段 | 结果 | 可复核证据 |
|---|---|---|
| 上游仓库 | `https://github.com/huggingface/agents-course.git` | [GitHub 仓库](https://github.com/huggingface/agents-course) |
| 获取方式 | `git clone --depth 1 --filter=blob:none ... source` | 本地 `source/.git`（原本地资料引用，未随公开版收录）；浅克隆只保留当前提交历史，工作树为完整当前仓库。 |
| HEAD | `b3946b1d09d29c65736e219d48a8a736a2c52154` | [固定提交树](https://github.com/huggingface/agents-course/tree/b3946b1d09d29c65736e219d48a8a736a2c52154) |
| HEAD 提交时间 | `2026-09-09T17:03:10+02:00` | 本地 `git log -1 --format='%H%n%cI%n%s'` |
| HEAD 标题 | `Merge pull request #693 from huggingface/dependabot/github_actions/actions-d2572d006c` | 同上 |
| License | Apache License 2.0 | `source/LICENSE`（原本地资料引用，未随公开版收录）｜[提交固定页](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/LICENSE) |
| tracked 文件数 | 441 | `git ls-files | Measure-Object` |
| 英文课程文件 | 78 | `git ls-files` 中 `units/en/*` |
| 简体中文课程文件 | 79 | `git ls-files` 中 `units/zh-CN/*` |
| 全部语言课程文件 | 422 | `units/*`；包括 en 78、es 79、fr 78、ko 53、ru-RU 27、vi 28、zh-CN 79。 |
| 其它仓库文件 | 19 | README、LICENSE、quiz、脚本、GitHub workflow、翻译约定等。 |
| Git 状态 | 采集后无修改 | 在 `source` 内执行 `git status --short` 无输出。研究文档写在 `source` 外。 |

## 2. 获取完整性

### 已获取

- 当前提交的**全部 441 个 tracked 文件**，没有对语言或章节做 sparse 排除。
- 英文课程正文、简体中文正文、其余仓库所含翻译、quiz JSON、课程维护脚本和许可证。
- 正文中所有代码块，因此“仓库内公开文字和代码”在该提交范围内完整落盘。
- 英文与中文 `_toctree.yml`，可据此还原官网目录顺序。

### 未获取/未执行

- 仓库正文以外的远程图片数据集。英文正文有 112 个包含 `course-images` 的引用行，图片托管在 `huggingface.co/datasets/agents-course/course-images`，本仓库没有把这些位图纳入 Git；本轮没有另行批量下载。
- 课程引用的 Hugging Face Spaces、datasets、GAIA 附件、Langfuse dashboard/trace 的完整离线副本。
- 3 处英文 YouTube 引用所对应的视频文件或字幕；没有逐个观看或转录视频。
- Discord 直播记录、社区讨论、登录后交互状态。
- 任何推理 API、Space 复制、排行榜提交、模型微调或证书流程。

因此可准确表述为：**当前仓库公开正文与仓库内代码已完整获取；远程媒体和交互服务未离线镜像，视频未逐看/转录，代码仅静态审阅。**

## 3. 当前官网复核

2026-10-03 直接打开了两页，而不是只读仓库 README：

- 英文：<https://huggingface.co/learn/agents-course/unit0/introduction>
- 简体中文：<https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction>

| 核对项 | 英文当前页/源码 | 简体中文当前页/源码 | 判断 |
|---|---|---|---|
| 认证截止 | “There’s no deadline for the certification process.”；`en/unit0/introduction.mdx`（原本地资料引用，未随公开版收录） | “所有考核作业需在 2025 年 7 月 1 日前完成”；`zh-CN/unit0/introduction.mdx`（原本地资料引用，未随公开版收录） | 中文政策信息过期，以英文当前页为准。 |
| 课程库列表 | smolagents、LlamaIndex、LangGraph | 欢迎页同一处写 smolagents、LangChain、LlamaIndex；后续大纲又写 LangGraph | 中文页内部也不一致。 |
| 维护团队 | 当前英文写 Ben Burtenshaw、Sergio Paniego | 中文保留 Joffrey/Ben/Thomas 的旧团队介绍 | 翻译没有完全跟随英文结构。 |
| 历史发布页 | 英文无 `communication/next-units.mdx` | 中文仍有 `communication/next-units.mdx`（原本地资料引用，未随公开版收录） | 中文 79、英文 78 的唯一规范化路径差异；是历史残留页。 |

文件集合复核方法：把中文的 `bonus_unit2` 规范化为英文的 `bonus-unit2` 后运行 `Compare-Object`，唯一多出的中文路径为 `communication/next-units.mdx`。所以中文版不是大量缺章，而是少量时效信息和历史结构落后。

## 4. 课程结构证据索引

以下 URL 固定到本轮提交，避免未来 main 分支变化后证据漂移。

| 判断/主题 | 本地证据 | 固定公开 URL |
|---|---|---|
| Agent 正式定义与 agency 光谱 | `what-are-agents.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/what-are-agents.mdx) |
| Tool schema、模型不直接执行工具 | `tools.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/tools.mdx) |
| Thought–Action–Observation loop | `agent-steps-and-structure.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/agent-steps-and-structure.mdx) |
| stop-and-parse 与 code execution 风险 | `actions.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/actions.mdx) |
| 手写 dummy loop 与幻觉失败 | `dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit1/dummy-agent-library.mdx) |
| smolagents sandbox/authorized imports | `code_agents.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit2/smolagents/code_agents.mdx) |
| 多 Agent manager/worker | `multi_agent_systems.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit2/smolagents/multi_agent_systems.mdx) |
| LlamaIndex RAG、QueryEngine、evaluators | `components.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit2/llama-index/components.mdx) |
| LlamaIndex workflow loop/branch/state | `workflows.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit2/llama-index/workflows.mdx) |
| LangGraph 邮件分类/条件路由 | `first_graph.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit2/langgraph/first_graph.mdx) |
| Agentic RAG 的三框架完整 Agent | `agent.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit3/agentic-rag/agent.mdx) |
| observability、online/offline eval | `what-is-agent-observability-and-evaluation.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/bonus-unit2/what-is-agent-observability-and-evaluation.mdx) |
| Langfuse/GSM8K dataset run | `monitoring-and-evaluating-agents-notebook.mdx`（原本地资料引用，未随公开版收录） | [GitHub](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/bonus-unit2/monitoring-and-evaluating-agents-notebook.mdx) |
| GAIA 与课程最终评分 | `what-is-gaia.mdx`（原本地资料引用，未随公开版收录）、`hands-on.mdx`（原本地资料引用，未随公开版收录） | [GAIA](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit4/what-is-gaia.mdx)｜[提交 API](https://github.com/huggingface/agents-course/blob/b3946b1d09d29c65736e219d48a8a736a2c52154/units/en/unit4/hands-on.mdx) |

## 5. 负面判断如何验证

“课程没有系统覆盖某主题”不能由目录直觉推出。本轮对全部 `units/en` 做了全文检索并回看上下文：

| 主题 | 检索与结果 | 可以下的结论 |
|---|---|---|
| SQLite/关系数据库 | 对 `sqlite|postgres|transaction|connection pool` 搜索，主课无 SQLite 教学结果。 | 可以说“课程没有 SQLite/事务/连接池章节”；不能说所有外部链接也没有。 |
| 写操作审批 | `approval|confirm|permission|side effect|write|delete` 主要命中课程管理文本、代码写内存/文件和安全提醒，没有发送/删除/支付前审批模式。 | 可以说“写操作边界未形成课程主线”。 |
| Skill | 没有独立 Agent Skill 定义/章节；命中多为自然语言 skills。 | 可以说“未讲清 Skill 与 Tool/MCP 的工程边界”。 |
| scaling | `scale|concurrency|rate limit|queue|multi-tenant|backpressure` 没有形成部署/容量章节。 | 可以说“缺少 scaling 教学”；不能把 multi-agent 分工直接等同于系统扩缩容。 |
| checkpoint/recovery | memory/state 章节存在，但没有 durable checkpoint、crash recovery、resume 的完整实验。 | 可以说“状态概念有，故障恢复没有”。 |
| 安全 | 明确命中 CodeAgent sandbox、safe import、prompt injection/恶意代码警告以及 `trust_remote_code=True`。 | 不能说课程完全不讲安全；准确说法是“有执行安全提示，缺写操作审批与权限系统”。 |

## 6. 版本与模型证据

- 仓库没有根 `requirements.txt`；课程依赖安装散落在 `.mdx`，因此没有统一可复现版本集合。
- `langgraph/introduction.mdx`（原本地资料引用，未随公开版收录） 仍写示例用 GPT-4o API；`dummy-agent-library.mdx`（原本地资料引用，未随公开版收录） 已使用 `moonshotai/Kimi-K2.5`。同一课程存在不同时期的模型选择。
- `langgraph/first_graph.mdx`（原本地资料引用，未随公开版收录） 设置 `temperature=0`，但没有固定跨章节 model revision 或多次运行一致性测试。
- `tutorial.mdx`（原本地资料引用，未随公开版收录）、`smolagents/code_agents.mdx`（原本地资料引用，未随公开版收录） 有 `trust_remote_code=True`；静态研究没有执行这些远程代码。

## 7. 可复核命令摘要

```powershell
git -C source rev-parse HEAD
git -C source log -1 --format='%H%n%cI%n%s'
git -C source ls-files | Measure-Object
git -C source status --short
Get-ChildItem source/units/en -Recurse -File | Measure-Object
Get-ChildItem source/units/zh-CN -Recurse -File | Measure-Object
rg -n -i "sqlite|approval|skill|checkpoint|concurr|production|eval|memory|context" source/units/en
```

以上命令只读取本地浅克隆；统计口径是 Git tracked 文件，不把 `.git` 对象、远程 Space、图片数据集或生成缓存算入课程文件数。

