from pathlib import Path
import json


project_root_path = Path(__file__).absolute().parent.parent
PATH_TO_SECRET = project_root_path / 'secret' / 'openai' / 'credentials.json'
with open(PATH_TO_SECRET, 'r') as f:
    secret_dict = json.load(f)

USERNAME = secret_dict['USERNAME']
PASSWORD = secret_dict['PASSWORD']


project_root_path = Path(__file__).absolute().parent.parent
PATH_TO_SECRET = project_root_path / 'secret' / 'openai' / 'api_key.json'
with open(PATH_TO_SECRET, 'r') as f:
    secret_dict = json.load(f)

API_KEY = secret_dict['API_KEY']

PATH_TO_PROMPT = project_root_path / 'tfg' / 'source' / 'init_prompt' / 'sql_assistant_3.txt'
with open(PATH_TO_PROMPT, 'r', encoding='utf-8') as f:
    init_prompt = f.read()


init_database_message = "Initial loading of the database has succeeded. Now you can ask anything related to the model\n" \
                        "Enter 'exit' to close the current session or 'reset' to reload the DB and restart the chat\n" \
                        "Enter 'cost' to know how much is the actual cost in dollars for all the request to the API\n" \
                        "Enter 'reset' to start again with the conversation\n"

instructions = "Instructions:" \
                        "\n1. Insert the database-related query you have chosen." \
                        "\n2. Press the 'Send' button to submit the message." \
                        "\n3. If you type 'Cost' and press send, you will receive the cost in dollars of the query so far." \
                        "\n4. If you type 'Exit', the session will be closed, and the program will end." \
                        "\n5. If you type 'Reset', the conversation with the AI and the cost will be reset."

