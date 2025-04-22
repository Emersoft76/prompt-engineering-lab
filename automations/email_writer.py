**Script simples para gerar e-mails automáticos via OpenAI**

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_email(subject, tone="formal"):
    prompt = f"Escreva um e-mail com o seguinte assunto: '{subject}', em um tom {tone}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um redator de e-mails profissional."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    assunto = input("Digite o assunto do e-mail: ")
    estilo = input("Tom (formal, casual, criativo): ")
    resultado = generate_email(assunto, estilo)
    print("\n--- E-mail gerado ---\n")
    print(resultado)
