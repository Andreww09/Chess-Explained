from chatterbot import ChatBot


chatbot = ChatBot("back",
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
    try:
        query = input("You: ")
        if query in exit_conditions:
            break
        response = chatbot.get_response(query.lower())
        print(f"Bot: {response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nExiting chat...")
        break
