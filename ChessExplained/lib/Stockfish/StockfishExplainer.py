from lib.utils import BoardUtils
import chess


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
        best_move = self.stockfish.get_best_move()
        explanation = f"The best move is {best_move}. "

        is_pin = self._is_move_a_pin(best_move)
        is_fork = self._is_move_a_fork(best_move)
        is_battery = self._is_move_a_battery(best_move)
        is_sacrifice = self._is_move_a_sacrifice(best_move)

        print("is_pin: ", is_pin)
        print("is_fork: ", is_fork)
        print("is_sacrifice:", is_sacrifice)
        print("is_battery: ", is_battery)

        if is_pin:
            explanation += "This move pins an opponent's piece. "
        if is_fork:
            explanation += "This move forks two of the opponent's pieces. "
        if is_battery:
            explanation += "This move creates a battery. "

        return explanation

    def _is_move_a_pin(self, move_san):
        """
        Determine if the move results in a pin

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a pin, False otherwise
        """
        return False

    def _is_move_a_fork(self, move_san):
        """
        Determine if the move results in a fork.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a fork, False otherwise
        """

        self.stockfish.make_move(move_san)

        # print board
        self.stockfish.display_board()

        # change the turn
        self.stockfish.change_turn()

        # get piece moved
        index = self.stockfish.get_index_from_san(move_san)

        # get all captures
        captures = self.stockfish.list_pieces_attacked_by(index)

        print("Captures: ", captures)

        # change the turn back
        self.stockfish.change_turn()

        # undo the move
        self.stockfish.board.pop()

        # check captures for 2 valuable pieces
        num_valuable_pieces = 0
        for capture in captures:
            # get piece type from position
            piece = self.stockfish.get_piece_at_position(capture)

            piece_string = str(piece).upper()

            # check if piece is valuable
            if piece_string in ['Q', 'R', 'B', 'N', 'K']:
                num_valuable_pieces += 1

        print("Num valuable pieces: ", num_valuable_pieces)
        return num_valuable_pieces >= 2

    def _is_move_a_battery(self, move_san):
        """
        Determine if the move results in a battery.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a battery, False otherwise
        """
        self.stockfish.make_move(move_san)

        # Check if there is a battery after the move
        is_battery = False

        move_index = BoardUtils.get_index_from_san(move_san)
        move_piece = self.stockfish.board.piece_at(move_index)

        # Get the pieces that are attacking the moved piece (the same color as the moved piece)
        self.stockfish.change_turn()
        attackers = BoardUtils.get_attackers_at_square(self.stockfish.board, move_index)
        self.stockfish.change_turn()

        # Check if there is a battery
        for attacker in attackers:
            # Get the piece that is attacking the moved piece
            attacker_piece = self.stockfish.board.piece_at(attacker)

            # Check if the attacker piece attacks on the same direction as the moved piece
            if BoardUtils.is_battery_compatible(move_piece, attacker_piece):
                is_battery = True
                break

        # Undo the move
        self.stockfish.undo_move()

        return is_battery

    def _is_move_a_sacrifice(self, move_san):
        # type of the piece that was captured
        index = self.stockfish.get_index_from_san(move_san)
        old_piece = self.stockfish.get_piece_at_index(index)

        self.stockfish.make_move(move_san)
        # type of the piece that was moved
        new_piece = str(self.stockfish.get_piece_at_index(index)).upper()
        # all the squares (as integers) that attack the moved piece
        attackers = self.stockfish.get_attackers_at(self.stockfish.board.turn, index)
        # all the squares that protect the moved piece
        protectors = self.stockfish.get_attackers_at(not self.stockfish.board.turn, index)

        # undo the move
        self.stockfish.board.pop()

        # the piece was moved to a square that is under attack and there are no protectors
        if old_piece is None:
            if len(attackers) > 0 and len(protectors) == 0:
                return True
            else:
                # the piece is protected but is attacked and can be taken by a weaker piece
                for attacker in attackers:
                    piece = str(self.stockfish.get_piece_at_index(attacker)).upper()
                    if self.piece_value[piece] < self.piece_value[new_piece]:
                        return True
                return False

        old_piece = str(old_piece).upper()

        # the piece was traded for a lower value piece
        if self.piece_value[old_piece] < self.piece_value[new_piece]:
            return True

        return False
