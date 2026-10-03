# Agent 连续教学资源补充：新增开放选择

核验日期：2026-10-03。本文按官方项目页、课程站和课程发布页的公开目录做静态审阅，供 Agent 教材选择视频比较。没有据此声称完整学习课程、完成作业或运行示例。

## 快速比较

| 资源 | 适合起点 | 教学形式与主线 | 可访问范围 |
|---|---|---|---|
| Datawhale《Generic Agent 使用指南》 | 中文入门者；想看一个具体 Agent 如何组成 | 中文在线文字，应用指南 → 架构原理 → 场景案例 | GitHub 与在线正文公开；教程标注 Beta 公测 |
| freeCodeCamp《Agentic AI – Complete Course for Beginners》 | 会基本 Python，想跟长视频从单 Agent 走到项目部署 | 英文约 24 小时视频，配套代码仓库；基础、单/多 Agent、工作流与综合项目 | 视频和代码公开；接模型/API及云端部署的练习可能需要账号或付费额度 |
| CMU 11-768《AI Agents》（Fall 2026） | 有较强 Python、AI/ML 与语言模型背景的研究生 | 课程讲授、阅读、作业与研究项目；涉及工具、规划、记忆、训练、安全、编码/GUI Agent | 课程站公开课程安排、部分课件和录像链接；2026 秋季进行中，具体课堂与作业访问以课程站为准 |

## 1. Datawhale《Generic Agent 使用指南》

- [官方 GitHub 项目与目录](https://github.com/datawhalechina/hello-generic-agent) · [在线阅读](https://datawhalechina.github.io/hello-generic-agent/)
- **教学内容：**分为应用指南、原理篇、案例篇。目录从安装、浏览器能力、日常使用、记忆与技能、聊天平台集成，进到 Agent 循环、工具集、分层记忆、上下文压缩、自我进化等原理，再以办公和网络任务案例串联。当前目录列有 13 个章节和 5 个案例。
- **适合的起点：**仓库称无基础要求，面向想先用起来、再拆解具体智能体架构的学习者。若要深入读实现，具备基本 Python 阅读能力会更容易。
- **材料形式：**中文网页正文与公开代码仓库；可从应用指南开始，也可以直接读原理篇或案例篇。
- **范围边界：**这是围绕 Generic Agent 这一具体项目的使用和架构教程，不是通用 Agent 框架横向课程。仓库把版本标为 Beta 公测并称主体已完成；目录中有关效率的项目方表述没有在本次研究中独立验证。

## 2. freeCodeCamp《Agentic AI – Complete Course for Beginners》

- [freeCodeCamp.org 发布的视频](https://www.youtube.com/watch?v=Zy7EXDONlTY) · [播放列表](https://www.youtube.com/playlist?list=PLkz_y24mlSJZ9SFlc9O4Q4Grli5SQDbrB) · [讲师配套代码仓库](https://github.com/entbappy/Complete-Agentic-AI-Course)
- **教学内容：**从 Agentic AI 基础、异步 Python 和 Pydantic，进入 LangChain 单 Agent/多 Agent，再通过 LangGraph 工作流与聊天机器人项目讲记忆、工具、RAG、人机介入、监控和部署。代码仓库有 Advanced RAG、异步编程、LangChain 多 Agent、LangGraph 等项目目录。
- **适合的起点：**会基本 Python，想按一个连续视频跟做的人。标题面向初学者，但项目部分涉及 API、数据库和部署环境。
- **材料形式：**英文长视频，YouTube 元数据显示时长约 24 小时 16 分钟；另有公开代码仓库和独立讲师播放列表。
- **范围边界：**课程由讲师 Bappy 授课、由 freeCodeCamp.org 频道发布；不应写成 freeCodeCamp 自编课程。它有较大篇幅讲 LangGraph，因此与现有 LangGraph 教材有部分重复。代码开放不代表模型 API、数据库或云部署都免费。

## 3. CMU 11-768《AI Agents》（Fall 2026）

- [课程站](https://www.cmu-agents.com/) · [公开讲座录像播放列表](https://www.youtube.com/playlist?list=PLSN0qpDfUvTM) · [示例：Lecture 1 slides](https://www.cmu-agents.com/slides/lecture-01-agents.pdf)
- **教学内容：**课程站将其列为卡内基梅隆大学 Fall 2026 研究生课程，主题是基于 LLM 的 Agent。目录包含工具使用、长上下文管理、规划、记忆、训练、Agent 安全与人机交互；作业包括构建 coding-agent harness、设计评测框架、实现 Agent 训练方法，另有研究项目。
- **适合的起点：**已有 AI/机器学习基础、熟悉 Python，且有训练神经语言模型经验的研究生。课程站列出的背景要求明显高于一般应用开发入门课。
- **材料形式：**课程安排、阅读列表、课件 PDF、公开讲座录像链接和作业说明；课程站列出讲座录播入口，例如工具使用等主题。
- **范围边界：**截至核验日，Fall 2026 学期进行中。课程目录和部分教学链接可以公开访问，但它是大学学期课程，不是保证所有讨论、作业反馈与课堂活动都对外开放的自学 MOOC；本条只按公开课程站目录记录。

## 本轮未另列的候选

smolagents 已作为 Hugging Face Agents Course 的一部分收录；LlamaIndex 目前核实到的是官方 starter 文档、示例笔记本和工作流文档，没有找到足以独立计为连续课程的开放课程目录，因此不把文档重复计作一门课。
