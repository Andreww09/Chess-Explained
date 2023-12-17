import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def train(file):
    trainer = ListTrainer(chatbot)
    with open(file) as file:
        data = json.load(file)

    for question, answer in data.items():
        trainer.train([question, answer])


chatbot = ChatBot("ChessExplained",
                  preprocessors=['chatterbot.preprocessors.convert_to_ascii',
                                 'chatterbot.preprocessors.unescape_html',
                                 'chatterbot.preprocessors.clean_whitespace'],
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'Sorry, I am unable to process your request.',
                          'maximum_similarity_threshold': 0.90
                      }
                  ]
                  )
train('training_dataset.json')
