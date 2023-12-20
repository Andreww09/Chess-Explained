from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json


def create_and_train_chatbot():
    chatbot = ChatBot(
        "ChessExplained",
        preprocessors=[
            'chatterbot.preprocessors.convert_to_ascii',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.clean_whitespace']
        ,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'Sorry, I am unable to process your request.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

    trainer = ListTrainer(chatbot)

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        for question, answer in data.items():
            trainer.train([question.lower(), answer])

    except FileNotFoundError:
        print("data.json file not found.")
    except json.JSONDecodeError:
        print("data.json is not a valid JSON file.")

    return chatbot


chatbot = create_and_train_chatbot()


def get_response(message):
    response = chatbot.get_response(message.lower())
    return str(response)


while True:
    try:
        question = input("You: ")
        response = get_response(question)
        print("Bot: ", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nExiting chat...")
        break
