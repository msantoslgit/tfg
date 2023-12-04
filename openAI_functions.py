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


def close_session(client, model, conversation, max_tokens):
    # Agrega un mensaje para cerrar la sesión
    conversation.append({"role": "system", "content": "Session Ended."})

    # Realiza una última llamada para cerrar la sesión
    completion = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=max_tokens
    )
    # assistant_response = completion.choices[0].message['content']
    assistant_response = completion.choices[0].message.content
    print(assistant_response)

