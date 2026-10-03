# Anthropic 官方 Agent 教材：来源、保存范围与证据边界

研究快照：2026-10-03（北京时间）。本文件只记录当前工作树中可核对的快照，不代表 Anthropic 网站当前或未来仍使用相同页面、课程结构和接口。

## Academy 课程正文的统计口径

课程抓取目标保存在 provider 根目录的 `academy_lesson_targets.json`、`targets.json` 与 `targets_current.json`；请求结果和正文清单在 `source/academy_lessons/manifest.json`。清单共有 **103 个目标**：其中 **90 页 `public_body`**，其余 13 页为没有可读课程正文的测验/徽章页面（10 个测验、3 个徽章）。90 页按 manifest 中的 course 字段分为：

| 课程 | 正文页 | 纳入统计 |
|---|---:|---|
| `claude-platform-101` | 13 | 是 |
| `building-with-the-claude-api` | 67 | 是 |
| `introduction-to-model-context-protocol` | 10 | 是 |
| 测验与徽章 | 13 | 否；HTML 已保存，但抽出的可读正文为空/需复核 |

可逐页追到课程 URL、页标题、HTTP 状态、抓取时间、字节数、文字长度、SHA-256、raw HTML 路径和抽取 text 路径。人工索引 [lesson_index.md](lesson_index.md) 记录 90 页的课程名、官方标注时长、小标题、原始链接和本地文字路径。`lesson_index.md` 中时长是网页标注时长，不是已实测的完整学习时长。

## 当前 Academy 是公开课程正文；旧 Skilljar 是登录壳

本轮主课程以 `https://academy.claude.com/` 的页面为准。实际页面的 manifest 和正文位于 `source/current/manifest.json` 与 `source/academy_lessons/`。旧站 `https://anthropic.skilljar.com/` 的首页和旧课程入口另记录在 `source/manifest.json`，其 acquisition 标记为 `login_shell`，抽取只有导航/壳文字，不能拿来支持课程讲了什么，也不能将“HTTP 200”当作取得正文。

因此，这批内容的准确说法是：“已取得 Claude Academy 当前站公开文字课程的 90 个教学页面。”不应说“已看完 Anthropic 全部课程”“所有教学视频均可完整观看”或“完成了课程测验”。

## 文字页面与视频的关系

`source/academy_lessons/raw/` 保存 HTML，`source/academy_lessons/text/` 保存提取后的可读文本。正文标题和段落确实可读，但课程页同时标注视频时长，媒体本身没有下载/观看。文本不是视频字幕转写，也未核对旁白是否逐字对应网页文字。后续视频内容、板书/终端演示、停顿和互动都不能从当前快照推断。

本轮用静态阅读判断目录层次、书面解释和可见代码片段。没有登录 Academy、提交练习、拿徽章、跑项目、配置 Anthropic API key、做 API 调用或产生模型费用。示例输出和模型回答只按页面文本引用；课程中的 mock、描述性预期和分数没有当成独立实验结果。

## SDK 文档：旧 `.md` 路径重定向导致重复，使用当前 HTML 快照

`source/manifest.json` 记录了旧 `platform.claude.com/.../*.md` 请求的结果。对于 `sdk-permissions.md`、`sdk-human-review.md`、`sdk-hooks.md`、`sdk-skills.md` 等，HTTP 请求最后都重定向到 Agent SDK overview，返回内容、SHA-256、标题与长度和 overview 相同。因此它们是重复 overview，不是权限、审批、hooks 或 Skills 正文，不能计为已获取的独立文档。

对应正文从 `source/current/manifest.json` 的当前 HTML 页面读取：

- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)
- [Permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
- [User input and approvals](https://code.claude.com/docs/en/agent-sdk/user-input)
- [Hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
- [Skills](https://code.claude.com/docs/en/agent-sdk/skills)
- [Sessions](https://code.claude.com/docs/en/agent-sdk/sessions)
- [Hosting](https://code.claude.com/docs/en/agent-sdk/hosting)
- [Secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [MCP](https://code.claude.com/docs/en/agent-sdk/mcp)
- [Subagents](https://code.claude.com/docs/en/agent-sdk/subagents)
- [Cost tracking](https://code.claude.com/docs/en/agent-sdk/cost-tracking)

上面链接是官网来源，`source/current/manifest.json` 是本地实际抓取事实。页面抓取是静态快照；SDK 的接口、默认权限和版本可能变化，复现时应依目标版本检查官方文档与类型定义。

## Anthropic 工程文章与项目材料

`source/manifest.json` 中 acquisition 为 `public_body` 的 Anthropic 工程资料有 9 篇：

1. [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
2. [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
3. [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
4. [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
5. [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
6. [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
7. [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
8. [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
9. [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)

另外 `source/assets/` 有两个 Claude Code/CLI 项目 ZIP 解包目录：`cli_project_COMPLETE-bkl5xnz8` 与 `cli_project-oeur3rwg`。它们可用于后续静态阅读代码结构；本轮没有执行这些项目、确认外部依赖或把项目代码当作课程作业。

## 可复核目录

| 内容 | 本地证据 |
|---|---|
| Academy 页面清单及状态 | `source/academy_lessons/manifest.json` |
| 课程目标 | provider 根目录的 `academy_lesson_targets.json`、`targets.json`、`targets_current.json` |
| Academy 网页原件与文字 | `source/academy_lessons/raw/`、`source/academy_lessons/text/` |
| 逐课阅读索引 | `lesson_index.md` |
| Anthropic 工程文章、旧 SDK 请求记录 | `source/manifest.json`、`source/raw/`、`source/text/` |
| 当前 SDK HTML 正文 | `source/current/manifest.json`、`source/current/raw/`、`source/current/text/` |
| CLI 项目快照 | `source/assets/` |

相关研究方法见[方法与证据标准](../../methodology.md)。
