# DeepLearning.AI 之外的 Agent 课程（官方目录审阅）

审阅日期：2026-10-03。仅核对官方目录/活动页；未完成课程，也未运行全部代码。共四组。

## 1. Google × Kaggle：5-Day AI Agents Intensive（2025）

- **形态/目录：**五日在线密集课，直播于2025-11-10至14举行，全部课程现整理为Kaggle自学指南。五天依次为Agent入门、工具与MCP、会话和记忆、可观测性与评测、A2A及生产部署。
- **代码/项目：**Gemini+ADK单/多Agent；Python工具、MCP与人工批准；跨会话记忆；观测及评测；A2A。最终项目赛道可交Kaggle Notebook、Colab或GitHub代码，2025届截止期已过。
- **前提/获取：**Kaggle账号需手机验证；codelab需Google AI Studio API key。Kaggle指南仍可自学；指南未列当前价格。
- **链接：**[2025自学指南](https://www.kaggle.com/learn-guide/5-day-agents)｜[Google/Kaggle课程回顾](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap/)｜[capstone](https://www.kaggle.com/competitions/agents-intensive-capstone-project/overview)
- **版本区别：**2026年6月的 [Vibe Coding 更新版](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding) 也已转成自学指南，改为Agent与Vibe Coding、工具互操作、Agent Skills、安全/评测、规格驱动部署；不应与2025目录混作同一版。

## 2. NVIDIA DLI：Building RAG Agents with LLMs

- **形态/目录：**8小时讲师带课。模块从LLM推理接口、LangChain/LCEL与Gradio/LangServe，进入对话状态/slot filling、长文切分与摘要、embedding与输入护栏、向量库RAG，最后做LLM-as-a-Judge评测；成果目标是回答研究论文集问题的RAG Agent。
- **代码/前提：**Python、LangChain、FAISS、Gradio、LangServe、FastAPI；要求中级Python（含OOP）和入门深度学习，PyTorch经验建议具备。讲师版为学员提供云端GPU工作站，开课需DLI和NGC账号。
- **费用/状态：**[当前讲师课页](https://www.nvidia.com/en-au/training/instructor-led-workshops/building-rag-agents-with-llms/)写联系NVIDIA询价；[学习路径](https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/)列自学版$90/8小时且可获证书；旧版[课程目录PDF](https://cdn.dli.learn.nvidia.com/web-asset/nvidia-learning-training%20course-catalog.pdf)曾列自学版免费。记录时需注明来源版本，报名按当时页面为准。

## 3. NVIDIA DLI：Building Agentic AI Applications with LLMs

- **形态/可核实内容：**官方[学习路径](https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/)和[证书备考路径](https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/)均列出课程；自学课程简介称用LangGraph和NVIDIA NIM构建长程推理、内容管理和实时操作型Agent。
- **目录边界：**当前公开的课程详情页只有导航、未呈现课程正文和逐节目录，未能核实代码/项目与学员前提。因此这项只能确认课程存在和简介，不能算完整目录评审。
- **费用/状态：**同一官方学习路径列讲师版$500/8小时，自学版在证书路径列$90/8小时；[NVIDIA自学列表](https://sp-experience.courses.nvidia.com/)却显示FREE。页面间价格冲突，报名时核对结账页。

## 4. IBM：Agentic AI in Practice

- **形态/目录：**IBM Training连续路径，共1门课程、9个教程、四段：Agent基础；CrewAI/LangChain；自定义工具、ReAct与LangGraph工作流；领域型多Agent与RAG。
- **应用项目：**目录列出CrewAI+Gradio多Agent、LangChain工具调用数学助手、自建工具、ReAct Agent、LangGraph模式、医疗AG2/AutoGen、PydanticAI客服Agent、LangGraph+Docling Agentic RAG。
- **获取/局限：**IBM标为Express Learning / No cost；路径页没列统一先修条件，也未展示每个教程完整运行环境或代码仓库。资产时长显示30至180 hours，页面未解释单位，不宜直接当实际学习耗时。
- **链接：**[IBM Agentic AI in Practice](https://www.ibm.com/training/learning-path/agentic-ai-in-practice-1058)

## 选材提示

Kaggle材料链和历史状态最清楚；NVIDIA RAG页的模块与实践信息最具体；NVIDIA Agentic课的公开细目不足，应只作“存在此课”的补充；IBM适合展示多框架应用路径，教程代码与实际投入时长仍需逐项核实。
