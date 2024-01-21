from openai import OpenAI as gpt


class OpenAI:
    def __init__(self, api_key="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"):
        self.api_key = api_key
        self.client = gpt(
            api_key=api_key
        )

    def reword(self, text):

        if self.api_key == "":
            return text

        message = ("You are a skilled chess player, reword the following sentence to make it sound more natural and "
                   "chess-like, such that a beginner chess player can understand why that move is the best: ") + text
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            model="gpt-4",
        )

        return chat_completion.choices[0].message.content
