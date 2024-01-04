import tiktoken


class TokenPricing:
    def __init__(self, max_tokens, price_per_token, model_name):
        """
        Initializes the TokenPricing object with the required parameters.

        Parameters:
        - max_tokens: Maximum number of tokens allowed.
        - price_per_token: Price per token for the model.
        - model_name: Name of the model for token encoding.
        """
        self.max_tokens = max_tokens
        self.price_per_token = price_per_token
        self.model_name = model_name

    def num_tokens_from_string(self, string):
        """
        Returns the number of tokens in a text string.

        Parameters:
        - string: Text string to calculate the number of tokens.

        Returns:
        - Number of tokens in the input text string.
        """
        # Obtaining the encoding for the specified model
        encoding = tiktoken.encoding_for_model(self.model_name)
        # Calculating the number of tokens in the input string
        n_tokens = len(encoding.encode(string))
        return n_tokens

    def total_price(self, num_tokens):
        """
        Returns the total price for the given number of tokens.

        Parameters:
        - num_tokens: Number of tokens to calculate the total price.

        Returns:
        - Total price based on the number of tokens and pricing information.
        """
        # Calculating the total price based on the number of tokens and pricing information
        return num_tokens * self.price_per_token + self.max_tokens * self.price_per_token
