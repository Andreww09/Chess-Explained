from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def train(file):
    trainer = ListTrainer(chatbot)
    with open(file, "r") as file:
        for line in file.readlines():
            statements = line.strip().split('|')
            questions = [question.lower() for question in statements[:-1]]
            answer = statements[-1]

            for question in questions:
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
train("chat.txt")
