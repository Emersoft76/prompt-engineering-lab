# 🛠️ Instalação de Ferramentas – Prompt Engineering Lab

Este guia ajuda a configurar seu ambiente local, tanto em **Windows** quanto **Linux**, para executar os scripts e dashboards incluídos neste repositório.

---

## ✅ Ferramentas Necessárias

| Ferramenta     | Função                             | Link Oficial                           |
|----------------|-------------------------------------|----------------------------------------|
| Python 3.10+   | Linguagem para scripts e IA         | [python.org](https://www.python.org)   |
| pip            | Gerenciador de pacotes Python       | Incluso no Python                      |
| OpenAI API Key | Acesso à IA generativa              | [platform.openai.com](https://platform.openai.com) |
| Streamlit      | Interface web para scripts Python   | [streamlit.io](https://streamlit.io)   |
| LangChain      | Framework de LLMs com integração    | [langchain.com](https://www.langchain.com) |
| VS Code        | Editor de código recomendado        | [code.visualstudio.com](https://code.visualstudio.com) |

---

## 🔧 Windows (via terminal PowerShell)

```bash
# Instalar bibliotecas básicas
pip install openai streamlit langchain python-dotenv requests
```
---

## 🐧 Linux (Ubuntu)
```
sudo apt update
sudo apt install python3-pip -y
pip3 install openai streamlit langchain python-dotenv requests
```
---

## 🔑 Criar variável de ambiente (OpenAI Key)
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
Ou configure via terminal:
```
export OPENAI_API_KEY="sua-chave
```
---
