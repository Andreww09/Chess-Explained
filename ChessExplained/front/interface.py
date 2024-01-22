import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
from chatterbot import ChatBot
import back.stockfish_tools as sf
from back.utils import BoardUtils
from back.utils import Util


class App(CTk):

    def __init__(self, engine_path, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.engine_path = engine_path
        self.title("Chess Explained")
        self.geometry("750x600")
        self.resizable(True, True)
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

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.img = ImageTk.PhotoImage(Image.open("front/assets/label.png"))
        self.label = CTkLabel(master=self, image=self.img, text="")
        self.label.grid(row=0, column=0,
                        columnspan=5,
                        sticky="nsew")

        self.textBox = CTkTextbox(master=self)
        self.textBox.grid(row=1, column=0,
                          rowspan=3, columnspan=5,
                          sticky="nsew",
                          padx=10, pady=10)
        self.textBox.configure(state=DISABLED)

        self.entryBox = CTkTextbox(master=self)
        self.entryBox.grid(row=4, column=0,
                           columnspan=4, rowspan=2,
                           sticky="nsew",
                           padx=10, pady=10)
        self.entryBox.focus()

        self.button1 = CTkButton(master=self, text="Send",
                                 command=lambda: self._on_enter_pressed())
        self.button1.grid(row=4, column=4, sticky="nsew", padx=10, pady=10)

        self.button2 = CTkButton(master=self, text="Best Move", command=lambda: self.input())
        self.button2.grid(row=5, column=4, sticky="nsew", padx=10, pady=10)

        # Set the theme
        set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.mainloop()

    def _on_enter_pressed(self):
        msg = self.entryBox.get("1.0", END)
        msg = msg.rstrip()
        msg = msg.lstrip()
        if not msg or msg == "":
            return
        else:
            self.entryBox.delete("1.0", END)
            self._insert_message(msg, "You")

    def input(self):
        fen_input = CTkInputDialog(text="Insert chess board FEN", title="Chess Explained")
        fen = fen_input.get_input()
        if fen is None:
            return
        fen = fen.lstrip()
        fen = fen.rstrip()
        if fen:
            if BoardUtils.is_valid_fen(fen):
                self._get_best_move(fen)
            else:
                self.textBox.configure(state=NORMAL)
                self.textBox.insert(END, "ChessBot: The provided fen is not a valid one\n\n")
                self.textBox.configure(state=DISABLED)

    def _insert_message(self, msg, sender):
        print(msg)
        msg1 = f"{sender}: {msg}\n"
        self.textBox.configure(state=NORMAL)
        self.textBox.insert(END, msg1)
        self.textBox.configure(state=DISABLED)
        response = Util.process_question(msg)
        if response is None:
            response = self.chatbot.get_response(msg.lower())
        msg2 = f"ChessBot: {response}\n\n"
        self.textBox.configure(state=NORMAL)
        self.textBox.insert(END, msg2)
        self.textBox.configure(state=DISABLED)

        return 0

    def _get_best_move(self, fen):
        self.textBox.configure(state=NORMAL)
        self.textBox.insert(END, f"You: What`s the best move for this board : {fen}\n")
        stockfish = sf.Stockfish(engine_path=self.engine_path)
        stockfish.setup(fen)
        explainer = sf.StockfishExplainer(stockfish)
        explain = explainer.explain()
        self.textBox.configure(state=NORMAL)
        self.textBox.insert(END, "Chatbot: ")
        self.textBox.insert(END, explain)
        self.textBox.insert(END, "\n\n")
        self.textBox.configure(state=DISABLED)
