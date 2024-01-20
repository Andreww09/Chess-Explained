import chess
import chess.engine


class Stockfish:
    """
    Class used to interact with Stockfish engine

    """

    def __init__(self, engine_path):
        """
        Constructor for Stockfish class
        Initializes board and engine path.

        :param engine_path: path to Stockfish engine on personal computer
        """

        self.engine_path = engine_path
        self.board = chess.Board()

    def make_move(self, move):
        """
        Make a move on the current board

        :param move: move to be made
        :return: True if move is valid, False otherwise
        """

        try:
            # make the move on the board
            self.board.push_san(move)
            return True
        except ValueError:
            print(f"Invalid move: {move}")
            return False

    def get_best_move(self, time_limit=2.0):
        """
        Get the best move for the current board

        :param time_limit: time limit for the engine to find the best move. Default is 2 seconds
        :return: best move for the current board
        """

        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
            # get the best move for the current board
            result = engine.play(self.board, chess.engine.Limit(time=time_limit))

            # convert the move to SAN notation and return it
            return self.board.san(result.move)

    def get_best_move_sequence(self, num_moves, time_limit=2.0):
        """
        Get the best sequence of moves for the current board

        :param num_moves: Number of moves to be returned
        :param time_limit: time limit for the engine to find the best move. Default is 2 seconds
        :return: best sequence of moves for the current board
        """

        # initialize the sequence of moves
        sequence = []

        # make a copy of the board, so we don't modify the original board
        temp_board = self.board.copy()

        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
            for _ in range(num_moves):
                # get the best move for the current board
                result = engine.play(temp_board, chess.engine.Limit(time=time_limit))

                # convert the move to SAN notation
                move = temp_board.san(result.move)

                # add the move to the sequence
                sequence.append(move)

                # make the move on the board
                temp_board.push(result.move)

        # return the sequence of moves
        return sequence

    def setup_game(self, fen):
        """
        Set the board to the given FEN

        :param fen: FEN to set the board to
        :return: True if FEN is valid, False otherwise
        """

        try:
            # set the board to the given FEN
            self.board.set_fen(fen)
            return True
        except ValueError:
            print(f"Invalid FEN: {fen}")
            return False

    def display_board(self):
        """
        Display the current board

        :return: None
        """
        print(self.board)

    def undo_move(self):
        """
        Undo the last move made on the board

        :return: True if move was undone, False otherwise
        """

        if len(self.board.move_stack) > 0:
            self.board.pop()
            return True
        return False

    def evaluate_board(self):
        """
        Evaluate the current board

        :return: evaluation of the current board
        """
        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
            info = engine.analyse(self.board, chess.engine.Limit(time=0.1))
            return info["score"]

    def game_status(self):
        """
        Check the status of the game

        :return: status of the game (checkmate, stalemate, draw, game ongoing)
        """

        if self.board.is_checkmate():
            return "Checkmate"
        elif self.board.is_stalemate():
            return "Stalemate"
        elif self.board.is_insufficient_material():
            return "Draw due to insufficient material"
        return "Game ongoing"

    def list_legal_moves(self):
        """
        List all legal moves for the current board

        :return: list of legal moves for the current board
        """

        return [self.board.san(move) for move in self.board.legal_moves]

    def list_attacked_pieces(self):
        """
        List squares of pieces that are under attack by the opponent of the current player

        :return: List of squares as strings
        """

        attacked_pieces = []
        opponent_color = not self.board.turn
        for square in chess.SQUARES:
            if self.board.piece_at(square) and self.board.color_at(square) == self.board.turn:
                if self.board.is_attacked_by(opponent_color, square):
                    attacked_pieces.append(chess.square_name(square))
        return attacked_pieces

    def list_all_captures(self):
        """
        List all possible captures for the current player.

        :return: List of capture moves in SAN
        """
        return [self.board.san(move) for move in self.board.generate_legal_captures() if
                self.board.color_at(move.from_square) == self.board.turn]

    def current_player_color(self):
        """
        Get the color of the current player

        :return: 'White' or 'Black'
        """
        return "White" if self.board.turn == chess.WHITE else "Black"

    def get_index_from_san(self, move_san):
        move = move_san.replace("+", "")
        return chess.parse_square(move[-2:])

    def get_piece_at_index(self, index):
        return self.board.piece_at(index)

    def get_attackers_at(self, color, poz):

        attackers = self.board.attackers(color, poz)
        return attackers
