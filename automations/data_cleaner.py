# Gera scripts de limpeza para datasets com base na descrição

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_cleaning_steps(dataset_description):
    prompt = f"""
Sugira etapas em Python para limpar o seguinte dataset:
{dataset_description}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    desc = input("Descreva seu dataset (ex: colunas, problemas...): ")
    steps = suggest_cleaning_steps(desc)
    print("\nSugestão de limpeza:\n")
    print(steps)
