from chatterbot import ChatBot

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

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"{chatbot.get_response(query)}")
