import time

import customtkinter

from front.chessboard import Square
from front.chessboard import Piece


class Board(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.squares = []
        self.create_squares()
        self.menu = None

    def add_menu(self, menu):
        self.menu = menu

    def set_new_game(self):
        self.squares = self.initial_board()
        self.print_board()

    '''def update_board(self, initial_index, final_index):
        initial_square = self.squares[initial_index]
        final_square = self.squares[final_index]
        initial_piece = initial_square.piece
        final_piece = final_square.piece
        
        initial_square.place_piece(final_piece)
        # print(self.squares[0].piece.get_image())
        if initial_square.piece is not None:
            initial_square_image = customtkinter.CTkLabel(master=self, image=initial_square.piece, text="")
            initial_square_image.grid(row=initial_index // 8, column=initial_index % 8,
                                      sticky="nsew")
        
        final_square.place_piece(initial_piece)
        # print(self.squares[0].piece.get_image())
        if final_square.piece is not None:
            final_square_image = customtkinter.CTkLabel(master=self, image=final_square.piece, text="")
            final_square_image.grid(row=final_index // 8, column=final_index % 8,
                                    sticky="nsew")
        
        #  era mult mai eficient sa le schimb doar pe cele 2 imagini, dar problema e ca daca am o piesa null, nu
        #  o pot afisa -> printez toata tabla din nou, se misca rapid oricum
        self.print_board()
    '''
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
                index += 1

        color = not color
        for rank in range(6, 8):
            for file in range(8):
                index_square = self.calculate_index_square(rank, file)
                square = self.squares[index_square]
                piece = Piece(color=color, piece_type=pieces_types[index], position=(rank, file))
                square.place_piece(piece)
                index += 1

        #  self.update_board(10, 60)
        return self.squares

    def print_board(self):
        for square in self.squares:
            if square.piece is not None:
                piece_image = customtkinter.CTkLabel(master=self, image=square.piece, text="")
                piece_image.grid(row=square.rank, column=square.file,
                                 sticky="nsew")

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
