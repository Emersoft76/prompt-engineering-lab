import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Carrega variáveis de ambiente
load_dotenv()

st.set_page_config(page_title="🧠 LangChain Chatbot", layout="centered")
st.title("💬 LangChain Chatbot Demo")

# Inicializa memória e modelo
memory = ConversationBufferMemory()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# Interface
user_input = st.text_input("Você:", "")

if user_input:
    output = conversation.run(user_input)
    st.markdown(f"**Assistente:** {output}")
