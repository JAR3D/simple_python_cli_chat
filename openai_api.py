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