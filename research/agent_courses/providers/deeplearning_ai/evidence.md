# DeepLearning.AI Agentic AI 获取范围与证据

研究日期：2026-10-03。采集沿用已有 targets 与采集脚本结果，没有重新下载任何已成功条目。

## 已保存的来源

| 来源 | 本地材料与观测 | 可以支持的判断 |
|---|---|---|
| 官方课程页 | [deeplearning.ai/courses/agentic-ai](https://www.deeplearning.ai/courses/agentic-ai)，targets.json 的 agentic_ai_official_course；存档正文只有 88 字符，manifest 标 needs_review | 可确认课程入口与题名，不能从这份文本重建完整课程目录或全部课程正文。 |
| 官方学习平台 | [learn.deeplearning.ai/courses/agentic-ai](https://learn.deeplearning.ai/courses/agentic-ai)，source/web 与 source/web_lessons | 课程页和 12 个选定 lesson 请求返回 200，但抽取文字是相同的播放器/学习环境提示壳。已在各 manifest 纠正为 player_shell；不要把它们视作正文。课程页面登录/注册控件可见，但本轮未登录人工核验后续权限、付费状态或作业可见性。 |
| 视频页面与转录 | source/videos/raw、source/videos/text、source/videos/transcripts、manifest.json 与 transcript_manifest.json | 共存有 31 个视频 lesson 请求与 31 个纯文本转录。转录长度约 1,978–15,314 字符，保留标题、lesson URL、视频 ID、哈希和路径。它们支持对讲师口头内容作静态分析；本轮未播放/观看视频，也没有核对时间轴、画面或平台课程总 lesson 数。 |
| 官方社区目录 | [Agentic AI Lecture Notes](https://community.deeplearning.ai/t/agentic-ai-lecture-notes/881566)，source/web/text/agentic_ai_public_lecture_notes_index.txt | 列出课程五模块名称，并提醒讲义未持续维护、可能漏项或出错，学习者应以课程视频为准。该页是课程社区目录线索，不等同官方 lesson 本文。 |
| 公开课程讨论 | [M3 Tool use 讨论](https://community.deeplearning.ai/t/agentic-ai-m3-ugl-1-hardcoded-function/884733)、[Email Assistant Lab 讨论](https://community.deeplearning.ai/t/ungraded-lab-email-assistant-workflow-prompt-to-delete-email-by-subject/891566) | 是学员/社区对不评分实验的具体问题或代码建议，属于补充讨论。它们不证明所有学员都会遇到同一问题，也不能替代课程实验源码。 |

## 关键本地证据

- Research Agent 和拆分工作流：source/videos/transcripts/video_nae3i1.txt、video_moivygo8.txt、video_jcl177.txt、video_wr78er.txt、video_egr0a8.txt。
- Agent 边界与模式：video_zqs9ty.txt（autonomy degrees）、video_rm9bg7.txt（design patterns）。
- Reflection：video_shknq1.txt、video_vtzr25.txt、video_txqmf0.txt。
- 工具与协议：video_3s0czq.txt、video_154qpw.txt、video_79cpry.txt、video_a4gs14.txt、video_x7jowg.txt。
- 评测与迭代：video_46yh5j.txt、video_pu5xbl.txt、video_2ftglp.txt、video_0kbds1.txt、video_ldf4ci.txt、video_fwxyds.txt、video_154qpa.txt、video_hl2aj7.txt。
- 多 Agent：video_608l3n.txt、video_gymk4l.txt。
- 页面正文误判的纠正依据：31 个 video player text 文件逐个比较后内容字节哈希相同；12 个 web_lessons text 文件也只有同一播放器帮助壳。相应 manifest acquisition 已改为 player_shell，转录另存于 transcripts 目录。

## 未获取/未验证

当前来源没有完整 lesson 正文、平台内 Notebook/实验 starter code、评分测验答案、全课程许可与价格详情。个别课程社区帖提及未评分 Lab，不代表拿到了该 Lab 的代码。视频文本是转录而非逐秒观看记录；若需要引用讲师原句、代码或 slides，需打开对应官方 lesson/video 重新核对。没有声称已经完成课程、实作或证书。
