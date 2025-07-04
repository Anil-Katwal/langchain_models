import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Initialize the Google Gemini chat model
llm_model = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-pro"  # Gemini model (not Groq!)
)

def chat():
    print("Gemini Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = llm_model.invoke([HumanMessage(content=user_input)])
            print("Gemini:", response.content, "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
