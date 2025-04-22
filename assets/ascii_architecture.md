# 🧠 Arquitetura do Projeto – Prompt Engineering Lab (ASCII)

Este diagrama representa a estrutura geral do laboratório, conectando os principais componentes do fluxo com IA generativa.
```
                    +------------------------------+
                    |    Usuário / Interface Web   |
                    |      (Streamlit App)         |
                    +--------------+---------------+
                                   |
                                   v
                    +------------------------------+
                    |         Prompt Design         |
                    |    (manual ou gerado por UI)  |
                    +--------------+---------------+
                                   |
                                   v
                    +------------------------------+
                    |     API OpenAI (GPT 3.5/4)    |
                    +--------------+---------------+
                                   |
                                   v
  +-------------------+     +-----------------+     +--------------------+
  | LangChain Agents  | --> | Prompt Templates| --> | Memory (Buffers)   |
  +-------------------+     +-----------------+     +--------------------+
                                   |
                                   v
                    +------------------------------+
                    |      Resposta da LLM         |
                    +--------------+---------------+
                                   |
                                   v
    +--------------+    +----------------+    +-----------------+
    | Scripts .py  |    | PDF Summarizer |    | Data Cleaner    |
    | Automations  |    | Email Writer   |    | Real Examples   |
    +--------------+    +----------------+    +-----------------+
```
---

