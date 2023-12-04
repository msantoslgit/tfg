#Libraries
from openai import OpenAI

#Files
from component import API_KEY
from openAI_functions import get_response, close_session


def main():

    client = OpenAI(api_key=API_KEY)
    model = "gpt-3.5-turbo"

    # Inicia la conversación con un mensaje de sistema
    conversation = [{"role": "system",
                     "content": "You are a helpful assistant."}]

    while True:

        content = input("¿Sobre que quieres hablar? ")

        if content == "exit":
            close_session(client, model, conversation)
            break

        response = get_response(client, model, conversation, content)
        print(response)


if __name__ == "__main__":
    main()
