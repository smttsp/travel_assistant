import openai


def get_location_csv(query):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )

    print(completion.choices[0].message.content)

    return None
