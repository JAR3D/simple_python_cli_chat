import os
from dotenv import load_dotenv

from openai import OpenAI

from tools import calculate_tokens_cost, MODEL_35_TURBO

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

user_input = input("Enter a message: ")

messages = [
    {
        "role": "user",
        "content": user_input
    },
    {
        "role": "system",
        "content": """
            You are an helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!
            If in your response you mention a number, for example 'seven', please write it as '7'."""
    }
]

chat_completion = get_chat_completion(messages)
gpt_response = chat_completion.choices[0].message.content

total_usage_costs = calculate_tokens_cost(MODEL_35_TURBO, chat_completion)

print("You:", user_input)
print("Assistant: ", gpt_response)
print("Cost:", f"${total_usage_costs:.8f}")