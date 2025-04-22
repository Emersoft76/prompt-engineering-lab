# 🎯 Fundamentos da Engenharia de Prompts

A **engenharia de prompts** é a prática de formular instruções claras, específicas e eficientes para modelos de linguagem (LLMs), com o objetivo de obter respostas mais úteis, precisas e controláveis.

---

## 🧠 O que é um Prompt?

Um prompt é o **texto de entrada** enviado ao modelo de linguagem. Ele pode conter instruções, contexto, exemplos ou perguntas.

```text
Traduza o seguinte texto para o inglês: "A IA está mudando o mundo."
```
---

## ✅ Boas Práticas Básicas

| Prática                      | Descrição                                                        |
|------------------------------|------------------------------------------------------------------|
| **Seja específico**          | Prompts vagos geram respostas genéricas ou imprecisas            |
| **Defina o papel do modelo** | Ex: "Aja como um advogado especializado em contratos"            |
| **Peça o formato desejado**  | Solicite JSON, tabela Markdown, lista, etc.                      |
| **Forneça contexto**         | Inclua detalhes do domínio ou situação específica                |
| **Use exemplos (few-shot)**  | Adicione exemplos de entrada e saída esperada                    |

---

## 🧩 Tipos de Prompt

| Tipo de Prompt       | Exemplo                                                                 |
|----------------------|-------------------------------------------------------------------------|
| **Zero-shot**        | "Traduza para francês: Hello."                                          |
| **One-shot**         | Um exemplo antes da pergunta principal                                  |
| **Few-shot**         | Múltiplos exemplos guiam o modelo para o padrão desejado                |
| **Chain-of-thought** | "Explique passo a passo como resolver 2x + 4 = 10."                     |
| **Role prompting**   | "Aja como um especialista em segurança da informação."                  |

---

## 🛠️ Recomendações Técnicas

* Use tokens delimitadores como """ ou ### para separar blocos

* Limite o tamanho do prompt para manter o desempenho (ver max_tokens)

* Valide a resposta: verifique se o modelo seguiu o formato solicitado

---

## 📘 Dica

    Pequenas mudanças no prompt podem gerar grandes diferenças na resposta.
    Teste, ajuste e compare versões com objetivos claros.

Para exemplos reais, veja: real_world_cases.md

---
