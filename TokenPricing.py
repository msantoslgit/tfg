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
        self.total_cost = 0
        self.previous_tokens = 0

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

    def add_tokens_to_previous(self, n_tokens):
        """
        Adds the given number of tokens to the previous count.

        Parameters:
        - n_tokens: Number of tokens to add to the previous count.
        """
        self.previous_tokens += n_tokens

    def api_call_total_price(self):
        """
        Returns the total price for the given number of tokens.

        Parameters:
        - num_tokens: Number of tokens to calculate the total price.

        Returns:
        - Total price based on the number of tokens and pricing information.
        """
        # Calculating the total price based on the number of tokens and pricing information
        total_price = self.previous_tokens * self.price_per_token + self.max_tokens * self.price_per_token
        return total_price

    def add_cost(self, price):
        """
        Adds the given price to the total cost.

        Parameters:
        - price: Price to add to the total cost.
        """
        self.total_cost += price

    def process_string(self, input_string, call):
        """
        Process the input string by adding tokens to the count and calculating cost.

        Parameters:
        - input_string: The text string to process.
        - call: A flag indicating whether to calculate the cost (call == 1) or just add tokens (call == 0).

        If call == 1, the function calculates the cost based on the number of tokens and adds it to the total cost.
        If call == 0, the function only adds the tokens to the count without calculating the cost.

        Note: The function relies on previously set attributes like max_tokens, price_per_token, and model_name.

        """

        # Only for testing
        # print("Tokens before processing")
        # self.print_total_tokens()

        # Calculate the number of tokens in the input string
        num_tokens = self.num_tokens_from_string(input_string)

        # Add the tokens to the count
        self.add_tokens_to_previous(num_tokens)

        # Only for testing
        # print("Tokens after processing")
        # self.print_total_tokens()

        # Check if cost calculation is required (call == 1)
        if call == 1:
            # Calculate the total cost based on the number of tokens and pricing information
            total_price = self.api_call_total_price()

            # Add the calculated cost to the total cost
            self.add_cost(total_price)

            # Print the cost for this API call
            print("The cost for this API call was: ")
            print(round(total_price, 7))
        # elif call == 0:
        #     print("Add response had no cost, only increase the n_tokens")
        # elif call == 2:
        #     print("Innit the model had no cost, only increase the n_tokens")

    def print_total_cost(self):
        """
        Print the total cost accumulated during the API session.

        This function prints the total cost incurred during the API session.
        The total cost is rounded to 7 decimal places for better readability.

        """
        # Print the message indicating the total cost for the API session
        print("The cost for this API session was: ")

        # Print the total cost rounded to 7 decimal places
        print(round(self.total_cost, 7))

    def get_total_cost(self):
        """
        Return total cost accumulated during the API session.

        This function Returns the total cost incurred during the API session.
        The total cost is rounded to 7 decimal places for better readability.

        """
        # Print the total cost rounded to 7 decimal places
        return round(self.total_cost, 7)

    def print_total_tokens(self):
        print(self.previous_tokens)




    # # Example of using TokenPricing
    # token_pricing = TokenPricing(max_tokens, price_per_token, model)
    #
    # num_tokens = token_pricing.num_tokens_from_string(init_prompt)
    # total_price = token_pricing.total_price(num_tokens)
    #
    # print(f"Number of tokens: {num_tokens}")
    # print(f"Total price: ${total_price}")
