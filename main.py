import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_API_BASE_URL = os.environ.get("OPENAI_API_BASE_URL")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_API_BASE_URL,
)

def get_chat_completion(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
    )

prompt = "What are you?"

messages = [
    {
        "role": "user",
        "content": prompt
    },
    {
        "role": "system",
        "content": "You are an helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!"
    }
]

chat_completion = get_chat_completion(messages)
gpt_response = chat_completion.choices[0].message.content

print(gpt_response)