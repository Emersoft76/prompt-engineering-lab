# Gera funções Python comentadas a partir de uma descrição

import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_codigo(descricao):
    prompt = f"""
Escreva uma função Python bem estruturada e comentada que faça o seguinte:

{descricao}

A função deve conter comentários explicando cada etapa.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    tarefa = input("Descreva a função que deseja gerar: ")
    codigo = gerar_codigo(tarefa)
    print("\n--- Função Gerada ---\n")
    print(codigo)
