# 补充：Hugging Face MCP Course

研究日期：2026-10-03。重点是协议课程目录与可获取代码；没有逐页审阅全部课文、运行服务、提交证书或调用外部系统。主Agent课程已有[独立分析](../huggingface/analysis.md)，这里不重复评价。

官方入口：[MCP Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction)。本地仓库：source/huggingface-mcp-course（原本地资料引用，未随公开版收录），固定提交`3b437221016136f02fcd5fc17bf5429d5b7024cc`；清点时120条提交树文件均落盘。目录直接依据英文_toctree.yml（原本地资料引用，未随公开版收录）。仓库包含LICENSE、requirements、units、quiz及projects。

## 可确认的课程结构

| 部分 | 目录内容 | 学习目标 |
|---|---|---|
| Unit0 | 欢迎与课程说明 | 确认前提与学习方式。 |
| Unit1 | 术语、架构、通信、能力、SDK、clients、HF server、Gradio集成、测验 | 分清host/client/server与协议能力。 |
| Unit2 | Gradio server/client、Continue客户端、Tiny Agents、本地加速路线 | 把服务接到实际应用。 |
| Unit3 | 自定义workflow server、GitHub Actions、Slack通知、PR Agent解答 | 用协议组织开发工作流。 |
| Unit3.1 | 在Hub构建PR Agent | 另一组集成项目入口，具体实现需深入读课文。 |

## 如何放进你的教材综述

它适合作为基础loop与工具课之后的专题：已经知道模型请求工具和程序执行工具，再学协议怎样统一发现和调用。目录提供概念→SDK→端到端应用→开发工作流的结构，具有连续性；但“有章节”不能直接证明每节练习质量、解释完整性或实际可复现性。

可取材的例子包括：Gradio服务接客户端、AI coding assistant接MCP、Tiny Agent接工具、PR工作流接GitHub Actions、发Slack通知。这里的通知和PR属于可能产生外部副作用的能力，后续亲测要定义授权、执行范围和失败策略；本轮没有发送通知或操作远程仓库。

MCP解决连接与协议问题，不自动解决Agent规划、Skill加载、用户意图歧义或写操作批准。面经问Skill/Tool/MCP时可以以它作协议补充；harness、事务、幂等、租户隔离和容量仍要看其他教材或实践。不要把MCP课宣传成全部Agent开发入门。

## 获取与体验边界

source/web/manifest.json（原本地资料引用，未随公开版收录）另存七个HF课程入口的抓取记录，其中部分是主Agent课，不能再计为七门新课程。extras中的Agent仓库副本与主HF档案为相同提交，不构成额外教材或独立研究样本。

本轮静态审阅可确认目录、材料形式和项目方向，尚不能确认每个项目当前安装成功、模型费用或真实用户体验。中文支持、认证条件及更新政策需要录制前查当前官方页面；这里不据有限目录作完整结论。
