**Resume PDFs com OpenAI**

import openai
import os
from dotenv import load_dotenv
import PyPDF2

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Resuma este texto:\n{text}"}],
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    pdf_path = input("Caminho do PDF: ")
    content = extract_text_from_pdf(pdf_path)
    resumo = summarize_text(content)
    print("\nResumo gerado:\n")
    print(resumo)
