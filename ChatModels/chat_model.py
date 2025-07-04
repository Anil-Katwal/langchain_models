import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq chat model
llm_model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192"  # You can also try 'mixtral-8x7b-32768' or others
)

def chat():
    print("Groq Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input(" You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = llm_model.invoke([HumanMessage(content=user_input)])
            print("Groq:", response.content, "\n")
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    chat()
