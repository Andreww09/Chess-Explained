import customtkinter
from customtkinter import *
from PIL import ImageTk, Image
from chatterbot import ChatBot
import back.stockfish_tools as sf
from back.utils import BoardUtils


class App(CTk):

    def __init__(self, engine_path, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.engine_path = engine_path
        self.title("Chess Explained")
        self.geometry("700x800")
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

        self.img = ImageTk.PhotoImage(Image.open("front/assets/label.png"))
        self.label = CTkLabel(master=self, width=680, height=90, image=self.img, text="")
        self.label.place(x=10, y=10)

        self.entryBox = CTkTextbox(master=self, width=600, height=100)
        self.entryBox.place(x=10, y=690)
        self.entryBox.focus()

        self.button1 = CTkButton(master=self, width=75, height=45, text="Send",
                                 command=lambda: self._on_enter_pressed())
        self.button1.place(x=615, y=690)

        self.button2 = CTkButton(master=self, width=75, height=45, text="Best Move", command=lambda: self.input())
        self.button2.place(x=615, y=745)

        self.best_move_label = CTkLabel(self.master, text="")

        self.textBox = CTkTextbox(master=self, width=680, height=550)
        self.textBox.place(x=10, y=110)
        self.textBox.configure(state=DISABLED)

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
