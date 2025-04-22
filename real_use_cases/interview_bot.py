# Simula uma entrevista de emprego com memória de contexto (LangChain)

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.6)
memory = ConversationBufferMemory()
interview = ConversationChain(llm=llm, memory=memory)

print("Bem-vindo ao Simulador de Entrevista!")
print("Digite 'sair' para encerrar a sessão.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        break
    resposta = interview.run(user_input)
    print("Entrevistador:", resposta)

# Requisitos: pip install langchain openai python-dotenv
