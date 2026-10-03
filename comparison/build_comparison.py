"""Build a reviewed topic crosswalk. Ratings are authored, not keyword scores.
Evidence excerpts are located in existing reviews; incomplete evidence lowers ratings.
"""
from pathlib import Path
import json,re,csv,io,html
ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/'assets/course_maps/catalog.json').read_text('utf8'))
ORDER=re.findall(r'\]\(courses/([^/]+)/README.md\)',(ROOT/'README.md').read_text('utf8'))
CAT=sorted(CAT,key=lambda c:ORDER.index(c['id']))
STAGES=['概念与基础','最小执行闭环','流程与决策','状态、记忆与人机交互','知识与上下文','协作、协议与框架','评测与优化','交付、安全与运行','应用形态','研究与扩展']
RAW=[
(1,0,'Agent、Workflow与自主程度','Agent|智能体|自主|Workflow','区别直接回答、固定流程与自主执行；发展史属于补充背景'),
(2,0,'LLM、消息、Token与模型选择','语言模型|LLM|消息|token|Token|模型选择','理解请求和上下文；不要求先掌握全部模型训练原理'),
(3,0,'提示、指令与Prompt Patterns','提示|prompt|Prompt|指令','写清目标、限制与输出要求'),
(4,0,'Python、异步与类型化编程基础','异步|Pydantic|Python基础','课程明确教授这些基础才计入；要求会Python不算覆盖'),
(5,1,'Agent loop、ReAct与停止条件','循环|loop|ReAct|步数','跟踪思考/调用/观察/停止；只会调用SDK不等于理解循环'),
(6,1,'工具定义、发现与实际调用','工具|Tool|function calling|函数调用','区分模型请求与程序执行；schema、注册、结果回填'),
(7,1,'结构化输出与参数校验','结构化|structured|schema|Schema|参数格式|Pydantic','类型合法与业务合法分开'),
(8,1,'执行反馈、异常与重试','错误|异常|反馈|error|failure','把失败带回下一轮，限制重试，避免伪造成功'),
(9,1,'文件、代码执行与沙箱','沙箱|sandbox|文件|代码执行|Terminal','隔离执行与文件访问；不是单纯生成代码文本'),
(10,2,'链式工作流、Query与意图路由','路由|Router|routing|query|intent|意图|工作流','识别任务，选路径，缺参数时澄清'),
(11,2,'任务分解、规划与重规划','规划|plan|Plan|分解','把目标拆成执行步骤并根据反馈修订'),
(12,2,'反思、自检与修订','反思|Reflection|reflection|元认知','生成、检查、修订；自评不自动可靠'),
(13,2,'图编排、节点、边与状态Schema','LangGraph|State|状态|节点|图基础','显式控制流及状态更新规则'),
(14,2,'并行、子图与Map-Reduce','并行|子图|Map|parallel|concurrent','并发执行与合并结果；子图不同于自主子Agent'),
(15,3,'短期记忆与会话历史','短期|会话|history|消息|记忆','区分上下文窗口内历史与持久状态'),
(16,3,'长期、共享与分层记忆','长期|跨会话|共享记忆|分层记忆|Store|Profile|Collection','持久偏好、知识和多Agent共享内容'),
(17,3,'Checkpoint、持久化与恢复','checkpoint|checkpointer|持久|恢复|serialize|Sqlite','暂停、进程故障和历史重放；有记忆不自动有恢复'),
(18,3,'人工介入、批准与交接','人工|批准|human|HITL|中断|审批','查看或修改状态、批准动作并继续'),
(19,4,'上下文选择、压缩、卸载与缓存','上下文|context|摘要|裁剪|缓存|压缩','选择放入模型的信息并管理长任务'),
(20,4,'文档加载、切分与摘要','切分|chunk|长文|文档处理|摘要','把原始文档变成可检索材料'),
(21,4,'Embedding、向量库与索引','Embedding|embedding|向量|Vector|FAISS','语义检索、存储与索引'),
(22,4,'混合检索、BM25、RRF与重排','BM25|RRF|重排|rerank|检索策略|词法','超出基础向量检索的质量改进'),
(23,4,'Agentic RAG与检索工具','RAG|QueryEngine|检索','把检索作为Agent可选择和迭代的动作'),
(24,5,'多Agent角色、分工与通信','多Agent|多智能体|Multi|multi|AutoGen|crewAI|CrewAI','何时需要多个角色，如何协调'),
(25,5,'Handoff、Agent-as-tool与委派','handoff|Handoff|manager|子Agent|委派|移交','比较控制权移交与将专家作为工具'),
(26,5,'Skills与可复用能力','Skill|技能','可复用任务说明、资源及其加载方式'),
(27,5,'MCP客户端、服务器与原语','MCP|Model Context Protocol','工具、资源、提示、调试及集成'),
(28,5,'A2A、ANP与跨Agent互操作','A2A|ANP|Agent协议|通信协议','跨Agent服务交互；不能把MCP自动计作A2A'),
(29,5,'框架抽象、手写框架与选型','框架|Framework|framework|LangChain|smolagents','比较实现结构；调用一个库不等于框架选型课'),
(30,6,'Trace、Span与运行可观测性','trace|Trace|观测|监控|OpenTelemetry','解释一次执行路径、耗时及失败位置'),
(31,6,'评测数据集、实验与版本对照','数据集|dataset|gold set|实验|评测','建立固定输入并比较模型、提示或系统版本'),
(32,6,'指标、Judge与任务基准','Judge|judge|GAIA|BFCL|指标|评分|Evaluat','答案、组件与轨迹要分开评测'),
(33,6,'错误归因、迭代与回归','错误分析|失败|归因|迭代|回归|Experiments','先定位组件，再修复和复测'),
(34,6,'成本、延迟与模型优化','成本|延迟|latency|cache|模型路由','测量之后再优化；免费课不等于零运行成本'),
(35,7,'服务部署、UI/API集成与交付','部署|deployment|Deployment|Gradio|FastAPI|LangServe','从Notebook变成可以使用的服务'),
(36,7,'扩展、并发、外部状态与生命周期','并发|concurrency|scalable|Redis|PostgreSQL|生命周期','多请求隔离、容量与服务状态；不是能部署就覆盖'),
(37,7,'授权、Guardrails与操作边界','权限|护栏|guardrail|授权|RBAC|可信|边界','策略执行、工具校验、身份与批准的区别'),
(38,7,'不可信输入、注入与数据安全','注入|poison|不可信|PII|安全|Security','检索、网页和工具返回可能携带攻击内容'),
(39,7,'审计、动作凭据、幂等与回滚','receipt|审计|可逆|rollback|回滚|篡改','这些是相关子主题；覆盖其中一项不代表整组均覆盖'),
(40,7,'本地模型、本地Agent与混合运行','本地|Local|SLM|离线|hybrid','硬件、模型能力及云/本地分流'),
(41,8,'Coding Agent与开发Harness','Coding|coding|代码库|软件开发|harness|Next.js','围绕代码修改、运行与反馈组织开发任务'),
(42,8,'浏览器与Computer Use','浏览器|Browser|browser|Computer|Playwright','观察网页并执行有边界的动作'),
(43,8,'多模态、视觉与环境输入','多模态|视觉|vision|multimodal','处理图像等环境信息'),
(44,8,'端到端应用与综合项目','项目|助手|案例|应用|capstone|Assignment','案例是整合机会；不因不同业务场景重复增加知识点'),
(45,9,'SFT、LoRA与Agentic RL','微调|LoRA|SFT|GRPO|RL|训练','模型训练是进阶分支，并非应用开发统一前提'),
(46,9,'研究论文、能力基准与研究方法','论文|研究|GAIA|BFCL|benchmark|科学','研究讲座深度与编码实践深度分别理解'),
(47,9,'游戏、具身与机器人Agent','游戏|Pokemon|Pokémon|机器人|GR00T|具身|赛博','与环境连续交互的扩展方向'),
(48,9,'Vibe Coding与规格驱动开发','Vibe|规格','自然语言开发与规格约束，不自动等于Agent基础'),
(49,5,'低代码平台与流程搭建','低代码|Coze|Dify|n8n|FastGPT','平台式构建与手写框架分开'),
]
TOPICS=[dict(id=f'K{n:02}',stage=STAGES[s],stage_index=s,title=t,aliases=a,description=d) for n,s,t,a,d in RAW]
PRECISE={'K02':'大语言模型|token|模型选择|messages|Tokens|LLM基础','K09':'沙箱|sandbox|代码执行|Terminal|文件系统|文件操作','K13':'LangGraph|StateGraph|reducer|图编排|节点|图基础','K15':'短期|会话历史|history|对话历史|短时|会话记忆'}
for t in TOPICS:t['aliases']=PRECISE.get(t['id'],t['aliases'])
TOPICS.sort(key=lambda t:(t['stage_index'],int(t['id'][1:])))
# Explicit reviewed candidate levels: 1 directory/intro; 2 explanation; 3 concrete implementation/assignment examined in reviews.
RATINGS={
'datawhale_hello_agents':'1:2 2:3 3:3 5:3 6:3 7:3 8:2 9:3 10:3 11:3 12:3 13:3 15:3 16:3 19:3 20:3 21:3 22:2 23:3 24:3 25:2 27:3 28:3 29:3 31:3 32:3 34:2 35:3 39:1 41:3 44:3 45:3 46:2 47:3 49:3',
'deeplearning_ai_agentic_ai':'1:2 3:2 5:2 6:2 7:2 8:2 9:2 10:2 11:2 12:2 14:2 24:2 25:2 27:2 31:2 32:2 33:2 34:2 41:2 44:2',
'huggingface_agents':'1:2 2:2 3:3 5:3 6:3 7:3 8:2 9:3 10:3 11:2 13:3 14:2 15:3 16:2 19:2 20:3 21:3 22:1 23:3 24:3 25:3 27:3 29:3 30:3 31:3 32:3 33:2 34:2 35:3 37:2 38:1 42:3 43:3 44:3 45:3 46:2 47:3',
'google_agents_2025':'1:1 5:1 6:1 15:1 16:1 18:1 24:1 27:1 28:1 30:1 31:1 32:1 35:1 44:1',
'google_agents_2026_vibecoding':'1:1 6:1 26:1 31:1 32:1 35:1 37:1 38:1 48:1',
'vanderbilt_python_agent_implementation':'5:1 6:1 9:1 29:1 44:1',
'vanderbilt_prompt_engineering':'3:1 44:1',
'vanderbilt_python_agent_architecture':'10:1 16:1 24:1 39:1',
'microsoft_ai_agents':'1:2 2:2 3:3 5:3 6:3 7:3 8:2 9:3 10:3 11:3 12:3 13:3 14:3 15:3 16:3 17:3 18:3 19:3 20:2 21:3 22:3 23:3 24:3 25:3 26:1 27:3 28:3 29:3 30:3 31:3 32:3 33:2 34:3 35:3 36:3 37:3 38:2 39:3 40:3 41:2 42:3 43:3 44:3',
'generic_agent':'1:1 5:1 6:1 15:1 16:1 19:1 26:1 35:1 41:1 42:1 44:1',
'freecodecamp_agentic_ai':'1:1 4:1 5:1 6:1 7:1 8:1 10:1 13:1 15:1 16:1 18:1 23:1 24:1 29:1 30:1 35:1 44:1',
'langgraph_fundamentals':'1:2 3:2 5:3 6:3 7:3 10:3 11:2 13:3 14:3 15:3 16:3 17:3 18:3 19:3 23:3 24:3 29:3 34:1 35:3 36:3 39:3 44:3',
'langchain_ambient_agents':'10:1 13:1 15:1 16:1 18:1 19:1 31:1 32:1 35:1 44:1',
'anthropic_platform_101':'1:2 2:2 3:2 5:3 6:3 7:2 9:1 15:2 19:2 26:2 27:2 29:1 35:1 41:1 44:2',
'anthropic_claude_api':'1:2 2:3 3:3 5:3 6:3 7:3 8:3 9:3 10:3 14:3 15:3 19:3 20:3 21:3 22:3 23:3 24:2 27:3 31:3 32:3 33:3 34:2 37:1 41:2 43:3 44:3',
'anthropic_mcp_course':'6:3 27:3 29:1 35:2 44:2',
'openai_building_agents':'1:2 2:2 3:3 5:2 6:3 7:3 8:2 10:3 15:3 17:3 18:3 24:3 25:3 29:2 30:3 31:2 32:2 33:2 34:2 37:3 44:3',
'langchain_deep_agents':'5:1 6:1 9:1 15:1 16:1 17:1 18:1 19:1 25:1 26:1 27:1 35:1 40:1 41:1 44:1',
'langchain_observability_evaluations':'3:1 30:1 31:1 32:1 33:1 35:1',
'huggingface-mcp':'6:1 27:1 35:1 41:1 44:1',
'nvidia-building-rag-agents':'2:1 6:1 15:1 19:1 20:1 21:1 23:1 29:1 32:1 35:1 37:1 44:1',
'nvidia-building-agentic-ai-applications':'11:1 13:1 19:1 29:1 44:1',
'ibm-agentic-ai-in-practice':'1:1 5:1 6:1 10:1 13:1 23:1 24:1 29:1 35:1 44:1',
'dlai-ai-agents-in-langgraph':'5:1 6:1 10:1 13:1 15:1 17:1 18:1 23:1 29:1 44:1',
'dlai-multi-ai-agent-systems-crewai':'6:1 8:1 14:1 15:1 16:1 24:1 25:1 29:1 37:1 44:1',
'dlai-building-coding-agents-tool-execution':'5:1 8:1 9:1 19:1 35:1 41:1 44:1',
'berkeley-llm-agents-fall-2024':'1:1 5:1 11:1 13:1 23:1 24:1 29:1 32:1 37:1 38:1 41:1 42:1 43:1 46:1 47:1',
'berkeley-llm-agents-spring-2025':'1:1 46:1',
'berkeley-agentic-ai-fall-2025':'1:1 46:1',
'cmu-11768-ai-agents-fall-2026':'1:1 6:1 9:1 11:1 15:1 16:1 19:1 31:1 32:1 37:1 38:1 41:1 44:1 45:1 46:1',
}
DOCS={
'datawhale_hello_agents':'providers/datawhale/curriculum.md','huggingface_agents':'providers/huggingface/curriculum.md','microsoft_ai_agents':'providers/microsoft/curriculum.md',
'deeplearning_ai_agentic_ai':'providers/deeplearning_ai/curriculum.md','langgraph_fundamentals':'providers/langchain/curriculum.md','openai_building_agents':'providers/openai/curriculum.md',
'anthropic_platform_101':'providers/anthropic/curriculum.md','anthropic_claude_api':'providers/anthropic/curriculum.md','anthropic_mcp_course':'providers/anthropic/curriculum.md',
}
PARTIAL={'vanderbilt_python_agent_implementation','vanderbilt_prompt_engineering','vanderbilt_python_agent_architecture','nvidia-building-agentic-ai-applications','berkeley-llm-agents-spring-2025','berkeley-agentic-ai-fall-2025','ibm-agentic-ai-in-practice'}
def doc_for(id):
 if id in DOCS:return 'research/agent_courses/'+DOCS[id]
 if id.startswith('dlai-'):return 'research/agent_courses/providers/deeplearning_ai/short_courses_supplement.md'
 if id.startswith(('langchain_','vanderbilt_')):return 'research/agent_courses/additional_framework_university_courses.md'
 if id.startswith(('google_','nvidia-','ibm-')):return 'research/agent_courses/additional_vendor_courses.md'
 if id.startswith('berkeley-'):return 'research/agent_courses/providers/berkeley/curriculum.md'
 if id=='huggingface-mcp':return 'research/agent_courses/providers/extras/analysis.md'
 return 'research/agent_courses/additional_open_courses.md'
