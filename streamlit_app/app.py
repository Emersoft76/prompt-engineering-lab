import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🧠 Prompt Playground", layout="centered")
st.title("🧪 Prompt Playground (OpenAI API)")

st.markdown("Digite seu prompt abaixo para testar diretamente com a API da OpenAI.")

prompt = st.text_area("✍️ Prompt", height=200)
temperature = st.slider("🎛️ Temperature", 0.0, 1.0, 0.7)
model = st.selectbox("📦 Modelo", ["gpt-3.5-turbo", "gpt-4"])

if st.button("Enviar"):
    with st.spinner("Consultando IA..."):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=700
        )
        result = response.choices[0].message.content.strip()
        st.success("Resposta gerada!")
        st.markdown("### ✨ Resposta:")
        st.write(result)
