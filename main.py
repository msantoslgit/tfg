from openai import OpenAI
from component import API_KEY

client = OpenAI(api_key = API_KEY)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an expert translator."},
    {"role": "user", "content": "Translate te following word to spanish and catalan: Teddy Bear."}
  ]
)

print(completion.choices[0].message)
