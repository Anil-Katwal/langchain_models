# langchain_models
## What are Models?
The Model Component in Langchain is a crucial part of the framework, designed to faciliate interactions with various language models and embedding models.
It abstracts the complexity of working directly with different LLMs, chat models, and embedding models, providing a uniform interface to communicate with them. This makes it easier to build applications that rely n AI-generated text, text embedding for similarity search. andd retrieval_agumented generation(RAG)

## Language Model:
### 1. Language Models:LLMs, Chat Models
### 2. Embedding Models:
language Models are used for the chat based application but embedding models used for the semantic search for example RAG.
## Sources:
Language Models: 
closed source- open AI, clude, gemini
Open source- Hugging Faces.

## Language Models:
Language Models are AI systems, designed to process, generate, and understand natural language text.

LLMs:- General purpose models that is used for raw text generation. They are string plain text as input and returns a string(Plain text). These are traditionally older models and are not used much now.

Chat Models:
Language models that are specilized for the conventational tasks. They take a sequence of messages as inputs and retun chat messages as outputs(as oppiste) to using plain text. These are traditionally newer models and used more in comparision to the LLMs.
## ***************************LLMs*************************
Groq
## Open Source Model:
Hugging face
1. Using HF Inference API
2. Locally 
## Disadvantage of Using Open Source Models:
1. High Hardware Requirements: Running large models(eg. LLaMA-2-70B) requires expensive GPUS
2.Setup Complexity: Requires installation of dependencies like pytorch, CUDA, transformers.
3. Lack of RLHF: Most open-source models do not have fine-tuning with human feedback, making them weaker in instruction-following
4. Limited Multimodel Abilities: Open Models don't support image, audio, or video like GPT-4V