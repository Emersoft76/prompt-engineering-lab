# Transforma um texto livre em um objeto JSON estruturado

import openai, os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def texto_para_json(texto):
    prompt = f"""
Converta o seguinte texto em um objeto JSON estruturado, com chaves claras e bem definidas:

\"\"\"{texto}\"\"\"
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=800
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    entrada = input("Cole o texto a ser convertido: ")
    json_gerado = texto_para_json(entrada)
    print("\n--- JSON Estruturado ---\n")
    print(json_gerado)
