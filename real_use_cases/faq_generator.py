# Gera FAQs com base em um conteúdo fornecido

import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_faq(texto_fonte):
    prompt = f"""
Gere uma lista de perguntas frequentes (FAQs) com base no seguinte conteúdo:

\"\"\"{texto_fonte}\"\"\"
    
Retorne em formato:
Q: Pergunta
A: Resposta
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    texto = input("Cole o conteúdo base: ")
    faqs = generate_faq(texto)
    print("\n--- FAQs Gerados ---\n")
    print(faqs)
