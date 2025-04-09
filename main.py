from openai_api import get_chat_completion
from tools import calculate_tokens_cost, MODEL_35_TURBO

messages = [
    {
        "role": "system",
        "content": """
            You are an helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!
            If in your response you mention a number, for example 'seven', please write it as '7'."""
    }
]

while True:
    # Get user input
    user_input = input("Enter a message: ")

    # Add user input to messages
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Get chat completion
    chat_completion = get_chat_completion(messages)
    # Extract the assistant's message
    gpt_message = chat_completion.choices[0].message
    # Append the assistant's message to messages
    messages.append(gpt_message)

    total_usage_costs = calculate_tokens_cost(MODEL_35_TURBO, chat_completion)

    print("You:", user_input)
    print("Assistant: ", gpt_message.content)
    print("Cost:", f"${total_usage_costs:.8f}")
