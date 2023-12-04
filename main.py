from openai import OpenAI
from component import API_KEY


def main():
    client = OpenAI(api_key=API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert translator."},
            {"role": "user", "content": "Translate the following word to Spanish and Catalan: Teddy Bear."}
        ]
    )

    print(completion.choices[0].message)


if __name__ == "__main__":
    main()
