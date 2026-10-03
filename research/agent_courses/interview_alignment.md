# 入门教材能否回答真实 Agent 面经？

对照材料：[原面经综述](../agent_interview_review.md)、[国内扩展目录](../interview_catalog_china_expanded.md)、[海外扩展目录](../interview_catalog_overseas_expanded.md)。这里做的是问题到教材章节的映射，不是面经频率统计，也不代表企业统一考纲。课程版本以各provider/evidence为准。

## 覆盖等级怎样读

- **直接入口**：正文明确解释概念并给相近代码或例子。
- **部分入口**：学过相关构件，但仍需自己组织系统设计或补实验。
- **额外准备**：现有教材不足以支持完整回答，需后端/算法/项目证据。

覆盖不是掌握。面试官问“你为什么这样设计”，教材只能给方法，回答还需要你自己实现的约束与结果。

中文主线可补查Datawhale：第04/07章是手写模式与工具，第06章含LangGraph，第08/09章是Memory/RAG与上下文，第10章协议，第12章评测，第13/14章提供旅行和研究项目；Skill/harness还见Extra补充文章。主教材与社区Extra应分开标识，详见[Datawhale目录](providers/datawhale/curriculum.md)。

## 原牛客帖子逐问映射

原帖：[小红书 Agentic 全栈研发练习生一面](https://www.nowcoder.com/feed/main/detail/e5e9311a623940eead6ec98c65e7f9e8?sourceSSR=subject)。以下为问题主题概括，非完整逐字转载。

| 问题主题 | 最贴近的已获取教材入口 | 教材能帮助组织的回答 | 仍需你补的证据 |
|---|---|---|---|
| Agent在业务里解决什么，客服与开发助手怎样分开 | HF Unit1 agency光谱；微软01/03；Anthropic workflows-vs-agents | 目标、数据、工具、自主程度、代价与错误后果。 | 真实用户需求、没有Agent时的基线、效果。 |
| 写操作边界 | 微软15/16/18；Anthropic SDK permissions/user-input；OpenAI approvals | 读写工具区分、身份资源范围、批准、执行点检查、审计。 | 越权样本、拒绝日志、重复动作与撤销策略。 |
| harness负责什么 | Anthropic长任务harness文章、agent-loop；微软14/16；HF dummy loop | 模型外部的上下文/工具/状态/预算/恢复设施。 | 自己项目的层级图和失败路径；不能只背组件表。 |
| 重构编排层 | OpenAI orchestration；LangGraph图式编排；微软14 | 固定workflow、handoff、agent-as-tool与自主loop的控制权区别。 | 原实现的问题、重构后指标、增加复杂度是否值得。 |
| query是否模糊、怎么意图分流 | Anthropic routing-workflows/agents-and-tools；HF邮件分类；微软15/16 | 先分类、再检查参数；缺信息追问；未知意图回退。 | 多意图、置信度、路由错例和规则/模型比较。 |
| Skill与Tool差异，何时拿Skill | Anthropic Platform101 Skills、SDK skills、工程文章 | 程序能力与任务方法/资源包装区别；按需加载。 | 实际选择错误、版本管理、权限独立于Skill说明。 |
| 模型前后是否一致 | 各课模型配置、HF chat templates；OpenAI models | 区分模型名、参数、提示、工具版本与依赖。 | 同任务多次运行、跨模型回归；temperature=0不是绝对确定性证明。 |
| 每日调用量如何统计 | OpenAI tracing；HF observability；微软10/16 | 区分用户任务、模型调用、工具调用、tokens、重试。 | 实际trace聚合与计费记录。 |
| 用户变多、十万级日请求怎么扩展 | 微软16直接入口；其他主入门课仅部分 | 无状态服务、外部状态、限流、队列、cache、bounded concurrency与降级。 | 峰值、任务耗时、每任务调用量、数据库写模式、负载/故障实验。 |
| 为什么SQLite | OpenAI running-agents的SQLiteSession；微软04的SQLite工具 | 课程展示SQLite用途和接口。 | 数据规模、读写比例、部署拓扑、锁与事务、备份、迁移；示范接口不能替代选型。 |
| LangGraph节点与边 | HF Unit2 LangGraph；LangChain Academy | State/Node/Edge、条件路由、持久化与中断等框架构件。 | 状态更新、终止条件、重复副作用、错误恢复。 |
| 自研还是用框架 | HF三框架比较；OpenAI SDK与直接API入口；微软02 | 控制需求、生态、调试、维护、托管与自运行区别。 | 在你项目中具体节省或损失什么；不能只列流行库名。 |
| Java/HashMap/MySQL B+树与索引 | 这些Agent材料不是合适主教材 | Agent课程能提供数据库使用语境。 | 语言、数据结构、数据库原理与编码练习需另学。 |

## 从章节变成可回答的问题

### 工具调用

初级解释：“模型产生schema约束的参数，执行器调用函数，再回填结果。”

项目追问：“函数超时但退款已发生怎么办？”必须补执行状态、幂等、对账或补偿。多数教程示例只到第一句；读到schema不能声称覆盖全部工具工程。

### 记忆和状态

初级解释：“Session保存会话，State保存执行中数据。”

项目追问：“两个租户共享进程时如何隔离？摘要是否丢失约束？”需要数据访问边界、状态持久化、回放与压缩验证。课程的memory例子是入口，不是完整答案。

### RAG

初级解释：“检索资料后生成答案。”

项目追问：“召回不到编号、召回过期资料、跨权限检出怎么办？”需要关键词/向量对比、时间过滤、ACL与引用核验。没有测试集的框架调用不等于检索系统设计。

### 评测

初级解释：“让judge对答案评分。”

项目追问：“结果正确但工具越权如何算？评分器错判怎么办？”要分最终结果、轨迹约束、成本/时延和人工校准。Anthropic evals、HF观测与评测、微软10更适合继续阅读。

### 规模

初级解释：“增加副本，做缓存。”

项目追问：“瓶颈是模型quota、长任务在途数还是数据库写锁？”要先测或说明假设，再选择扩容。日均量无法独自回答峰值容量。

## 不同岗位的阅读权重

| 岗位方向 | 核心教材入口 | 配套准备 |
|---|---|---|
| Agent应用/全栈毕业生 | 一门中文或HF基础课 + 一个小项目；再补routing、批准与eval | Web/API、SQL、鉴权、测试和个人贡献。 |
| Coding Agent/Harness | Anthropic loop/权限/长任务/Skills + 图式状态与恢复 | 沙箱、文件操作、checkpoint、预算、失败复盘。 |
| 平台/基础设施 | 微软16/18 + 各SDK运行/观测材料 | 后端与分布式基础、租户隔离、队列、容量及SLO。 |
| Agent算法/研究 | Berkeley研究讲座、相关论文及评测方法 | 数据、训练/优化、基线与消融；应用SDK课不能取代。 |

岗位分类来自本地面经研究的分析框架，不是所有公司的正式职级分类。海外有经验岗位的系统设计问题不能直接转换为国内毕业生统一要求。

## 面试准备的小型交付物

选一个项目，准备：目标与基线、数据流、工具契约、权限策略、两条成功轨迹、三条失败轨迹、一个评测集、实际成本记录、一个选型权衡。可以规模很小，但解释必须对应真实代码。具体练习见[worked_examples](worked_examples.md)。
