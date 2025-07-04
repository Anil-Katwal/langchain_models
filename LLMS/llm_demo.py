import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"  # You can try 'mixtral-8x7b-32768' or others
)
Respone=input('enter the prompt')
response = llm.invoke([HumanMessage(content=Respone)])
print(response.content)
