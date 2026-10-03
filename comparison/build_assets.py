"""Build the secondary format inventory and self-contained comparison viewer."""
from pathlib import Path
import json,html,re
P=Path(__file__).resolve().parent
D=json.loads((P/'coverage.json').read_text('utf8'))
# Video / body / code / exercises-projects. Availability is independent of completion.
M={
'datawhale_hello_agents':('未统一确认配套视频','完整中文教材已审阅','公开仓库与正文代码','章节实践、多个项目；毕业设计指导，统一评分标准未确认'),
'deeplearning_ai_agentic_ai':('课程视频；未全部观看','31 份公开转录已审阅','课程宣称代码示例；Notebook 未核验','课程宣称练习/示例；完整作业及评分未核验'),
'huggingface_agents':('部分配套视频入口','单元正文已审阅','公开 Notebook/代码与项目入口','练习、任务基准与项目；评测范围见研究记录'),
'microsoft_ai_agents':('1–13 课视频链接；14–18 未确认','18 课正文已审阅','公开仓库与 Notebook','章节代码练习与案例；统一毕业项目未确认'),
'langgraph_fundamentals':('Academy 课程视频入口','目录/课程说明；Notebook 已审阅','公开 Notebook 仓库','模块练习与研究助手；部署模块，评分未确认'),
'anthropic_platform_101':('课程页面视频入口','13 个公开教学页已获取','正文有示例；独立配套仓库未确认','测验页面存在，内容未完整获取；独立项目未确认'),
'anthropic_claude_api':('课程页面视频入口','67 个公开教学页已获取','正文有代码示例；本轮未逐例验证','测验/工作流案例；统一毕业项目未确认'),
'anthropic_mcp_course':('课程页面视频入口','10 个公开教学页已获取','正文客户端/服务器示例；未运行验证','示例练习；独立项目及评分未确认'),
'openai_building_agents':('此文档路线未确认统一视频','官方指南正文已获取','官方文档示例；公开 SDK','本仓库实验为自行设计，不算官方作业'),
'google_agents_2025':('历史活动回放入口','白皮书、活动材料入口','公开 codelab/Notebook 入口','五天实践与历史 capstone；提交窗口已结束'),
'google_agents_2026_vibecoding':('活动视频/直播入口，逐项未审阅','2026 活动目录/材料入口','codelab 入口；内容未逐例核验','规格、评测、安全与交付实践；完成度未核验'),
'vanderbilt_python_agent_implementation':('Coursera 课程入口','公开简介；完整讲义未获取','实现课程宣称 Python 实践；文件未核验','平台内练习/作业细目未核验'),
'vanderbilt_prompt_engineering':('Coursera 课程入口','公开简介；完整讲义未获取','不以代码实现为主；材料未核验','提示实践；完整作业与评分未核验'),
'vanderbilt_python_agent_architecture':('Coursera 课程入口','公开简介；完整讲义未获取','Python 架构主题；文件未核验','完整实践与评分未核验'),
'generic_agent':('未确认统一配套视频','公开中文指南/目录','公开项目/示例入口，未完整运行','13 章与案例；独立评分体系未确认'),
'freecodecamp_agentic_ai':('公开长视频；未全部观看','章节说明；完整转录未获取','公开配套代码仓库','视频带项目；无统一评分确认'),
'langchain_ambient_agents':('Academy 项目课视频入口','6 模块目录，完整正文未获取','配套项目入口；未逐例审阅','邮件助手项目；环境及评价细则未验证'),
'langchain_deep_agents':('Academy 课程视频入口','5 模块目录，完整正文未获取','公开 lca-deepagents 仓库入口','项目/实践入口；未完成验证'),
'langchain_observability_evaluations':('Academy 课程视频入口','官方详细目录；未完课','示例/配套代码入口；未逐例审阅','数据集、评测实验、反馈实践；未完成验证'),
'huggingface-mcp':('部分演示/配套视频入口','公开单元正文与目录入口','公开课程仓库/示例入口','客户端/服务器实践与应用；未完整核验'),
'nvidia-building-rag-agents':('自学/讲师形式依具体版本','公开模块介绍，完整讲义未获取','课程宣称云端实验环境；公开代码未确认','RAG 实践；账号及课程环境需要另行核验'),
'nvidia-building-agentic-ai-applications':('课程存在；具体形式未核验','简介；逐节目录不足','未确认','未确认'),
'ibm-agentic-ai-in-practice':('学习路径内教程，形式逐项未核验','历史目录快照；当前入口可能调整','教程代码入口未逐项确认','多框架教程；完整项目/评分未核验'),
'dlai-ai-agents-in-langgraph':('短课视频入口','公开目录；完整正文未获取','平台 Code Example 标识；文件未核验','短课实现实践；作业反馈未核验'),
'dlai-multi-ai-agent-systems-crewai':('短课视频入口','公开目录；完整正文未获取','平台 Code Example 标识；文件未核验','多 Agent 案例；评分未核验'),
'dlai-building-coding-agents-tool-execution':('短课视频入口','公开目录；完整正文未获取','平台 Code Example 标识；文件未核验','代码执行/开发案例；评分未核验'),
'berkeley-llm-agents-fall-2024':('公开讲座视频链接','官方讲座目录、讲义/论文入口','讲座提及项目不算配套代码齐全','研究讲座；统一编码作业未确认'),
'berkeley-llm-agents-spring-2025':('课程/讲座入口；逐课未核验','课程页面，细目核验不足','未确认','未确认'),
'berkeley-agentic-ai-fall-2025':('课程/讲座入口；逐课未核验','课程页面，细目核验不足','未确认','未确认'),
'cmu-11768-ai-agents-fall-2026':('公开课次视频入口；课程进行中','课程目录、阅读/PDF 入口','作业说明/资源入口，部分材料未发布','Harness、评测、训练作业与研究项目；未完成'),
}
assert set(M)=={c['id'] for c in D['courses']}
for c in D['courses']:c['materials']=dict(zip(['video','body','code','practice'],M[c['id']]))
(P/'materials.json').write_text(json.dumps({c['id']:c['materials'] for c in D['courses']},ensure_ascii=False,indent=2),'utf8')
rows=['# 第二层：视频、正文、代码与练习\n','先读 [知识矩阵](COVERAGE_MATRIX.md)，再用本表决定学习形式。这里记录材料入口和采集状态，不表示已观看、跑通或完成。配套代码公开、平台内代码和宣称提供实验环境不是同一回事。\n','| 课程 | 视频 | 正文/文档 | 代码 | 练习/项目 |','|---|---|---|---|---|']
for c in D['courses']:
 rows.append('| ['+c['title']+']('+c['source']+') | '+' | '.join(M[c['id']])+' |')
