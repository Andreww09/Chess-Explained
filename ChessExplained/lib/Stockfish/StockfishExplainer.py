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
        best_move = self.stockfish.get_best_move()
        explanation = f"The best move is {best_move}. "

        is_pin = self._is_move_a_pin(best_move)
        is_fork = self._is_move_a_fork(best_move)
        is_sacrifice = self._is_move_a_sacrifice(best_move)

        print("is_pin:", is_pin)
        print("is_fork:", is_fork)
        print("is_sacrifice:", is_sacrifice)

        if is_pin:
            explanation += "This move pins an opponent's piece. "
        if is_fork:
            explanation += "This move forks two of the opponent's pieces. "

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
        self.stockfish.board.turn = not self.stockfish.board.turn

        # get all captures
        captures = self.stockfish.list_all_captures()

        # change the turn back
        self.stockfish.board.turn = not self.stockfish.board.turn

        # undo the move
        self.stockfish.board.pop()

        # check captures for 2 valuable pieces
        num_valuable_pieces = 0
        for capture in captures:
            if capture[0] == "Q" or capture[0] == "R" or capture[0] == "B" or capture[0] == "N" or capture[0] == "K":
                num_valuable_pieces += 1

        return num_valuable_pieces >= 2

    def _is_move_a_sacrifice(self, move_san):
        # type of the piece that was captured
        old_piece = self.stockfish.get_piece_at_san(move_san)

        self.stockfish.make_move(move_san)
        print(move_san)
        # type of the piece that was moved
        new_piece = str(self.stockfish.get_piece_at_san(move_san)).upper()
        # all the squares (as integers) that attack the moved piece
        attackers = self.stockfish.get_attackers_at(self.stockfish.board.turn, move_san)
        # all the squares that protect the moved piece
        protectors = self.stockfish.get_attackers_at(not self.stockfish.board.turn, move_san)

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
