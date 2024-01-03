from openai import OpenAI


class OpenAIChat:
    def __init__(self, api_key, conversation, model="gpt-3.5-turbo", max_tokens=50):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.conversation = conversation

    def get_response(self, content):
        self.conversation.append({"role": "user", "content": content})

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            max_tokens=self.max_tokens
        )
        assistant_response = completion.choices[0].message.content

        return assistant_response

    def add_context_response(self, response):
        self.conversation.append({"role": "assistant", "content": response})

    def close_session(self):
        # Agrega un mensaje para cerrar la sesión
        self.conversation.append({"role": "system", "content": "Close sesion."})

        # Realiza una última llamada para cerrar la sesión
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
            max_tokens=self.max_tokens
        )
        assistant_response = completion.choices[0].message.content
        print("Session closed")
