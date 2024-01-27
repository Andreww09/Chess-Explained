import customtkinter

from front.chessboard import Square
from front.chessboard import Piece


class Board(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.squares = []
        self.create_squares()
        self.menu = None
        self.new_game = False

    def add_menu(self, menu):
        self.menu = menu

    def set_new_game(self):
        print("New Game")
        self.new_game = True
        self.initial_board()

    def calculate_index_square(self, rank, file):
        linear_index = rank * 8 + file
        return linear_index

    def initial_board(self):
        pieces_types = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
                        'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
                        'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
                        'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        color = False
        index = 0
        for rank in range(0, 2):
            for file in range(8):
                index_square = self.calculate_index_square(rank, file)
                square = self.squares[index_square]
                piece = Piece(color=color, piece_type=pieces_types[index], position=(rank, file))
                square.place_piece(piece)
                # print(self.squares[0].piece.get_image())
                piece_image = customtkinter.CTkLabel(master=self, image=piece, text="")
                piece_image.grid(row=rank, column=file,
                                 sticky="nsew")
                index += 1

        color = not color
        for rank in range(6, 8):
            for file in range(8):
                index_square = self.calculate_index_square(rank, file)
                square = self.squares[index_square]
                piece = Piece(color=color, piece_type=pieces_types[index], position=(rank, file))
                square.place_piece(piece)
                # print(self.squares[0].piece.get_image())
                piece_image = customtkinter.CTkLabel(master=self, image=piece, text="")
                piece_image.grid(row=rank, column=file,
                                 sticky="nsew")
                index += 1

    def create_squares(self):
        """
        Create the squares of the chess board.
        """
        for rank in range(8):
            for file in range(8):
                square_color = "white" if (rank + file) % 2 == 0 else "gray"
                # file = chr(ord('a') + file)
                square = Square(self, 60, 60, square_color, file, rank)
                square.grid(row=rank, column=file, sticky="nsew")

                self.squares.append(square)
