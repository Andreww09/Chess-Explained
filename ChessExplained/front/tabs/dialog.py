import customtkinter
from chatterbot import ChatBot
from customtkinter import *

from back.utils import Util


class Dialog(customtkinter.CTkFrame):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.chatbot = ChatBot("back",
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
        self.responses = Responses(self, **kwargs)
        self.responses.grid(row=0, column=0,
                            sticky="nsew",
                            padx=10, pady=10)
        self.entryBox = CTkTextbox(master=self, width=350, height=80)
        self.entryBox.grid(row=1, column=0,
                           columnspan=1, rowspan=1,
                           sticky="nsew",
                           padx=10, pady=10)
        self.entryBox.bind("<Return>", self.add_text)
        self.entryBox.focus()

    def add_text(self, event):
        text = self.entryBox.get("1.0", "end")
        self.responses.add_text(text, 1)
        response = self.get_response(text)
        self.responses.add_text(response, 0)

        # Clear the text in the CTkTextbox if needed
        self.entryBox.delete("1.0", "end")
        self.responses.update()

    def get_response(self, msg):
        response = Util.process_question(msg)
        if response is None:
            response = str(self.chatbot.get_response(msg.lower()))
        return response


class Responses(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=350, height=500, **kwargs)

        self.messages = ["Hi"]
        self.turn = [0]
        self.textBox = []
        for i, message in enumerate(self.messages):
            self.create_conversation(i, message)

    def add_text(self, message, turn):
        self.messages.append(message)
        self.turn.append(turn)
        self.create_conversation(len(self.messages) - 1, message)

    def create_conversation(self, index, message):
        max_column = 350 // 2 + 1
        font_size = 15
        message_width = len(message) * font_size
        message_height = (message_width // 280 + 1) * 12
        message_width = min(280, message_width)
        columnspan = message_width // 2 + 1
        column = self.turn[index] * (max_column - columnspan)
        self.textBox.append(CTkTextbox(master=self, width=message_width, height=message_height))
        self.textBox[index].insert("1.0", message)
        self.textBox[index].grid(row=index, column=column, columnspan=columnspan, sticky="nsew", padx=10, pady=10)
        self.textBox[index].configure(state=DISABLED)