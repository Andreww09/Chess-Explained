import customtkinter
from front.chessboard import Square


class Board(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.squares = []
        self.create_squares()

    def create_squares(self):
        """
        Create the squares of the chess board.
        """
        for row in range(8):
            for col in range(8):
                square_color = "white" if (row + col) % 2 == 0 else "gray"
                square = Square(self, square_color)
                square.grid(row=row, column=col, sticky="nsew")
                self.squares.append(square)
