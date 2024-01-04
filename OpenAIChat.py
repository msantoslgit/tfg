from openai import OpenAI


class OpenAIChat:
    def __init__(self, api_key, conversation, model="gpt-3.5-turbo", max_tokens=50, temperature=0.5):
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
        return assistant_response

    def add_context_response(self, response):
        """
        Adds an assistant's response to the conversation context.

        Parameters:
        - response: Assistant's response to be added to the conversation.
        """
        self.conversation.append({"role": "assistant", "content": response})

    def add_context_user_content(self, content):
        """
        Adds user input content to the conversation context.

        Parameters:
        - content: User input content to be added to the conversation.
        """
        self.conversation.append({"role": "user", "content": content})

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

    def print_conversation(self):
        """
        Prints the entire conversation history.
        """
        print(self.conversation)
