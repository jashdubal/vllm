import asyncio
from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"  # Replace with your actual API key or mechanism if needed
openai_api_base = "http://localhost:8000/v1"  # Assuming default vLLM server address

async def main():
    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    # Example chat interaction
    chat_response = await client.chat.completions.acreate(
        model="your_model_name",  # Replace with the actual model name served by vLLM
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print("Chat completion results:")
    print(chat_response.choices.message.content)

if __name__ == "__main__":
    asyncio.run(main())
