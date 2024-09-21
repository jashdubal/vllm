from openai import OpenAI

api_key = "sk-0qL5X8H8x6w7n7g7z7v7t7r7e7u7i7a7"
base_uri = "http://localhost:8000/v1"


client = OpenAI(
    api_key=api_key,
    base_url=base_uri
)

models = client.models.list()
model = models.data[0].id

print(model)


completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello world"},
    ]
)

print(completion.choices[0].message.content)