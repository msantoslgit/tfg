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

