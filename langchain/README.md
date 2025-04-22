# 🔗 LangChain – Integração com LLMs e Memória

Esta pasta contém exemplos usando a biblioteca **LangChain**, uma poderosa ferramenta para conectar LLMs com memória, ferramentas externas, APIs e fluxos complexos.

---

## 📦 Requisitos

```
pip install langchain openai python-dotenv streamlit
```
---

## 📘 Exemplos

| Arquivo                | Descrição                                                             |
|------------------------|-----------------------------------------------------------------------|
| `chatbot_streamlit.py` | Mini chatbot com memória e interface web via Streamlit                |
| `memory_examples.py`   | Execução local com buffer de memória para rastrear o histórico        |

---

## 🚀 Executar chatbot (interface web)
```
streamlit run chatbot_streamlit.py
```
Acesse: http://localhost:8501

---

## 🧪 Executar teste no terminal
```
python memory_examples.py
```
---

## 💡 Dica

Experimente ajustar o temperature, usar modelos maiores (GPT-4), e criar fluxos com agentes e ferramentas.

---
