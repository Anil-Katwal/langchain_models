import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Step 1: Create the raw LLM using HuggingFaceEndpoint with task='conversational'
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

# Step 2: Wrap the LLM in ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm)

# Chat loop
def chat():
    print("TinyLlama Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        try:
            response = chat_model.invoke([HumanMessage(content=user_input)])
            print("TinyLlama:", response.content, "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
