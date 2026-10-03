# Agent 入门教材研究资料库

> 公开版说明：本目录收录研究分析与来源索引；下文提到的 `source/`、采集工具和原始正文属于原研究档案，未随本仓库发布。获取统计描述当时的采集范围，不是本仓库附带的文件数。
研究日期：2026-10-03。用途：对照公开课程、教材、文档与项目的内容结构，并记录研究范围和证据依据。

## 建议先看

1. [跨课程比较](comparative_review.md)：教材类型、不同起点与搭配关系。
2. [课程与面经对应](interview_alignment.md)：把原牛客帖里的追问定位到具体教材，标出缺口。
3. [术语解释](glossary.md)：操作边界、harness、编排、query、意图分流等，附例子和误区。
4. [18个取材练习](worked_examples.md)：同一问题在不同教材里怎样解释、怎样验证。
5. [学习体验审阅](learning_experience_audit.md)：静态审阅结论与实际亲测的区别。

## 教材分档案

每个主体的 `analysis.md` 是综合分析，`curriculum.md` 是章节地图，`evidence.md` 是获取范围与复核依据，`source/` 是原始材料。课程正文里的内容与我们的归纳分开放置。

| 材料 | 深度分析 | 章节地图 | 获取范围 / 证据 |
|---|---|---|---|
| Datawhale Hello-Agents | [分析](providers/datawhale/analysis.md) | [目录](providers/datawhale/curriculum.md) | [证据](providers/datawhale/evidence.md) |
| Hugging Face Agents Course | [分析](providers/huggingface/analysis.md) | [目录](providers/huggingface/curriculum.md) | [证据](providers/huggingface/evidence.md) |
| Microsoft AI Agents for Beginners | [分析](providers/microsoft/analysis.md) | [目录](providers/microsoft/curriculum.md) | [证据](providers/microsoft/evidence.md) |
| Anthropic Academy + SDK +工程说明 | [分析](providers/anthropic/analysis.md) | [目录](providers/anthropic/curriculum.md) | [证据](providers/anthropic/evidence.md)；[90节公开文字课索引](providers/anthropic/lesson_index.md) |
| OpenAI学习路线 + Agent/SDK说明 | [分析](providers/openai/analysis.md) | [目录](providers/openai/curriculum.md) | [证据](providers/openai/evidence.md) |
| LangChain Academy / LangGraph | [分析](providers/langchain/analysis.md) | [目录](providers/langchain/curriculum.md) | [证据](providers/langchain/evidence.md) |
| DeepLearning.AI Agentic AI | [分析](providers/deeplearning_ai/analysis.md) | [目录](providers/deeplearning_ai/curriculum.md) | [证据](providers/deeplearning_ai/evidence.md) |
| Berkeley Agent MOOC | [分析](providers/berkeley/analysis.md) | [目录](providers/berkeley/curriculum.md) | [证据](providers/berkeley/evidence.md) |
| HF MCP补充课 | [有限范围分析](providers/extras/analysis.md) | 文内目录 | 文内获取边界 |

新增：[DeepLearning.AI三门专题短课](providers/deeplearning_ai/short_courses_supplement.md)，补充LangGraph、crewAI多Agent协作与Coding Agent代码执行。仅核实官方简介和目录，尚未获取完整课文或运行练习。

继续扩充：[框架工程与大学课程](additional_framework_university_courses.md)，包含LangChain Deep Agents、独立评测课、邮件助手项目课及Vanderbilt Python Agent系列。仅按官网目录审阅，尚未完成课程实践。

完整新增名单见[课程选择扩充表](expanded_course_choices.md)：本轮补充11项非DeepLearning.AI资源，按实际形式区分课程、开源教材和厂商学习路径。

## “获取课程”具体指什么

- 开源仓库：固定提交中的文字与代码，可以本地阅读；浅克隆不含完整历史，稀疏克隆不含全部语言路径。
- 网页课程：保存公开正文与获取记录；HTML200但仅登录壳，不算已获取课程。
- 官方文档：按选定Agent学习范围获取，不代表整个平台所有API文档。
- 视频、交互测验、账号后的作业或付费资源：未获取部分明确记录。网页里的课程介绍不能代替完整课文。
- 本轮学习体验是**静态文字与代码审阅**；未跑完课程、未调用付费模型、未获得证书。设计的例子标为未运行。

尤其值得注意：Anthropic当前Academy已有连续的Platform101、Claude API及MCP文字课程，不能继续把它概括成“只有零散官方文章”。反过来，官方SDK文档也不能因为内容权威就视为完整本科式教材。

## 完整性与来源边界

[方法与证据标准](methodology.md)；离线资料清单（原研究档案引用，未随公开版收录）。清单中的文件数包括图片、代码、HTML、翻译等，**不是课时数，也不是全部已审阅数量**。

原仓库许可证保留于各 `source/`。来源网页未明确开放许可时，研究采集不等于可再分发完整教材。公开归纳应以独立分析、必要的少量摘录和原始链接为主，并遵循各来源许可。
