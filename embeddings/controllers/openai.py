import openai
import os
import asyncio
class OpenAI:
    def __init__(self):
        openai.api_key = os.getenv('OPEN_AI_API_KEY')

    def get_embedding(self, text):
        response = openai.embeddings.create(
            model="text-embedding-ada-002", input=text.replace("\n", " ")
        )
        embedding = response.data[0].embedding
        return embedding

    async def get_completion_from_messages(
        self, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=1000
    ):
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )
        for chunk in response:
            content = getattr(chunk.choices[0].delta, "content", None)  # Use getattr safely
            if content:
                yield content  # Yield each chunk as it's received
                await asyncio.sleep(0)  # Ensures async compatibility
