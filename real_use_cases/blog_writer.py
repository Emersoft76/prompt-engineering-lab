# Gera um artigo ou post de blog com base em um título ou tema

import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_artigo(titulo):
    prompt = f"""
Crie um artigo de blog com título: "{titulo}"

O artigo deve conter introdução, desenvolvimento (em até 3 tópicos) e conclusão, com tom profissional e linguagem acessível.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=900
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    tema = input("Tema ou título do artigo: ")
    artigo = gerar_artigo(tema)
    print("\n--- Artigo Gerado ---\n")
    print(artigo)
