# Libraries
from openai import OpenAI

# Files
from component import API_KEY, init_prompt
from OpenAIChat import OpenAIChat
from Tester import Tester
from database_functions import get_available_db_directories, read_db_txt


def main():

    # Declaration of global variables
    client = OpenAI(api_key=API_KEY)
    model = "gpt-3.5-turbo"
    max_tokens = 200
    price_per_token = 0.002 / 1000

    # Usage of get_available_db_directories
    selected_db_directory = get_available_db_directories()
    print(f"Selected directory: {selected_db_directory}")

    # Usage of read_db_txt
    db_content = read_db_txt(selected_db_directory)
    print(db_content)


    # Start the conversation with a system message
    init_conversation = [{"role": "system", "content": init_prompt}]

    # Initialize the OpenAIChat class with the model, max_tokens, API_KEY, and the initial conversation
    openai_chat = OpenAIChat(api_key=API_KEY, conversation=init_conversation, model=model,
                             max_tokens=max_tokens, price_per_token=price_per_token)

    # Pass the loaded database content to the model
    response = openai_chat.get_response(db_content)
    # response = '1'

    if response == "1":
        print("Initial loading of the database has succeeded. Initializing tester \n")

        tester = Tester(openai_chat)
        tester.test()

    else:
        print("Initial loading of the database has failed")


if __name__ == "__main__":
    main()
