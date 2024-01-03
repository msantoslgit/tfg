import tiktoken

max_tokens = 50
price_per_token = 0.002 / 1000


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def total_price(num_tokens: int, max_tokens: int, price_token: float) -> float:
    """Returns the total price for the input"""
    return num_tokens * price_token + max_tokens * price_token


