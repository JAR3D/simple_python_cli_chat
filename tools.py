MODEL_35_TURBO = "gpt-3.5-turbo"
MODEL_4O_MINI = "gpt-4o-mini"

MODELS = {
    MODEL_35_TURBO: {"input_cost": 0.5 / 1000000, "output_cost": 1.5 / 1000000},
    MODEL_4O_MINI: {"input_cost": 0.15 / 1000000, "output_cost": 0.6 / 1000000, "cached_input_cost": 0.075 / 1000000},
}


def calculate_tokens_cost(model, chat_completion):
    if model not in MODELS:
        raise ValueError(f"Model {model} is not supported.")

    model_costs = MODELS[model]
    input_tokens_cost = chat_completion.usage.prompt_tokens * model_costs["input_cost"]
    output_tokens_cost = (
        chat_completion.usage.completion_tokens * model_costs["output_cost"]
    )

    # TODO: Add support for cached input cost

    return input_tokens_cost + output_tokens_cost