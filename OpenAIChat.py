from openai import OpenAI
from TokenPricing import TokenPricing
import json


def is_json(response):
    try:
        json_object = json.loads(response)
        # print("succeeded")
        return True
    except ValueError as e:
        # print(f"failed: {e}")
        return False


def pretty_print_json(json_string):
    try:
        parsed_json = json.loads(json_string)
        pretty_json = json.dumps(parsed_json, indent=4, sort_keys=True)
        print(pretty_json)
    except ValueError as e:
        print(f"Error: {e}")


class OpenAIChat:
    def __init__(self, api_key, conversation, model="gpt-3.5-turbo", max_tokens=50, temperature=0.5, price_per_token=0):
        """
        Initializes the OpenAIChat object with the required parameters.

        Parameters:
        - api_key: API key for OpenAI API.
        - conversation: List representing the conversation history.
        - model: The GPT model to use (default: "gpt-3.5-turbo").
        - max_tokens: Maximum number of tokens for a response (default: 50).
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.conversation = conversation
        self.temperature = temperature
        self.price_per_token = price_per_token
        self.token_pricing = TokenPricing(max_tokens, price_per_token, model)

        content_value = conversation[0]["content"]
        self.token_pricing.process_string(content_value, 2)

    def get_response(self, content):
        """
        Generates a response from the OpenAI model based on user input.

        Parameters:
        - content: User input content to generate a response.

        Returns:
        - Assistant's response to the user input.
        """
        # Appending user input to the conversation
        self.conversation.append({"role": "user", "content": content})

        # Creating a completion using OpenAI API
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        # Extracting and returning the assistant's response
        assistant_response = completion.choices[0].message.content

        # Processing cost from the call
        self.token_pricing.process_string(content, 1)

        return assistant_response

    def add_context_response(self, response):
        """
        Adds an assistant's response to the conversation context.

        Parameters:
        - response: Assistant's response to be added to the conversation.
        """
        self.conversation.append({"role": "assistant", "content": response})

        # Processing cost from the call
        self.token_pricing.process_string(response, 0)

    def close_session(self):
        """
        Closes the conversation session by adding a system message and making a final call.

        Note:
        - This method adds a system message to close the session and makes a final call to the model.
        """
        # Adding a system message to close the session
        self.conversation.append({"role": "system", "content": "Close session."})

        # Making a final call to the model to close the session
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            max_tokens=self.max_tokens
        )
        # Extracting and printing the assistant's response
        assistant_response = completion.choices[0].message.content
        print("Session closed")

    def reset_session(self, new_conversation, db_content):
        print("Trying to reset conversation")

        self.print_total_cost()

        # Crear una nueva instancia de OpenAIChat con la nueva conversación
        new_instance = OpenAIChat(api_key=self.client.api_key, conversation=new_conversation, model=self.model,
                                  max_tokens=self.max_tokens, temperature=self.temperature,
                                  price_per_token=self.price_per_token)

        # Actualizar la instancia actual con la nueva instancia
        self.__dict__.update(new_instance.__dict__)

        # Add the db content to the conversation
        return self.get_response(db_content)

    def print_conversation(self):
        """
        Prints the entire conversation history.
        """
        print(self.conversation)

    def print_total_cost(self):
        """
        Prints the entire cost.
        """
        self.token_pricing.print_total_cost()

    def handle_responses(self, content):
        """
        Function to handle assistant responses and display them on the screen.

        Parameters:
        - self: Object of the OpenAIChat class.
        - user_input: User input to generate a response.
        """

        response = self.get_response(content)

        if is_json(response):
            print("La respuesta es un JSON")
            pretty_print_json(response)

            # Cargar el objeto JSON
            json_obj = json.loads(response)
            # Obtener el valor asociado a la clave "query"
            query_value = json_obj["query"]
            # Imprimir el resultado
            print("Valor de 'query':", query_value)

        else:
            print("La respuesta NO es un JSON")
            print(response)

        self.add_context_response(response)

