#Libraries
from openai import OpenAI


#Files
from component import API_KEY
from openAI_functions import get_response, close_session, add_context_response
from database_functions import read_db_txt, get_available_db_directories #, get_db_directory

from OpenAIChat import OpenAIChat

def main():

    # # Example of usage get_available_db_directories
    # selected_db_directory = get_available_db_directories()
    # print(f"Directorio seleccionado: {selected_db_directory}")
    #
    # # Example of usage read_db_txt
    # total_content = read_db_txt(selected_db_directory)
    # print(total_content)


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

    ## Ejemplo de uso de la funcion OpenAIChat

    client = OpenAI(api_key=API_KEY)
    model = "gpt-3.5-turbo"
    max_tokens = 100

    # Inicia la conversación con un mensaje de sistema
    init_conversation = [{"role": "system",
                          "content": "You are a helpful assistant."}]

    openai_chat = OpenAIChat(api_key=API_KEY, conversation=init_conversation,  model=model, max_tokens=max_tokens)


    print("¿Sobre que quieres hablar? ")
    while True:

        content = input(" ")

        if content == "exit":
            openai_chat.close_session()
            break

        response = openai_chat.get_response(content)

        print(response)
        openai_chat.add_context_response(response)


if __name__ == "__main__":
    main()
