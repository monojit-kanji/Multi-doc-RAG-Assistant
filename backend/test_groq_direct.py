from groq import Groq
from config import GROQ_API_KEY

print("API key loaded:", bool(GROQ_API_KEY))

client = Groq(api_key=GROQ_API_KEY)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
)

print(response.choices[0].message.content)