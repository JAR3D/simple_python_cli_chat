# Simple Python CLI Chat

A basic command-line interface (CLI) chat application that interacts with the OpenAI API.

## Description

This project provides a simple chat interface running in your terminal. You can have a conversation with an AI assistant powered by OpenAI's chat completion models (specifically configured for `gpt-3.5-turbo` in `tools.py`). The application keeps track of the conversation history and displays the estimated cost for each API interaction.

## Features

*   **CLI Interaction:** Chat directly from your terminal.
*   **OpenAI Integration:** Uses the OpenAI API for generating chat responses.
*   **Function Calling:** Supports OpenAI function calling. Currently includes a `close_session` function to end the chat.
*   **Cost Calculation:** Estimates and displays the cost of each API call based on token usage.
*   **Conversation History:** Maintains the context of the conversation.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace with the actual URL if available
    cd simple_python_cli_chat
    ```
2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    *This project requires the `openai` and `python-dotenv` packages.* You can install them using pip:
    ```bash
    pip install openai python-dotenv
    ```
4.  **Configure Environment Variables:**
    Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY='your_openai_api_key_here'
    ```
    The `.gitignore` file should already include `.env` to prevent accidentally committing your key.

## Usage

Run the main script from the terminal:

```bash
python main.py
```

Enter your messages when prompted. The chat will continue until the `close_session` function is triggered (e.g., by saying "goodbye" or "exit" - the exact trigger depends on the AI's interpretation and function call).
