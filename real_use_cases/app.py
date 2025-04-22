# Interface única para execução dos 6 casos de uso reais

import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🤖 IA: Casos Reais", layout="centered")
st.title("🤖 IA Generativa – Casos de Uso Reais")
st.markdown("Escolha um caso de uso no menu lateral e insira os dados necessários para testar os recursos.")

# Menu lateral
case = st.sidebar.selectbox("🧭 Escolha o caso de uso", [
    "Gerador de FAQs",
    "Analisador de Sentimento",
    "Gerador de Código Python",
    "Simulador de Entrevista",
    "Texto para JSON",
    "Escritor de Blog"
])

# Funções de IA
def call_openai(prompt, temperature=0.5, max_tokens=700):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

# Interface por caso
if case == "Gerador de FAQs":
    st.subheader("📋 Geração de FAQs a partir de texto")
    texto = st.text_area("Conteúdo de referência:", height=200)
    if st.button("Gerar FAQs"):
        prompt = f"""Gere uma lista de FAQs com base neste conteúdo:\n\"\"\"{texto}\"\"\""""
        st.write(call_openai(prompt))

elif case == "Analisador de Sentimento":
    st.subheader("🧠 Análise de Sentimento")
    frase = st.text_input("Digite uma frase para análise:")
    if st.button("Analisar"):
        prompt = f"Classifique o sentimento da seguinte frase como Positivo, Negativo ou Neutro:\n\n\"{frase}\""
        st.success(call_openai(prompt, temperature=0))

elif case == "Gerador de Código Python":
    st.subheader("⚙️ Geração de Função Python")
    descricao = st.text_area("Descreva a função desejada:")
    if st.button("Gerar Código"):
        prompt = f"Escreva uma função Python com comentários explicativos para:\n{descricao}"
        st.code(call_openai(prompt), language='python')

elif case == "Simulador de Entrevista":
    st.subheader("🎤 Simulador de Entrevista com IA")
    st.info("Este módulo simula uma única pergunta por vez. Para entrevista completa, use `interview_bot.py` no terminal.")
    pergunta = st.text_input("Digite sua pergunta:")
    if st.button("Responder"):
        prompt = f"Aja como um recrutador. Responda de forma profissional à seguinte pergunta:\n{pergunta}"
        st.write(call_openai(prompt, temperature=0.7))

elif case == "Texto para JSON":
    st.subheader("📑 Conversor de Texto para JSON")
    texto_json = st.text_area("Texto a ser convertido:", height=150)
    if st.button("Converter"):
        prompt = f"Converta este texto para um objeto JSON:\n\"\"\"{texto_json}\"\"\""
        st.code(call_openai(prompt), language='json')

elif case == "Escritor de Blog":
    st.subheader("✍️ Geração de Artigo de Blog")
    tema = st.text_input("Tema ou título do artigo:")
    if st.button("Gerar Artigo"):
        prompt = f"Escreva um artigo de blog com base no tema: \"{tema}\""
        st.write(call_openai(prompt, temperature=0.8, max_tokens=900))
