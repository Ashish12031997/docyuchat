import openai
import os
class OpenAI:
    def __init__(self):
        openai.api_key = os.getenv('OPEN_AI_API_KEY')

    def get_embedding(self, text):
        response = openai.embeddings.create(
            model="text-embedding-ada-002", input=text.replace("\n", " ")
        )
        embedding = response.data[0].embedding
        return embedding

    def get_completion_from_messages(
        self, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=1000
    ):
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
