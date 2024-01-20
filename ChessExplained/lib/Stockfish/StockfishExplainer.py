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
        is_discovered_attack = self._is_a_discovered_attack(best_move)
        is_castling = self._is_a_castling(best_move)
        is_pawn_promotion = self._is_pawn_promotion(best_move)
        is_skewer = self._is_skewer(best_move)
        is_forced_checkmate = self._is_forced_checkmate(best_move)
        is_polish_opening = self._is_polish_opening(best_move)
        is_nimzowitsch_larsen_attack = self._is_nimzowitsch_larsen_attack(best_move)
        is_kings_indian = self._is_kings_indian(best_move)
        is_birds_opening = self._is_birds_opening(best_move)
        is_english_opening = self._is_english_opening(best_move)
        is_alekhine_defense = self._is_alekhine_defense(best_move)
        is_benko_gambit = self._is_benko_gambit(best_move)
        is_benoni_defense = self._is_benoni_defense(best_move)
        is_bogo_indian_defense = self._is_bogo_indian_defense(best_move)
        is_caro_kann_defense = self._is_caro_kann_defense(best_move)
        is_catalan_opening = self._is_catalan_opening(best_move)
        is_vienna_game = self._is_vienna_game(best_move)
        is_trompowsky_attack = self._is_trompowsky_attack(best_move)
        is_slav_defense = self._is_slav_defense(best_move)
        is_sicilian_defense = self._is_sicilian_defense(best_move)
        is_scotch_game = self._is_scotch_game(best_move)
        is_scandinavian_defense = self._is_scandinavian_defense(best_move)
        is_ruy_lopez_opening = self._is_ruy_lopez_opening(best_move)
        is_reti_opening = self._is_reti_opening(best_move)
        is_queens_indian_defense = self._is_queens_indian_defense(best_move)
        is_pirc_defense = self._is_pirc_defense(best_move)
        is_queens_gambit = self._is_queens_gambit(best_move)
        is_nimzo_indian_defense = self._is_nimzo_indian_defense(best_move)
        is_london_system = self._is_london_system(best_move)
        is_kings_gambit = self._is_kings_gambit(best_move)
        is_kings_fianchetto_opening = self._is_kings_fianchetto_opening(best_move)
        is_king_indian_defense = self._is_king_indian_defense(best_move)
        is_dutch_defense = self._is_dutch_defense(best_move)
        is_french_defense = self._is_french_defense(best_move)
        is_italian_game = self._is_italian_game(best_move)
        is_grunfeld_defense = self._is_grunfeld_defense(best_move)
        is_grob_opening = self._is_grob_opening(best_move)

        print("is_fork: ", is_fork)
        print("is_checkmate: ", is_checkmate)
        print("is_capture: ", is_capture)
        print("is_en_passant: ", is_en_passant)
        print("is_stalemate: ", is_stalemate)
        print("is_insufficient_material: ", is_insufficient_material)
        print("is_battery: ", is_battery)
        print("is_sacrifice: ", is_sacrifice)
        print("is_discovered_attack: ", is_discovered_attack)
        print("is_castling: ", is_castling)
        print("is_pawn_promotion: ", is_pawn_promotion)
        print("is_skewer: ", is_skewer)
        print("is_forced_checkmate: ", is_forced_checkmate)
        print("is_polish_opening: ", is_polish_opening)
        print("is_nimzowitsch_larsen_attack: ", is_nimzowitsch_larsen_attack)
        print("is_kings_indian: ", is_kings_indian)
        print("is_birds_opening: ", is_birds_opening)
        print("is_english_opening: ", is_english_opening)
        print("is_alekhine_defense: ", is_alekhine_defense)
        print("is_benko_gambit: ", is_benko_gambit)
        print("is_benoni_defense: ", is_benoni_defense)
        print("is_bogo_indian_defense: ", is_bogo_indian_defense)
        print("is_caro_kann_defense: ", is_caro_kann_defense)
        print("is_catalan_opening: ", is_catalan_opening)
        print("is_vienna_game: ", is_vienna_game)
        print("is_trompowsky_attack: ", is_trompowsky_attack)
        print("is_slav_defense: ", is_slav_defense)
        print("is_sicilian_defense: ", is_sicilian_defense)
        print("is_scotch_game: ", is_scotch_game)
        print("is_scandinavian_defense: ", is_scandinavian_defense)
        print("is_ruy_lopez_opening: ", is_ruy_lopez_opening)
        print("is_reti_opening: ", is_reti_opening)
        print("is_queens_indian_defense: ", is_queens_indian_defense)
        print("is_pirc_defense: ", is_pirc_defense)
        print("is_queens_gambit: ", is_queens_gambit)
        print("is_nimzo_indian_defense: ", is_nimzo_indian_defense)
        print("is_london_system: ", is_london_system)
        print("is_kings_gambit: ", is_kings_gambit)
        print("is_kings_fianchetto_opening: ", is_kings_fianchetto_opening)
        print("is_king_indian_defense: ", is_king_indian_defense)
        print("is_dutch_defense: ", is_dutch_defense)
        print("is_french_defense: ", is_french_defense)
        print("is_italian_game: ", is_italian_game)
        print("is_grunfeld_defense: ", is_grunfeld_defense)
        print("is_grob_opening: ", is_grob_opening)

        print("---------------------------------------------------")
        advantage_color, probability = self._calculate_winning_prob()

        print("Player that has advantage: " + str(advantage_color))
        print("Winning probability: " + str(probability * 100) + "%")

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
        old_piece = self.stockfish.board.piece_at(index)

        self.stockfish.move(move_san)
        # type of the piece that was moved
        new_piece = BoardUtils.piece_at_index_str(self.stockfish.board, index)
        # all the squares (as integers) that attack the moved piece
        attackers = BoardUtils.get_attackers_at_index(self.stockfish.board, self.stockfish.board.turn, index)
        # all the squares that protect the moved piece
        protectors = BoardUtils.get_attackers_at_index(self.stockfish.board, not self.stockfish.board.turn, index)

        # undo the move
        self.stockfish.undo()

        # the piece was moved to a square that is under attack and there are no protectors
        if old_piece is None:
            if len(attackers) > 0 and len(protectors) == 0:
                return True
            else:
                # the piece is protected but is attacked and can be taken by a weaker piece
                for attacker in attackers:
                    piece = BoardUtils.piece_at_index_str(self.stockfish.board, attacker)
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
        '''
            Determine if the move results in a discovered attack.

            :param move_san: Move in standard algebraic notation
            :return: True if the move results in a discovered attack, False otherwise
        '''

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
        if self.stockfish.piece_at_index(from_square).piece_type == 1:
            self.stockfish.move(move_san)
            if self.stockfish.piece_at_index(to_square).piece_type != 1:
                self.stockfish.undo()
                return True
            self.stockfish.undo()
        return False

    def _is_skewer(self, move_san):

        start_end_move = self.stockfish.start_end_from_san(move_san)

        # index of best move
        index = self.stockfish.index_from_san(start_end_move[1])

        self.stockfish.move(move_san)

        # all the squares attacked be the moved piece
        previously_attacked_pieces = self.stockfish.board.attacks(index)

        # a skewer requires two extra moves for completion
        best_moves = self.stockfish.best_move_sequence(2)

        if len(best_moves) < 2:
            self.stockfish.undo()
            return False

        # indexes for the starting and ending position of the first move in the sequence
        start_first_move, end_first_move = self.stockfish.start_end_from_san(best_moves[0])
        start_first_move = self.stockfish.index_from_san(start_first_move)
        end_first_move = self.stockfish.index_from_san(end_first_move)

        # type of the attacked and attacking piece to be compared
        attacked_piece = BoardUtils.piece_at_index_str(self.stockfish.board, start_first_move)
        attacking_piece = BoardUtils.piece_at_index_str(self.stockfish.board, index)

        # get all the attacked squares after the opponent played an optimal move
        self.stockfish.move(best_moves[0])
        attacked_pieces = self.stockfish.board.attacks(index)

        # indexes for the second move in the sequence
        start_second_move, end_second_move = self.stockfish.start_end_from_san(best_moves[1])
        start_second_move = self.stockfish.index_from_san(start_second_move)
        end_second_move = self.stockfish.index_from_san(end_second_move)

        # undo the moves
        self.stockfish.undo()
        self.stockfish.undo()

        # a skewer requires to attack a higher value piece
        if self.piece_value[attacking_piece] >= self.piece_value[attacked_piece]:
            return False

        # the opponent move must move an attacked piece to be a skewer
        if start_first_move not in previously_attacked_pieces:
            return False

        # the opponent must take the higher piece to safety
        if end_first_move in attacked_pieces:
            return False

        # the attacking piece must capture a piece in the next move that was defended previously
        if start_second_move == index and end_second_move not in previously_attacked_pieces and "x" in best_moves[1]:
            return True

        return False

    def _is_forced_checkmate(self, move_san):
        self.stockfish.move(move_san)
        eval_first_item = self.stockfish.first_item_evaluation()
        self.stockfish.undo()

        return eval_first_item[0] == 'M'

    def _calculate_winning_prob(self):
        eval_first_item = self.stockfish.first_item_evaluation()
        score_cp = self.stockfish.get_evaluation_score(eval_first_item)
        color = self.stockfish.get_color_eval_score(eval_first_item)
        probability = self.stockfish.winning_probability(score_cp)

        return color, probability

    def _is_sicilian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_french_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/3P4/8/PPP2PPP/R1BQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_ruy_lopez_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/8/3Pp3/5N2/PPP2PPP/R1BQKB1R w KQkq - 0 6"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_caro_kann_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp2pppp/2p5/3p4/3P4/8/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_italian_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/R1BQKB1R w KQkq - 0 5"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_scandinavian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/ppp1pppp/8/3p4/3P4/8/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_pirc_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/ppp1pppp/8/3p4/3Pn3/8/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_alekhine_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 3"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPP2PPP/R1BQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_scotch_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPP2PPP/R1BQKB1R b KQkq - 0 3"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_vienna_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/R1BQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_queens_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp2ppp/8/3p4/3Pp3/8/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_king_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1P1PPP/RNBQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_slav_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp2pppp/8/2pp4/3P4/8/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_nimzo_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp2ppp/4p3/3p4/3P4/5N2/PPP2PPP/R1BQKB1R w KQkq - 0 5"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_queens_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp2ppp/4p3/3p4/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_catalan_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp2ppp/3p4/4p3/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_bogo_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/8/PPPP1PPP/R1BQK1NR w KQkq - 0 5"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_grunfeld_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp3ppp/8/3pp3/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq - 0 4"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_dutch_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/3P4/8/PPP2PPP/R1BQKBNR w KQkq - 0 3"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_trompowsky_attack(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_benko_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/1p3ppp/p3p3/3pP3/3P4/8/PPP2PPP/R1BQKBNR w KQkq - 0 5"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_grob_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_london_system(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/3P4/5N2/PPP1PPPP/R1BQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_benoni_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/8/4p3/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 0 3"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_reti_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_english_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_birds_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_indian(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 2"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_fianchetto_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_nimzowitsch_larsen_attack(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_polish_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/1P6/P1PPPPPP/RNBQKBNR b KQkq - 0 1"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False
