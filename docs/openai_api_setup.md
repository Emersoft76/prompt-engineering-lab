### ✅ `openai_api_setup.md` — Como Configurar a API da OpenAI

# 🔐 Como Configurar a API da OpenAI

Este guia mostra como criar uma conta na OpenAI, gerar uma API Key e configurá-la para uso local em seus projetos com Python.

---

## 🪪 1. Criar Conta

Acesse o site: https://platform.openai.com/signup  
Crie sua conta com e-mail, Google ou GitHub.

---

## 🔑 2. Gerar API Key

1. Acesse: https://platform.openai.com/account/api-keys  
2. Clique em **Create new secret key**
3. Copie e salve sua chave em um local seguro (não será exibida novamente)

---

## 🔒 3. Armazenar em `.env`

Crie um arquivo `.env` no diretório raiz do seu projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-xxxxxxx...
```
⚠️ Nunca compartilhe sua chave pública ou em repositórios abertos.

---

## 💻 4. Acessar via Python

Instale as bibliotecas:
```
pip install openai python-dotenv
```
Código básico para usar sua chave via .env:
```
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```
---

## 🧪 Teste rápido
```
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Olá, o que você sabe sobre IA?"}]
)
print(response.choices[0].message.content)
```
---