def lines_for(c):
 doc=doc_for(c['id']);lines=(ROOT/doc).read_text('utf8').splitlines()
 # Provider docs cover multiple courses. Never transfer sibling-course evidence.
 if c['id'].startswith('anthropic_'):
  doc='research/agent_courses/providers/anthropic/lesson_index.md'
  key={'anthropic_platform_101':'claude-platform-101','anthropic_claude_api':'building-with-the-claude-api','anthropic_mcp_course':'introduction-to-model-context-protocol'}[c['id']]
  lines=[l for l in (ROOT/doc).read_text('utf8').splitlines() if '/courses/'+key+'/' in l]
 # For outline-only reviews use this course's own catalog, never a sibling's prose.
 elif c['id'] not in DOCS:
  lines=[]
 elif c['id']=='openai_building_agents':
  cut=next((i for i,l in enumerate(lines) if l.startswith('## ') and ('实验' in l or '练习' in l)),len(lines))
  lines=lines[:cut]
 if c['id'] in {'datawhale_hello_agents','huggingface_agents','microsoft_ai_agents','deeplearning_ai_agentic_ai','langgraph_fundamentals'}:
  analysis=str(Path(doc).with_name('analysis.md')).replace('\\','/')
  lines += ['@@'+analysis+'@@'+l for l in (ROOT/analysis).read_text('utf8').splitlines() if not l.startswith('#')]
 return doc,lines
