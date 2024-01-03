import tiktoken


class TokenPricing:
    def __init__(self, max_tokens, price_per_token, model_name):
        self.max_tokens = max_tokens
        self.price_per_token = price_per_token
        self.model_name = model_name

    def num_tokens_from_string(self, string):
        """Returns the number of tokens in a text string."""
        encoding = tiktoken.encoding_for_model(self.model_name)
        n_tokens = len(encoding.encode(string))
        return n_tokens

    def total_price(self, num_tokens):
        """Returns the total price for the input"""
        return num_tokens * self.price_per_token + self.max_tokens * self.price_per_token
