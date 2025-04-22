# 💻 Compatibilidade de Sistemas e Configuração de Ambiente

Este projeto foi desenvolvido para funcionar em **ambientes Windows, Linux (Ubuntu)** e **MacOS**.  
Abaixo, você encontra orientações específicas para cada sistema e como configurar o ambiente corretamente.

---

## ✅ Compatibilidade Geral
```
| Ferramenta / Tecnologia | Windows | Linux (Ubuntu/Debian) | MacOS |
|-------------------------|---------|-----------------------|-------|
| Python 3.10+            | ✅      | ✅                   | ✅   |
| pip                     | ✅      | ✅                   | ✅   |
| OpenAI API Key          | ✅      | ✅                   | ✅   |
| LangChain               | ✅      | ✅                   | ✅   |
| Streamlit               | ✅      | ✅                   | ✅   |
| Git                     | ✅      | ✅                   | ✅   |
| VS Code                 | ✅      | ✅                   | ✅   |
```
---

## ⚙️ Instruções por sistema

### 🪟 Windows (via PowerShell ou CMD)

1. Instale o Python pelo site oficial:  
   → [https://www.python.org](https://www.python.org)

2. Instale as bibliotecas:
```
pip install openai streamlit langchain python-dotenv requests
```
---
3. Crie o arquivo .env na raiz do projeto:
```---
OPENAI_API_KEY=sk-sua-chave-aqui
```
---
4. Para executar scripts:
```
python automations/email_writer.py
streamlit run streamlit_app/app.py
```
---

🐧 Linux (Ubuntu / Debian)
```
sudo apt update
sudo apt install python3-pip -y

pip3 install openai streamlit langchain python-dotenv requests
```
---
Crie o arquivo .env com sua chave:
```
echo "OPENAI_API_KEY=sk-sua-chave-aqui" > .env
```
Execute com:
```
python3 automations/email_writer.py
streamlit run streamlit_app/app.py
```
---

🍏 MacOS (via Homebrew)
```
brew install python
pip3 install openai streamlit langchain python-dotenv requests
```
---

## 📁 Estrutura recomendada de arquivos
```
/prompt-engineering-lab/
├── .env                    ← Sua chave API aqui
├── automations/
│   └── email_writer.py
└── streamlit_app/
    └── app.
```
---

## 🧪 Testando o ambiente

Você pode testar se tudo está funcionando corretamente com:
```
python automations/email_writer.py
```
Se o script retornar um e-mail gerado pela IA, sua chave e bibliotecas estão funcionando!

---

## 📘 Dica para o .env não ser rastreado pelo Git

Crie (ou edite) um arquivo .gitignore:
```
.env
__pycache__/
```
---
