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

        # Make the move
        self.stockfish.move(best_move)

        # print board
        self.stockfish.display()

        # Undo the move
        self.stockfish.undo()

        is_pin = self._is_pin(best_move)
        is_fork = self._is_fork(best_move)
        is_capture = self.stockfish.is_capture(best_move)
        is_check = self._is_check(best_move)
        is_checkmate = self._is_checkmate(best_move)
        is_en_passant = self.stockfish.is_en_passant(best_move)
        is_stalemate = self._is_stalemate(best_move)
        is_insufficient_material = self._is_insufficient_material(best_move)
        is_battery = self._is_battery(best_move)
        is_sacrifice = self._is_sacrifice(best_move)
        is_discovered_attack = self._is_a_discovered_attack(best_move)
        is_castling = self._is_a_castling(best_move)
        is_pawn_promotion = self._is_pawn_promotion(best_move)

        print("is_pin: ", is_pin)
        print("is_fork: ", is_fork)
        print("is_check: ", is_check)
        print("is_checkmate: ", is_checkmate)
        print("is_check_forced: ", self._is_move_check_forced())
        print("is_capture: ", is_capture)
        print("is_en_passant: ", is_en_passant)
        print("is_stalemate: ", is_stalemate)
        print("is_insufficient_material: ", is_insufficient_material)
        print("is_battery: ", is_battery)
        print("is_sacrifice: ", is_sacrifice)
        print("is_discovered_attack: ", is_discovered_attack)
        print("is_castling: ", is_castling)
        print("is_pawn_promotion: ", is_pawn_promotion)

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

    def _is_a_discovered_attack(self, move_san):
        """
            Determine if the move results in a discovered attack.

            :param move_san: Move in standard algebraic notation
            :return: True if the move results in a discovered attack, False otherwise
        """

        from_square = self.stockfish.board.parse_san(move_san).from_square
        to_square = self.stockfish.board.parse_san(move_san).to_square

        squares_before_move = self.stockfish.captures_except_square_allowing_duplicates(from_square)

        self.stockfish.move(move_san)
        self.stockfish.board.turn = not self.stockfish.board.turn

        squares_after_move = self.stockfish.captures_except_square_allowing_duplicates(to_square)

        self.stockfish.undo()

        for attacked_square in squares_after_move:
            if squares_after_move.count(attacked_square) > squares_before_move.count(attacked_square):
                return True
        return False

    def _is_a_castling(self, move_san):
        return self.stockfish.board.is_castling(self.stockfish.board.parse_san(move_san))

    def _is_pawn_promotion(self, move_san):
        from_square = self.stockfish.board.parse_san(move_san).from_square
        to_square = self.stockfish.board.parse_san(move_san).to_square
        if self.stockfish.board.piece_at(from_square).piece_type == 1:
            self.stockfish.move(move_san)
            if self.stockfish.board.piece_at(to_square).piece_type != 1:
                self.stockfish.undo()
                return True
            self.stockfish.undo()
        return False

    def _is_en_passant(self, move_san):
        return self.stockfish.is_en_passant(move_san)

    def _is_capture(self, move_san):
        return self.stockfish.is_capture(move_san)

    def _is_check(self, move_san):
        """
        Determine if the move results in a check.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a check, False otherwise
        """

        self.stockfish.move(move_san)
        is_check = self.stockfish.board.is_check()
        self.stockfish.undo()

        return is_check

    def _is_move_check_forced(self):
        """
        Determine if the move is forced by a check.

        :return: True if the move is forced by a check, False otherwise
        """

        is_check = self.stockfish.board.is_check()
        is_checkmate = self.stockfish.board.is_checkmate()

        return is_check and not is_checkmate

    def _is_pin(self, move_san):
        """
        Determine if the move results in a pin.

        :param move_san: Move in standard algebraic notation
        :return: True if the move results in a pin, False otherwise
        """
        # Get the square name of the moved piece
        moved_square = self.stockfish.start_end_from_san(move_san)[1]

        # Make the move
        self.stockfish.move(move_san)

        # Get the piece that is moved
        moved_piece = self.stockfish.piece_at_san(moved_square)

        # Check if the moved piece is a pawn, knight or king
        if moved_piece == 'P' or moved_piece == 'N' or moved_piece == 'K':
            # Undo the move
            self.stockfish.undo()

            # Return False if the moved piece is a pawn, knight or king
            return False

        # Get all the pieces that are attacked by the moved piece
        attacked_pieces = set(self.stockfish.captures_by(moved_square))

        # Make backup of board
        board_backup = self.stockfish.board.copy()

        for attacked_piece_square in attacked_pieces:
            # Convert the attacked piece to a chess.Piece object
            attacked_piece = self.stockfish.piece_at_san(attacked_piece_square)

            # Remove the attacked piece from the board
            self.stockfish.board.remove_piece_at(self.stockfish.index_from_san(attacked_piece_square))

            # Get all the pieces that are attacked by the moved piece after the attacked piece is removed
            attacked_pieces_after = set(self.stockfish.captures_by(moved_square))

            # Add the attacked piece back to the board
            self.stockfish.add_piece_at(chess.Piece(attacked_piece.piece_type, self.stockfish.board.turn),
                                        self.stockfish.index_from_san(attacked_piece_square))

            # Check if another piece is attacked by the moved piece after the attacked piece is removed
            if len(attacked_pieces_after) > 0:
                # Get the other attacked piece from behind the removed attacked piece
                other_attacked_pieces = attacked_pieces_after.difference(attacked_pieces)

                # Get the first other attacked piece
                if len(other_attacked_pieces) > 0:
                    other_attacked_piece = other_attacked_pieces.pop()
                else:
                    continue

                # Convert the other attacked piece to a chess.Piece object
                other_attacked_piece = self.stockfish.piece_at_san(other_attacked_piece)

                # Check if there is a pin
                if BoardUtils.is_pin_compatible(moved_piece, attacked_piece, other_attacked_piece):
                    # Restore the board
                    self.stockfish.board = board_backup

                    # Undo the move
                    self.stockfish.undo()

                    # Return True if there is a pin
                    return True

        # Restore the board
        self.stockfish.board = board_backup

        # Undo the move
        self.stockfish.undo()

        # Return False if there is no pin
        return False
