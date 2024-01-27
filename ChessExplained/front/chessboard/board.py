import customtkinter

from front.chessboard import Square
from front.chessboard import Piece
import chess


class Board(customtkinter.CTkFrame):

    def __init__(self, master, stockfish, **kwargs):
        super().__init__(master, **kwargs)

        self.squares = []
        self.create_squares()
        self.menu = None
        self.stockfish = stockfish

    def create_squares(self):
        """
        Create the squares of the chess board.
        """
        for rank in range(8):
            squares_file = []
            for file in range(8):
                square_color = "white" if (rank + file) % 2 == 0 else "gray"

                square = Square(self, 60, 60, square_color, file, rank)
                square.grid(row=rank, column=file, sticky="nsew")

                squares_file.append(square)
            self.squares.append(squares_file)

    def load_from_fen(self, fen):
        """
        Load the board from a fen.
        :param fen:
        :return:
        """
        # Clean the board
        self.clean_board()

        # Set up the board with the fen
        self.stockfish.setup(fen)

        for piece, square_rank, square_file in self.stockfish.get_occupied_squares():
            # Get the piece type and color
            piece_color = piece.color
            piece_type = piece.symbol()

            # Get the square
            square = self.squares[7 - square_rank][square_file]

            # Place the piece on the square
            piece = Piece(color=piece_color, piece_type=piece_type, position=(square_rank, square_file))
            square.place_piece(piece)
        self.print_board()

    def initial_board(self):
        """
        Create the initial board.

        """
        starting_fen = chess.STARTING_FEN
        self.load_from_fen(starting_fen)

    def add_menu(self, menu):
        self.menu = menu

    def clean_board(self):
        """
        Clean the board.
        """
        for piece, square_rank, square_file in self.stockfish.get_occupied_squares():
            # Get the square
            square = self.squares[7 - square_rank][square_file]

            # Delete the piece on the square
            square.place_piece(None)
            for widget in square.winfo_children():
                widget.destroy()

    def print_board(self):
        for squares_file in self.squares:
            for square in squares_file:
                if square.piece is not None:
                    piece_image = customtkinter.CTkLabel(master=square, image=square.piece, text="")
                    piece_image.grid(row=square.rank, column=square.file,
                                     sticky="nsew")
