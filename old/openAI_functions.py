from openai import OpenAI


def get_response(client, model, conversation, content, max_tokens):
    conversation.append({"role": "user", "content": content})

    completion = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=max_tokens
    )
    # assistant_response = completion.choices[0].message['content']
    assistant_response = completion.choices[0].message.content

    return assistant_response


def add_context_response(conversation, response):
    conversation.append({"role": "assistant", "content": response})


def close_session(client, model, max_tokens):
    # Agrega un mensaje para cerrar la sesión
    conversation = [{"role": "system", "content": "Close sesion."}]

    # Realiza una última llamada para cerrar la sesión
    completion = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=max_tokens
    )
    # assistant_response = completion.choices[0].message['content']
    assistant_response = completion.choices[0].message.content
    print("Session closed")

## Ejemplo de uso con las funciones sueltas
    # client = OpenAI(api_key=API_KEY)
    # model = "gpt-3.5-turbo"
    # max_tokens = 50
    #
    # # Inicia la conversación con un mensaje de sistema
    # conversation = [{"role": "system",
    #                  "content": "You are a helpful assistant."}]
    #
    # print("¿Sobre que quieres hablar? ")
    # while True:
    #
    #     content = input(" ")
    #
    #     if content == "exit":
    #         close_session(client, model, max_tokens)
    #         break
    #
    #     response = get_response(client, model, conversation, content, max_tokens)
    #
    #     print(response)
    #     add_context_response(conversation, response)
