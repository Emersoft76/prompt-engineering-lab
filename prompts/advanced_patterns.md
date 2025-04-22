# 🧠 Padrões Avançados de Prompts

Este documento apresenta **padrões de engenharia de prompts** mais avançados, úteis para controlar melhor o comportamento de modelos LLM como o GPT-4 e GPT-3.5, aumentando a previsibilidade, a utilidade e a segurança das respostas.

---

## 🧩 1. Cadeia de Pensamento (Chain of Thought)

**🟢 Descrição:** Incentiva o modelo a mostrar seu raciocínio passo a passo.

```text
Pergunta: João tem 5 maçãs. Ele dá 2 para Maria e compra mais 3. Quantas ele tem agora?

Responda passo a passo.
---
✅ Resultado esperado:
O modelo primeiro explica a operação (5 - 2 + 3), depois dá a resposta: 6.

---

## 🧩 2. Role Prompting (Identidade e Persona)
🟢 Descrição: Define uma persona ou papel para o modelo antes da tarefa.
---
Aja como um professor de matemática experiente. Explique a seguinte equação para alunos do ensino médio:
x² - 4x + 4 = 0

---
