<!-- BANNER -->
<h1 align="center">🧠 Prompt Engineering Lab</h1>
<p align="center">Práticas modernas em IA Generativa com OpenAI, Python, LangChain e Automação Inteligente.</p>
<p align="center"><strong>Prompt Design | LLM Automation | API Integration | Streamlit + LangChain</strong></p>

---

<!-- BADGES -->
<p align="center">
  <a href="https://platform.openai.com/"><img src="https://img.shields.io/badge/OpenAI-API-blue?style=flat-square&logo=openai" /></a>
  <a href="https://python.org/"><img src="https://img.shields.io/badge/Python-3.10-yellow?style=flat-square&logo=python" /></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat-square&logo=streamlit" /></a>
  <a href="https://www.langchain.com/"><img src="https://img.shields.io/badge/LangChain-LLM%20Framework-orange?style=flat-square" /></a>
  <a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub-Actions-2088FF?style=flat-square&logo=githubactions" /></a>
</p>

---

## 🧭 Sobre o projeto / About this project

**PT-BR:**  
Este laboratório foi criado para desenvolver habilidades práticas em **engenharia de prompts**, uso de **IA generativa via API** e **automação com Python**. Inclui exemplos reais com OpenAI, integração com documentos, automações com LangChain e interface web com Streamlit.

**EN:**  
This lab is designed to build and validate hands-on skills in **prompt engineering**, **generative AI via API**, and **Python-based automation**. Includes real examples using OpenAI, document chains, LangChain workflows and Streamlit UI.

---

## 📚 Índice Geral

### 🧠 Conceitos e Configurações Iniciais

- [`📄 introduction.md`](docs/introduction.md)
- [`🧪 prompt_design.md`](docs/prompt_design.md)
- [`🔐 openai_api_setup.md`](docs/openai_api_setup.md)
- [`📦 tools_installation.md`](docs/tools_installation.md)
- [`🧩 system_compatibility.md`](docs/system_compatibility.md)

### 🤖 Casos de Uso Reais com IA Generativa

- [`faq_generator.py`](real_use_cases/faq_generator.py)
- [`sentiment_analyzer.py`](real_use_cases/sentiment_analyzer.py)
- [`code_generator.py`](real_use_cases/code_generator.py)
- [`interview_bot.py`](real_use_cases/interview_bot.py)
- [`text_to_json.py`](real_use_cases/text_to_json.py)
- [`blog_writer.py`](real_use_cases/blog_writer.py)
- [`Interface Streamlit`](real_use_cases/app.py)

### 🔗 LangChain & IA com Memória

- [`chatbot_streamlit.py`](langchain/chatbot_streamlit.py)
- [`memory_examples.py`](langchain/memory_examples.py)

### 🎛️ Prompt Playground (UI Visual)

- [`app.py`](streamlit_app/app.py)
- [`requirements.txt`](streamlit_app/requirements.txt)

### 🧩 Diagramas e Visualizações

- [`ascii_architecture.md`](assets/ascii_architecture.md)

### ⚙️ Workflows e Integração

- [`.github/workflows/ai_pipeline.yml`](.github/workflows/ai_pipeline.yml)

---

## 📁 Estrutura do Projeto

```bash
/prompt-engineering-lab/
├── README.md
├── .env.example
├── requirements.txt
├── docs/
│   ├── introduction.md
│   ├── prompt_design.md
│   ├── openai_api_setup.md
│   ├── tools_installation.md
│   └── system_compatibility.md
├── prompts/
│   ├── basic_examples.md
│   ├── advanced_patterns.md
│   └── real_world_cases.md
├── real_use_cases/
│   ├── faq_generator.py
│   ├── sentiment_analyzer.py
│   ├── code_generator.py
│   ├── interview_bot.py
│   ├── text_to_json.py
│   ├── blog_writer.py
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── langchain/
│   ├── chatbot_streamlit.py
│   ├── memory_examples.py
│   └── README.md
├── streamlit_app/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── assets/
│   └── ascii_architecture.md
└── .github/
    └── workflows/
        └── ai_pipeline.yml
```
---

## 💻 Compatibilidade de Sistemas

| Ferramenta / Tecnologia | Windows | Linux (Ubuntu/Debian) | MacOS |
|--------------------------|:------:|:----------------------:|:------:|
| Python 3.10+             |   ✅   |          ✅           |  ✅   |
| pip                      |   ✅   |          ✅           |  ✅   |
| OpenAI API Key           |   ✅   |          ✅           |  ✅   |
| LangChain                |   ✅   |          ✅           |  ✅   |
| Streamlit                |   ✅   |          ✅           |  ✅   |
| Git                      |   ✅   |          ✅           |  ✅   |
| VS Code                  |   ✅   |          ✅           |  ✅   |

---

## 📘 Próximos módulos

* ✅ Vetorização e embeddings com FAISS

* ✅ Agentes com ferramentas externas (busca, código)

* ✅ Chat com documentos PDF / TXT

* ✅ Deploy em nuvem (Streamlit Cloud / HuggingFace Spaces)
---


<!-- FOOTER --> <p align="center"> <strong>“From structured prompts to intelligent automation, connectivity is the key.”</strong><br> Desenvolvido por <a href="https://github.com/Emersoft76"><strong>@Emersoft76</strong></a><br> <em>Formado em Gerenciamento de Redes de Computadores – UNIP (Brasília/Brasil), 2009</em><br> <em>Soluções modernas com base sólida em redes, cloud, automação e inteligência artificial.</em> </p>
