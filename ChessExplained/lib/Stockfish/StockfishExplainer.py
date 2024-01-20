from lib.utils import BoardUtils
import chess
import chess.engine


class StockfishExplainer:
    """
    Class used to provide explanations for moves suggested by Stockfish
    """

    def __init__(self, stockfish):
        """
        Constructor for StockfishExplainer class.

        :param stockfish: Instance of Stockfish class
        """
        self.stockfish = stockfish
        self.piece_value = {
            'K': 10,
            'Q': 9,
            'R': 5,
            'B': 3,
            'N': 3,
            'P': 1,
        }

    def explain(self):
        """
        Explain the next best move.

        :return: Explanation as a string
        """
        best_move = self.stockfish.best_move()
        explanation = f"The best move is {best_move}. "

        is_fork = self._is_fork(best_move)
        is_capture = self.stockfish.is_capture(best_move)
        is_checkmate = self._is_checkmate(best_move)
        is_en_passant = self.stockfish.is_en_passant(best_move)
        is_stalemate = self._is_stalemate(best_move)
        is_insufficient_material = self._is_insufficient_material(best_move)
        is_battery = self._is_battery(best_move)
        is_sacrifice = self._is_sacrifice(best_move)

        print("is_fork: ", is_fork)
        print("is_checkmate: ", is_checkmate)
        print("is_capture: ", is_capture)
        print("is_en_passant: ", is_en_passant)
        print("is_stalemate: ", is_stalemate)
        print("is_insufficient_material: ", is_insufficient_material)
        print("is_battery: ", is_battery)
        print("is_sacrifice: ", is_sacrifice)

        return explanation

    def _is_fork(self, move_san):
        """
        Determine if the move results in a fork

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a fork, False otherwise
        """

        # get (start, end) square of the move
        start_end_move = self.stockfish.start_end_from_san(move_san)

        # check that piece is not a pawn
        if self.stockfish.piece_at_san(start_end_move[0]) == 'P':
            return False

        # initialize the valuable pieces count
        valuable_pieces_count = 0

        # make the move
        self.stockfish.move(move_san)

        # print board
        self.stockfish.display()

        # get all captures by the moved piece
        captures = self.stockfish.capture_pieces_by_san(start_end_move[1])

        # loop through all captures
        for capture in captures:
            # get captured piece
            captured_piece = capture[0]

            if captured_piece in ['K', 'Q', 'R', 'B', 'N']:
                valuable_pieces_count += 1

        # undo the move
        self.stockfish.undo()

        return valuable_pieces_count >= 2

    def _is_checkmate(self, move_san):
        """
        Determine if the move results in a checkmate.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a checkmate, False otherwise
        """
        self.stockfish.move(move_san)
        is_checkmate = self.stockfish.board.is_checkmate()
        self.stockfish.undo()
        return is_checkmate

    def _is_battery(self, move_san):
        """
        Determine if the move results in a battery.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a battery, False otherwise
        """
        # Get the index of the moved piece
        move_index = chess.parse_square(self.stockfish.start_end_from_san(move_san)[1])

        self.stockfish.move(move_san)

        # Get the moved piece
        move_piece = self.stockfish.board.piece_at(move_index)

        # Get the pieces that are attacking the moved piece (the same color as the moved piece)
        self.stockfish.switch_turn()
        attackers = BoardUtils.get_attackers_at_square(self.stockfish.board, move_index)
        self.stockfish.switch_turn()

        is_battery = False

        # Check if there is a battery
        for attacker in attackers:
            # Get the piece that is attacking the moved piece
            attacker_piece = self.stockfish.board.piece_at(attacker)

            # Check if the attacker piece attacks on the same direction as the moved piece
            if BoardUtils.is_battery_compatible(move_piece, attacker_piece):
                is_battery = True
                break

        # Undo the move
        self.stockfish.undo()

        return is_battery

    def _is_sacrifice(self, move_san):

        start_end_move = self.stockfish.start_end_from_san(move_san)

        # type of the piece that was captured
        index = self.stockfish.index_from_san(start_end_move[1])
        old_piece = self.stockfish.piece_at_index(index)

        self.stockfish.move(move_san)
        # type of the piece that was moved
        new_piece = str(self.stockfish.piece_at_index(index)).upper()
        # all the squares (as integers) that attack the moved piece
        attackers = self.stockfish.get_attackers_at(self.stockfish.board.turn, index)
        # all the squares that protect the moved piece
        protectors = self.stockfish.get_attackers_at(not self.stockfish.board.turn, index)

        # undo the move
        self.stockfish.undo()

        # the piece was moved to a square that is under attack and there are no protectors
        if old_piece is None:
            if len(attackers) > 0 and len(protectors) == 0:
                return True
            else:
                # the piece is protected but is attacked and can be taken by a weaker piece
                for attacker in attackers:
                    piece = str(self.stockfish.piece_at_index(attacker)).upper()
                    if self.piece_value[piece] < self.piece_value[new_piece]:
                        return True
                return False
        old_piece = str(old_piece).upper()

        # the piece was traded for a lower value piece
        if self.piece_value[old_piece] < self.piece_value[new_piece]:
            return True

        return False

    def _is_stalemate(self, move_san):
        """
        Determine if the move results in a stalemate.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a stalemate, False otherwise
        """
        self.stockfish.move(move_san)
        is_stalemate = self.stockfish.board.is_stalemate()
        self.stockfish.undo()
        return is_stalemate

    def _is_insufficient_material(self, move_san):
        """
        Determine if the move results in a stalemate.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a stalemate, False otherwise
        """
        self.stockfish.move(move_san)
        is_insufficient_material = self.stockfish.board.is_insufficient_material()
        self.stockfish.undo()
        return is_insufficient_material