COURSES=[];LEDGER=[]
for c in CAT:
 id=c['id'];ratings={f'K{int(k):02}':int(v) for k,v in (x.split(':') for x in RATINGS[id].split())}
 doc,lines=lines_for(c);cells={}
 for t in TOPICS:
  key=t['id'];level=ratings.get(key); candidates=[]
  if level:
   candidates=[l.strip() for l in lines if re.search(t['aliases'],l,re.I) and not l.startswith('#') and len(l)>20 and not re.search(r'研究基准|盘点日期|静态审阅|来源边界|本地快照',l)]
   if key=='K10':candidates=[l for l in candidates if not re.search(r'Q/K/V|Attention',l)]
   candidates.sort(key=lambda l:sum(bool(re.search(a,l,re.I)) for a in t['aliases'].split('|')),reverse=True)
   catalog_lines=[s['title']+': '+'、'.join(s['items']) for s in c['sections'] if re.search(t['aliases'],s['title']+' '.join(s['items']),re.I)]
   if level>=2 and not candidates:level=1
   if level==3 and not any(re.search(r'notebook|脚本|示例|代码|练习|\.ipynb|Python|config|实现|作业',l,re.I) for l in candidates):level=2
   if not candidates and not catalog_lines:
    cells[key]={'level':'?','reason':'候选主题尚未定位到该课程的明确目录或正文依据，待核验'}
    continue
   if id.startswith('anthropic_'):level=min(level,2) # index proves explanation headings, not code inspection
   if level==3:
    candidates.sort(key=lambda l:not bool(re.search(r'notebook|脚本|示例|代码|练习|\.ipynb|Python|config|实现|作业',l,re.I)))
   evidence=(candidates or catalog_lines)[0]
   evidence_doc=doc
   if evidence.startswith('@@'):_,evidence_doc,evidence=evidence.split('@@',2)
   cells[key]={'level':level,'review':evidence_doc,'locator':evidence[:1100],'source':c['source'],'evidence_kind':'正文/代码静态审阅' if level>=2 else '目录/简介主题'}
   LEDGER.append({'course_id':id,'course':c['title'],'topic_id':key,'topic':t['title'],'level':level,'review':evidence_doc,'locator':evidence[:1100],'source':c['source']})
  else:cells[key]={'level':'?' if id in PARTIAL else '—','reason':'课程细目或当前访问范围不足' if id in PARTIAL else '在当前审阅范围中未定位到明确证据，不等于完整课程没有'}
 c={**c,'cells':cells,'review':doc,'scope':'细目有限' if id in PARTIAL else '有目录或内容地图','counts':{str(k):sum(x['level']==k for x in cells.values()) for k in [1,2,3,'?','—']}}
 COURSES.append(c)
