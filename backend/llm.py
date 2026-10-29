from langchain_groq import ChatGroq

from config import GROQ_API_KEY


def get_llm():
    """
    Load Groq LLM.
    """

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=GROQ_API_KEY,
        temperature=0.0,
        max_tokens=700,
    )

    return llm