# Datawhale Hello-Agents 来源与证据记录

记录日期：2026-10-03（Asia/Shanghai）  
对象：[`datawhalechina/hello-agents`](https://github.com/datawhalechina/hello-agents) 本地仓库快照和已存在的面经综述。  
研究方法：静态阅读 Markdown、目录/代码清点、针对研究问题的源代码审阅；没有运行代码、测试、Notebook、服务、benchmark 或外部 API，也没有观看/转录配套视频。

## 1. 获取基线

| 字段 | 记录 |
|---|---|
| 仓库 | `https://github.com/datawhalechina/hello-agents.git`，本地 `origin` 与此一致 |
| 固定 commit | [`4b014ad47e2658af24b59f21e7bdb3f89a66205e`](https://github.com/datawhalechina/hello-agents/tree/4b014ad47e2658af24b59f21e7bdb3f89a66205e) |
| commit 日期/说明 | 2026-09-29；`Merge pull request #921 from datawhalechina/codex/recover-pr-614-squashed` |
| 本地变更 | 检查时工作树干净；当前分析文件在仓库外层 `providers/datawhale/`，不改动课程快照 |
| 克隆形态 | 浅克隆；`git rev-parse --is-shallow-repository` 返回 `true`。固定 commit 的工作树可读，完整历史不可读 |
| Checkout 形态 | sparse-checkout 开启，pattern 包含 `/*` 并排除 `.png/.jpg/.jpeg/.webp/.gif`、音视频、PDF、压缩包及模型权重等扩展名 |
| 文件数 | `git ls-files` 返回 2,434 条；其中 2,036 条在工作树，398 条因 sparse-checkout 文件类型规则未落盘 |
| 目录 | `docs/`、`code/`、`Extra-Chapter/`、`Additional-Chapter/`、`Co-creation-projects/` 都已存在。文本教材和目标代码可读；398 个跳过文件意味着配图、录屏/音频、PDF、压缩包等素材不在本地 |

“浅克隆”和“稀疏检出”含义不同：本次有固定 commit 的文本/代码树，但没有 Git 全历史；被排除的媒体也不能作为当前视觉/视频体验的审阅证据。为完成本轮研究没有重新下载仓库或媒体。

## 2. 阅读范围与没有覆盖的部分

### 已检查

- 中文 README（原本地资料引用，未随公开版收录）、英文 README（原本地资料引用，未随公开版收录）、中文侧边栏（原本地资料引用，未随公开版收录）、前言（原本地资料引用，未随公开版收录）和根目录 LICENSE（原本地资料引用，未随公开版收录）。
- 16 章中文正文：通读目录结构/标题层级，对定义、实践、配置、代码说明、评估和讨论题做目标性检索。各章正文均位于 `source/docs/chapter1`–`chapter16`；英文对应版本也在 `docs/`，本次不做逐段翻译校对。
- `source/code/chapter1`–`chapter15` 的文件清单和与主要判断有关的代码。第 16 章代码目录提供 `共创路径.md`；毕业设计配套项目主要在独立的 `Co-creation-projects/`。
- 与术语相关的补充材料：Extra01 面试问题/参考答案、Extra05 Skill 与 MCP、Extra08 Skill 写作、Extra09 Agent 应用经验、Extra10 Agent 自进化、Extra13 视频共创索引。
- 本地 [面经综述](../../../agent_interview_review.md) 和 [国内扩展目录](../../../interview_catalog_china_expanded.md)，仅用于定位公开帖子已记录的题目类型和证据等级。

### 未检查或不能据此判断

- 没有逐行审计 `Co-creation-projects/` 中的 1,600 多个社区文件；不把个别投稿项目等同于课程主教材质量。
- 没有完成每个源文件的代码审查。下面列出的 Python/TypeScript/GDScript 是用于说明特定概念的选读样本，不是全仓安全或正确性审计。
- `hello_agents` 框架链接到外部仓库 [`jjyaoao/helloagents`](https://github.com/jjyaoao/helloagents)。Datawhale 教材的第 7–9 章通过导入该库展示能力；本地快照不含该依赖的完整实现，所以不能声称审计了 MemoryTool、RAGTool、ContextBuilder、NoteTool 或 TerminalTool 的内部代码。
- 未登录 Coze、Dify、FastGPT、n8n、Qdrant Cloud、Neo4j Aura、地图/搜索服务或模型平台；没有验证 2026-10-03 的外部服务、API、账号额度和依赖是否仍可运行。
- Extra13 视频索引（原本地资料引用，未随公开版收录）含外部链接和待发布条目；仅阅读索引，不打开或观看视频。
- 不推断首次跑通时间、实际价格、稳定性、正确率、课程覆盖率、证书/结课结果或所有初学者的真实体验。

## 3. 主张与直接材料的对应

| 报告中的判断 | 可复查材料 | 证据边界 |
|---|---|---|
| 主目录共 16 章、分为五部分 | README 导航/学习建议（原本地资料引用，未随公开版收录）、侧边栏（原本地资料引用，未随公开版收录） | 目录设计的直接证据，不是已完成学习记录 |
| 项目将读者定位为有 Python 和 LLM API 基础的开发者/学生 | README 如何学习（原本地资料引用，未随公开版收录）；第 4 章依赖与 API 配置（原本地资料引用，未随公开版收录） | 作者建议和书面先修，不是每个章节的硬性安装门槛 |
| 初始 Agent 是天气→景点的行动闭环 | 第 1 章（原本地资料引用，未随公开版收录）、`FirstAgentTest.py`（原本地资料引用，未随公开版收录） | 代码静态可见；本次未验证外部服务响应 |
| ReAct/计划/反思包含不同控制模式 | 第 4 章（原本地资料引用，未随公开版收录）、`ReAct.py`（原本地资料引用，未随公开版收录）、`Plan_and_solve.py`（原本地资料引用，未随公开版收录）、`Reflection.py`（原本地资料引用，未随公开版收录） | 可证明示例结构，不能证明模型每次解析成功 |
| 框架篇包含 AutoGen、AgentScope、CAMEL 和 LangGraph | 第 6 章（原本地资料引用，未随公开版收录）、`LangGraph Dialogue_System.py`（原本地资料引用，未随公开版收录） | LangGraph 文件将 `understand→search→answer` 固定相连并挂 `InMemorySaver`；此文件本身不是生产持久化或条件分流证明 |
| Skill 与 Tool 可在补充材料中对照 | Extra05（原本地资料引用，未随公开版收录）、Extra08（原本地资料引用，未随公开版收录）、第 7 章工具系统（原本地资料引用，未随公开版收录）、第 10 章协议（原本地资料引用，未随公开版收录） | Skill 主体是社区扩展；不要把补充文章定义说成所有生态的统一规范 |
| Query 需要辨别语境 | 第 3 章 Attention Query（原本地资料引用，未随公开版收录）、第 4 章搜索 query（原本地资料引用，未随公开版收录）、第 14 章研究任务（原本地资料引用，未随公开版收录） | 三处同词不同对象；这是跨章术语阅读提醒，不是原文错误 |
| 记忆与 RAG 是可区分的系统能力 | 第 8 章（原本地资料引用，未随公开版收录）、`01_MemoryTool_Basic_Operations.py`（原本地资料引用，未随公开版收录）、`10_RAG_Pipeline_Complete.py`（原本地资料引用，未随公开版收录） | 示例依赖 HelloAgents 外部库及所选存储/embedding 服务 |
| Chapter 9 用上下文、笔记和终端工具做代码库维护 | 第 9 章（原本地资料引用，未随公开版收录）、`05_terminal_tool_examples.py`（原本地资料引用，未随公开版收录）、`06_three_day_workflow.py`（原本地资料引用，未随公开版收录） | 有白名单/工作区/路径逃逸的文字及调用样例；未审计外部 TerminalTool 实现，也未做实际越权尝试 |
| 协议章节有 MCP/A2A/ANP 设计 | 第 10 章（原本地资料引用，未随公开版收录）、第 10 章代码（原本地资料引用，未随公开版收录） | 有多种示例和习题；概念规模与经过压测的网络系统不是一回事 |
| 课程出现 BFCL/GAIA 等评估 | 第 12 章（原本地资料引用，未随公开版收录）、评测 README（原本地资料引用，未随公开版收录）、现有模板输出（原本地资料引用，未随公开版收录） | 模板目录里的旧报告/分数属于仓库内容；没有独立复跑或更新结果 |
| 综合项目覆盖 Web/前端/存储/交互 | 旅行助手（原本地资料引用，未随公开版收录）、DeepResearch（原本地资料引用，未随公开版收录）、AI Town（原本地资料引用，未随公开版收录） | 用于静态架构观察；外部依赖未安装、服务未启动 |
| SQLite 作为记忆存储出现，但不是完整数据库工程训练 | 第 8 章存储架构（原本地资料引用，未随公开版收录）、第 15 章架构/记忆（原本地资料引用，未随公开版收录）、项目 `backend/memory_data/` | 教材确实提到 SQLite，目录带示例 DB；本轮没有检查 DB 表结构或并发语义 |
| 第 15 章的背景更新/状态管理是单进程示范 | `state_manager.py`（原本地资料引用，未随公开版收录） | 静态代码可见进程内字典、单例与 `asyncio.create_task`；这说明样例形态，不说明作者未在其他实现扩展 |
| 第 16 章偏向项目组织/共创 | 第 16 章（原本地资料引用，未随公开版收录）、`共创路径.md`（原本地资料引用，未随公开版收录） | 核心 chapter16 目录只有路径文件；其他完整项目在社区汇总目录，不存在统一评分 rubric 的证据 |

## 4. 版本与可复现性记录

- 固定 commit 是本报告的唯一版本锚点。GitHub 仓库搜索页在 2026-10-03 周边显示该仓库最近更新于 2026-09-29；本地 commit 也标为 9 月 29 日。未来复查应使用固定 SHA，不用 `main` 替代。
- 仓库首页“下一步规划”写 HelloAgents 框架 V1.0.0；第 8 章安装段又提示 `hello-agents` 0.2.0 遇到模型问题时看 issue #320 或切换到 0.2.9。它们可能对应不同时间/发布渠道，至少表明不能只从 README 抄一个统一依赖版本。
- 主教材各章各有服务和依赖，未见能够锁定所有章节运行环境的一个根级环境文件。部分子项目有 `requirements.txt`、`pyproject.toml`、Node lockfile；这些只约束各自子项目。
- 第 6 章正文以 AutoGen 0.7.4 为例；依赖版本的“最新”是原文撰写时的表述，不代表本研究已向上游包索引验证当前最新版。
- Python 示例中有 API key、Base URL、provider 和外部服务的配置流程。审阅时只查看了示例文件/配置位置，没有显示、复制或验证任何密钥值。

## 5. 许可与引用方式

仓库 README 的开源协议段及根目录 `LICENSE.txt`（原本地资料引用，未随公开版收录） 指向 **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）**。准确条文应以 [Creative Commons 官方许可文本](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en) 和 项目声明（原本地资料引用，未随公开版收录） 为准。署名、非商业使用和相同方式共享都是该许可名称中的条件；如果要把教材原文、图表或大段代码直接改编进有商业收益的视频，应先核实许可是否适用并取得必要授权。报告中的课程评价和简述是独立文字，引用例子时应保留 Datawhale/原作者/章节链接，避免整段搬运教材内容。

仓库里也存在社区投稿、第三方项目和外链资料。根许可声明不能被自动当成每个第三方素材或外部项目都具有相同权利；逐项引用时仍应看其自身许可证/来源。

## 6. 可复查的本地只读命令

以下命令仅用于读 Git 元数据和目录，不会运行课程代码：

```powershell
$src = 'Agent/research/agent_courses/providers/datawhale/source'
git -C $src remote -v
git -C $src rev-parse HEAD
git -C $src log -1 --format='%H%n%cs%n%s'
git -C $src status --short
git -C $src rev-parse --is-shallow-repository
git -C $src sparse-checkout list
git -C $src ls-files | Measure-Object
rg --files $src/docs $src/code $src/Extra-Chapter
```

对课程覆盖的负面判断均使用有限口径：“在已审阅的主教材或对应章节中未形成完整示范”，不推断整个 Datawhale 社区、外部链接或未来版本都不存在该材料。