OUT=ROOT/'comparison';OUT.mkdir(exist_ok=True)
DATA={'date':'2026-10-03','taxonomy_version':'1.0','stages':STAGES,'topics':TOPICS,'courses':COURSES,'depth_labels':{'1':'目录明确列出','2':'正文/转录中有解释','3':'审阅材料可定位具体实现或练习','—':'当前审阅未定位','?':'细目不足以判断'}}
(OUT/'coverage.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),'utf8')
buf=io.StringIO();w=csv.writer(buf,lineterminator='\n');w.writerow(['course_id','course','stage','topic_id','topic','level','review','locator','official_source'])
for c in COURSES:
 for t in TOPICS:
  v=c['cells'][t['id']];w.writerow([c['id'],c['title'],t['stage'],t['id'],t['title'],v['level'],v.get('review',''),v.get('locator',v.get('reason','')),c['source']])
(OUT/'coverage.csv').write_text(buf.getvalue(),encoding='utf-8-sig')
timeline=['# 共同知识主线\n','这是一条建议学习顺序，不是发展史或日历，也不是必须学完的统一考纲。每个节点的子主题可能只被部分覆盖；应用与研究分支可按目标选择。\n']
for s in STAGES:
 timeline+=['## '+s+'\n','| 编号 | 知识点 | 学会后应能解释或验证 |\n|---|---|---|']
 timeline += [f"| {t['id']} | {t['title']} | {t['description']} |" for t in TOPICS if t['stage']==s]
timeline += ['\n## 归并规则\n','- ReAct 与 loop 放在同一节点；分流、Router 与 routing 同一节点。\n- 工具调用与 MCP 分开；多 Agent 与 A2A 分开；长期记忆与 checkpoint 分开。\n- 旅行、客服、邮件等归入综合应用，不因业务名称不同重复增加覆盖数量。\n- 框架名、教材形式、证书、价格和课时不计入内容覆盖点。框架选型本身、低代码和特殊开发方式可以作为知识点。\n- 研究训练与游戏具身是分支；应用开发覆盖率默认不应被这些方向拉低。\n- 粗粒度节点不是所有子主题的全覆盖；精确内容由单元格证据和后续笔记补充。']
(OUT/'KNOWLEDGE_TIMELINE.md').write_text('\n'.join(timeline),'utf8')
matrix=['# 所有课程的知识覆盖与深度\n','[方法](METHOD.md) · [共同主线](KNOWLEDGE_TIMELINE.md) · [材料形式](MATERIALS.md) · [逐项证据](EVIDENCE.md)\n','**1 = 目录列出，2 = 有正文解释，3 = 已审阅到具体实现/练习，— = 当前未定位，? = 细目不足。** 3不代表代码已跑通。未定位不等于未教。\n']
for stage in STAGES:
 topics=[t for t in TOPICS if t['stage']==stage];matrix+=['## '+stage+'\n','\n'.join(f"- **{t['id']}**：{t['title']}" for t in topics)+'\n','| 课程 | '+' | '.join(t['id'] for t in topics)+' |','|---|'+'---|'*len(topics)]
 for c in COURSES:matrix.append('| ['+c['title']+'](../courses/'+c['id']+'/README.md) | '+' | '.join(str(c['cells'][t['id']]['level']) for t in topics)+' |')
matrix+=['\n## 已确认主题数量（证据下限）\n','这些数字只描述本知识表中的已确认节点，不是教学质量排行；1/2/3为最高确认等级且互斥。“有目录”与“有正文”采集深度不同，不能据此宣称目录课更浅。\n','| 课程 | 目录级1 | 解释级2 | 实作材料级3 | 细目不足? |','|---|---:|---:|---:|---:|']
for c in COURSES:matrix.append(f"| {c['title']} | {c['counts']['1']} | {c['counts']['2']} | {c['counts']['3']} | {c['counts']['?']} |")
(OUT/'COVERAGE_MATRIX.md').write_text('\n'.join(matrix),'utf8')
ev=['# 逐课程、逐知识点证据\n','此表定位到本仓库已有研究记录与官方入口。摘录是研究者的归纳，不冒充官方逐字引文。层级为当前证据支持的下限；需与原课核对后再升级。\n']
for c in COURSES:
 ev+=['## '+c['title']+'\n','[官网]('+c['source']+') · [课程笔记](../courses/'+c['id']+'/README.md)\n','| 点 | 等级 | 研究记录中的定位依据 |','|---|---|---|']
 for t in TOPICS:
  v=c['cells'][t['id']]
  if isinstance(v['level'],int):ev.append(f"| {t['id']} {t['title']} | {v['level']} | [记录](../{v['review']})：{v['locator'].replace('|',' / ').replace(chr(10),' ')} |")
(OUT/'EVIDENCE.md').write_text('\n'.join(ev),'utf8')
print('Built',len(TOPICS),'topics ×',len(COURSES),'courses;',len(LEDGER),'positive evidence entries')
