import chess
import chess.engine
from lib.utils import BoardUtils


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

        print("is_pin: ", is_pin)
        print("is_fork: ", is_fork)
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

        # get all captures
        captures = self.stockfish.list_all_captures()

        # change the turn back
        self.stockfish.change_turn()

        # undo the move
        self.stockfish.board.pop()

        # check captures for 2 valuable pieces
        num_valuable_pieces = 0
        for capture in captures:
            if capture[0] == "Q" or capture[0] == "R" or capture[0] == "B" or capture[0] == "N" or capture[0] == "K":
                num_valuable_pieces += 1

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