rows+=['\n逐课来源与访问限制见 [研究材料](../research/agent_courses/README.md) 和 [证据账本](EVIDENCE.md)。本表不承诺当前收费、账户权限、证书或运行成本；正文也不意味着有完整独立讲义。']
(P/'MATERIALS.md').write_text('\n'.join(rows),'utf8')
rows=['# 目录原项与共同知识主线的对照\n','保留全部 30 份现有目录图中的模块和条目。这些图本身可能是官方目录的中文归组、主题归纳或简介，并非都拥有完整逐课细目。最后一列是辅助定位候选，不是新增评分依据；未匹配条目仍保留。细目与教学深度以 [证据](EVIDENCE.md) 为准。\n']
for c in D['courses']:
 rows+=['## '+c['title']+'\n',c['basis']+'；[官方入口]('+c['source']+')\n','| 原模块 | 原目录条目 | 可对照节点（待逐课核对） |','|---|---|---|']
 for s in c['sections']:
  for item in s['items']:
   ids=[t['id'] for t in D['topics'] if isinstance(c['cells'][t['id']]['level'],int) and re.search(t['aliases'],item,re.I)]
   rows.append('| '+s['title'].replace('|',' / ')+' | '+item.replace('|',' / ')+' | '+(', '.join(ids) or '保留原项，尚未细分到节点')+' |')
(P/'DIRECTORY_CROSSWALK.md').write_text('\n'.join(rows),'utf8')
rows=['# 各课程在哪些学习阶段展开\n','数字为该阶段已确认节点数 / 本表该阶段节点数，只是当前证据下限，不是覆盖百分比或教学质量。括号列出该阶段确认到的最高材料层次。0 不等于完全不讲；资料不足的格子另列 ? 数量。请用 [详细矩阵](COVERAGE_MATRIX.md) 区分具体节点和证据。\n','| 课程 | '+' | '.join(f'{i+1} {s}' for i,s in enumerate(D['stages']))+' |','|---|'+'---|'*len(D['stages'])]
for c in D['courses']:
 cells=[]
 for s in D['stages']:
  vals=[c['cells'][t['id']]['level'] for t in D['topics'] if t['stage']==s]
  known=[v for v in vals if isinstance(v,int)];unknown=vals.count('?')
  cells.append(f'{len(known)}/{len(vals)}'+(f'（最高 {max(known)}）' if known else '')+(f'；? {unknown}' if unknown else ''))
 rows.append('| '+c['title']+' | '+' | '.join(cells)+' |')
(P/'STAGE_SUMMARY.md').write_text('\n'.join(rows),'utf8')
template=(P/'viewer.template.html').read_text('utf8')
(P/'index.html').write_text(template.replace('/*DATA*/',json.dumps(D,ensure_ascii=False).replace('</','<\\/')),'utf8')
print('Built format inventory, complete catalog crosswalk, standalone viewer')
