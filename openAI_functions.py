from openai import OpenAI


def get_response(client, model, conversation, content):
    conversation.append({"role": "user", "content": content})

    completion = client.chat.completions.create(
        model=model,
        messages=conversation
    )
    # assistant_response = completion.choices[0].message['content']
    assistant_response = completion.choices[0].message

    return assistant_response


def close_session(client, model, conversation):
    # Agrega un mensaje para cerrar la sesión
    conversation.append({"role": "system", "content": "Session Ended."})

    # Realiza una última llamada para cerrar la sesión
    completion = client.chat.completions.create(
        model=model,
        messages=conversation
    )
    # assistant_response = completion.choices[0].message['content']
    assistant_response = completion.choices[0].message
    print(assistant_response)

