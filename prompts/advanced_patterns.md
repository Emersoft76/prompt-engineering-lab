# 🧠 Padrões Avançados de Prompts

Este documento apresenta **padrões de engenharia de prompts** mais avançados, úteis para controlar melhor o comportamento de modelos LLM como o GPT-4 e GPT-3.5, aumentando a previsibilidade, a utilidade e a segurança das respostas.

---

## 🧩 1. Cadeia de Pensamento (Chain of Thought)

**🟢 Descrição:** Incentiva o modelo a mostrar seu raciocínio passo a passo.

```text
Pergunta: João tem 5 maçãs. Ele dá 2 para Maria e compra mais 3. Quantas ele tem agora?

Responda passo a passo.
```
---
✅ Resultado esperado:
O modelo primeiro explica a operação (5 - 2 + 3), depois dá a resposta: 6.

---

## 🧩 2. Role Prompting (Identidade e Persona)

🟢 Descrição: Define uma persona ou papel para o modelo antes da tarefa.
```
Aja como um professor de matemática experiente. Explique a seguinte equação para alunos do ensino médio:
x² - 4x + 4 = 0
```
✅ Aplicações: Suporte técnico, coaching, personagens, tradução especializada etc.

---

## 🧩 3. Prompt de Crítica e Autoavaliação

🟢 Descrição: Peça ao modelo para revisar ou melhorar sua própria resposta.
```
Responda à pergunta a seguir, e depois critique sua própria resposta para encontrar possíveis melhorias:

"Por que a água ferve a 100 °C ao nível do mar?"
```
---

## 🧩 4. Prompt por Exemplo (Few-shot)
```
🟢 Descrição: Fornece exemplos para guiar o modelo.

Corrija a gramática das seguintes frases:

Entrada: "Eu vai no mercado ontem."
Saída: "Eu fui ao mercado ontem."

Entrada: "Ela estão felizes."
Saída:
```
✅ Resultado esperado:
"Elas estão felizes."

---

## 🧩 5. Prompt com Restrições de Formato

🟢 Descrição: Solicita respostas em formato específico (JSON, tabela, Markdown etc.)
```
Converta a seguinte informação para JSON:

Nome: Maria  
Idade: 29  
Cidade: Lisboa
```
✅ Resultado esperado:
```
{
  "nome": "Maria",
  "idade": 29,
  "cidade": "Lisboa"
}
```
---

## 🧩 6. Prompt Iterativo / Reflexivo

🟢 Descrição: Solicita múltiplas abordagens ou reavaliação de uma ideia.
```
Forneça 3 abordagens diferentes para resolver o problema abaixo. Depois, diga qual delas parece mais eficaz e por quê.

Problema: Reduzir o tempo de resposta de um chatbot em um site.
```
---

## 🧩 7. Prompt com Contexto Técnico

🟢 Descrição: Injeta informações específicas do domínio no prompt.
```
Considere o seguinte código em Python:

def soma(a, b):
    return a + b

Explique como funciona e a complexidade da função.
```
✅ Resultado esperado:
Resposta técnica clara, mencionando O(1) como complexidade.

---

## ✅ Boas Práticas

| Estratégia                  | Benefício                                                         |
|-----------------------------|-------------------------------------------------------------------|
| **Especificidade**          | Reduz ambiguidade e gera respostas mais direcionadas              |
| **Definir persona**         | Ajusta tom, linguagem e abordagem da resposta                     |
| **Exemplos contextuais**    | Ajuda o modelo a entender o formato esperado (few-shot learning)  |
| **Formato exigido**         | Facilita parsing (JSON, Markdown, tabela, etc.)                   |
| **Raciocínio passo a passo**| Melhora coerência e aumenta transparência no processo de resposta |
| **Autoavaliação/reflexão**  | Permite correções, melhorias e resultados mais confiáveis         |
| **Iteratividade**           | Estimula múltiplas abordagens para um mesmo problema              |

---

📘 Referências

* OpenAI Cookbook

* Prompt Engineering Guide

* Papers: "Chain-of-Thought Prompting Elicits Reasoning in LLMs", "Self-Refine: Iterative Refinement with Self-Feedback"
