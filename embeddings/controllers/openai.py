import openai


class OpenAI:
    def __init__(self):
        openai.api_key = "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"

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
