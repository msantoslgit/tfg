# Libraries
from openai import OpenAI

# Files
from component import API_KEY, init_prompt
from OpenAIChat import OpenAIChat
from TokenPricing import TokenPricing
from database_functions import get_available_db_directories, read_db_txt


def main():

    # Declaración de variables globales
    client = OpenAI(api_key=API_KEY)
    model = "gpt-3.5-turbo"
    max_tokens = 100
    price_per_token = 0.002 / 1000

    print(init_prompt)

    # Example of usage get_available_db_directories
    selected_db_directory = get_available_db_directories()
    print(f"Directorio seleccionado: {selected_db_directory}")

    # Example of usage read_db_txt
    db_content = read_db_txt(selected_db_directory)
    print(db_content)

    # Example of usage TokenPricing
    token_pricing = TokenPricing(max_tokens, price_per_token, model)

    num_tokens = token_pricing.num_tokens_from_string(init_prompt)
    total_price = token_pricing.total_price(num_tokens)

    print(f"Number of tokens: {num_tokens}")
    print(f"Total price: ${total_price}")

    # Ejemplo de uso de la funcion OpenAIChat

    # Inicia la conversación con un mensaje de sistema
    init_conversation = [{"role": "system",
                          "content": init_prompt}]

    # Iniciamos la clase con el modelo, max_tokens, la API_KEY y la conversación inicial
    openai_chat = OpenAIChat(api_key=API_KEY, conversation=init_conversation,  model=model, max_tokens=max_tokens)

    # Pasamos al modelo la base de datos que hemos cargado de los ficheros
    response = openai_chat.get_response(db_content)
    print(response)

    if response == "1":

        while True:

            content = input(" ")

            if content == "exit":
                openai_chat.close_session()
                break

            response = openai_chat.get_response(content)

            print(response)
            openai_chat.add_context_response(response)
    else:
        print("La carga inicial de la base de datos no ha funcionado")


if __name__ == "__main__":
    main()
