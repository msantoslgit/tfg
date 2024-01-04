# Libraries
from openai import OpenAI

# Files
from component import API_KEY, init_prompt
from OpenAIChat import OpenAIChat
from TokenPricing import TokenPricing
from database_functions import get_available_db_directories, read_db_txt


def main():

    # Declaration of global variables
    client = OpenAI(api_key=API_KEY)
    model = "gpt-3.5-turbo"
    max_tokens = 100
    price_per_token = 0.002 / 1000

    # Usage of get_available_db_directories
    selected_db_directory = get_available_db_directories()
    print(f"Selected directory: {selected_db_directory}")

    # Usage of read_db_txt
    db_content = read_db_txt(selected_db_directory)
    print(db_content)

    # Example of using TokenPricing
    token_pricing = TokenPricing(max_tokens, price_per_token, model)

    num_tokens = token_pricing.num_tokens_from_string(init_prompt)
    total_price = token_pricing.total_price(num_tokens)

    print(f"Number of tokens: {num_tokens}")
    print(f"Total price: ${total_price}")

    # Start the conversation with a system message
    init_conversation = [{"role": "system", "content": init_prompt}]

    # Initialize the OpenAIChat class with the model, max_tokens, API_KEY, and the initial conversation
    openai_chat = OpenAIChat(api_key=API_KEY, conversation=init_conversation, model=model, max_tokens=max_tokens)

    # Pass the loaded database content to the model
    response = openai_chat.get_response(db_content)

    if response == "1":
        print("Initial loading of the database has succeeded. Now you can ask anything related to the model")
        while True:
            content = input(" ")

            if content == "exit":
                openai_chat.close_session()
                break

            response = openai_chat.get_response(content)
            print(response)
            openai_chat.add_context_response(response)
    else:
        print("Initial loading of the database has failed")


if __name__ == "__main__":
    main()
