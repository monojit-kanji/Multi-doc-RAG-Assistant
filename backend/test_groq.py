from langchain_groq import ChatGroq
from config import GROQ_API_KEY

print("API key loaded:", bool(GROQ_API_KEY))

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0,
    max_tokens=100,
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)