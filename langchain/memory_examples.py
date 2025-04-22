from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Simula um pequeno diálogo
print(conversation.run("Olá, quem é você?"))
print(conversation.run("Qual foi minha pergunta anterior?"))
