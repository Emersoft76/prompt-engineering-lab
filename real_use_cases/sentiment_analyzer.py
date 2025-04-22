# Classifica sentimento com base em texto

import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analisar_sentimento(frase):
    prompt = f"Classifique o sentimento da seguinte frase como Positivo, Negativo ou Neutro:\n\n\"{frase}\""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=60
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    texto = input("Digite a frase a ser analisada: ")
    sentimento = analisar_sentimento(texto)
    print("\nSentimento identificado:", sentimento)
