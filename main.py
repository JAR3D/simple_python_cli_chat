import json
from openai_api import get_chat_completion, functions_list
from tools import calculate_tokens_cost, MODEL_35_TURBO

is_session_active = True

def close_session():
    global is_session_active
    is_session_active = False
    return ""

functions_dict = {
    "close_session": close_session,
}

def get_function_to_call(function_name):
    if function_name in functions_dict:
        return functions_dict[function_name]
    else:
        raise ValueError(f"Function {function_name} is not supported.")



messages = [
    {
        "role": "system",
        "content": """
            You are an helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!
            If in your response you mention a number, for example 'seven', please write it as '7'."""
    }
]

while is_session_active:
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
    chat_completion = get_chat_completion(messages, tools=functions_list)
    # Extract the assistant's message
    gpt_message = chat_completion.choices[0].message
    # Append the assistant's message to messages
    messages.append(gpt_message)

    # If tool_calls is not empty
    if gpt_message.tool_calls:
        # For each tool_call, call the corresponding function and append it to messages
        for tool_call in gpt_message.tool_calls:
            # Extract the function name and arguments
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # Get the function to call
            function_to_call = get_function_to_call(function_name)

            # Call the function with the extracted arguments
            if function_name == "close_session":
                function_result = function_to_call()

            # Append the function result to messages with corresponding tool_call_id
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_result
            })

            # Print the function call id
            print(tool_call.id)

        chat_completion = get_chat_completion(messages, tools=functions_list)
        gpt_message = chat_completion.choices[0].message
        messages.append(gpt_message)

    total_usage_costs = calculate_tokens_cost(MODEL_35_TURBO, chat_completion)

    print("You:", user_input)
    print("Assistant: ", gpt_message.content)
    print("Cost:", f"${total_usage_costs:.8f}")
    print()
