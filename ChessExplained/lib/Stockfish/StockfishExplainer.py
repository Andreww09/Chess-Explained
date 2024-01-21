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
        dict = {}

        # Make the move
        self.stockfish.move(best_move)

        # print board
        print("Current board: ")
        self.stockfish.display()

        # Undo the move
        self.stockfish.undo()

        is_pin = self._is_pin(best_move)
        is_fork = self._is_fork(best_move)
        is_capture = self.stockfish.is_capture(best_move)
        dict['checkmate'] = self._is_checkmate(best_move)
        is_check = self._is_check(best_move)
        is_en_passant = self.stockfish.is_en_passant(best_move)
        is_stalemate = self._is_stalemate(best_move)
        is_insufficient_material = self._is_insufficient_material(best_move)
        is_battery = self._is_battery(best_move)
        is_sacrifice = self._is_sacrifice(best_move)
        dict['discovered_attack'] = self._is_a_discovered_attack(best_move)
        dict['castling'] = self._is_a_castling(best_move)
        dict['pawn_promotion'] = self._is_pawn_promotion(best_move)
        is_skewer = self._is_skewer(best_move)
        is_forced_checkmate = self._is_forced_checkmate(best_move)
        is_polish_opening = self._is_polish_opening(best_move)
        is_nimzowitsch_larsen_attack = self._is_nimzowitsch_larsen_attack(best_move)
        is_kings_indian_attack = self._is_kings_indian_attack(best_move)
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

        print("is_pin: ", is_pin)
        print("is_fork: ", is_fork)
        print("is_checkmate: ", dict['checkmate']['enable'])
        print("is_check: ", is_check)
        print("is_check_forced: ", self._is_move_check_forced())
        print("is_capture: ", is_capture)
        print("is_en_passant: ", is_en_passant)
        print("is_stalemate: ", is_stalemate)
        print("is_insufficient_material: ", is_insufficient_material)
        print("is_battery: ", is_battery)
        print("is_sacrifice: ", is_sacrifice)
        print("is_discovered_attack: ", dict['discovered_attack']['enable'])
        print("is_castling: ", dict['castling']['enable'])
        print("is_pawn_promotion: ", dict['pawn_promotion']['enable'])
        print("is_skewer: ", is_skewer)
        print("is_forced_checkmate: ", is_forced_checkmate)
        print("is_polish_opening: ", is_polish_opening)
        print("is_nimzowitsch_larsen_attack: ", is_nimzowitsch_larsen_attack)
        print("is_kings_indian_attack: ", is_kings_indian_attack)
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

        #  EXPLANATIONS
        """ 
            in some cases, key 'piece' corresponds to an explicit piece(type of promoted pawn,
            the piece who delivers checkmates, etc). In other cases, key 'piece' corresponds to a list of 
            pieces(discovered_attack, fork , etc): first piece is always the attacker, followings are attacked pieces 
        """

        if dict['checkmate']['enable']:
            explanation += f"{dict['checkmate']['piece']} delivers checkmate. "
        if dict['castling']['enable']:
            explanation += f"{dict['castling']['side']} castling happens. "
        if dict['pawn_promotion']['enable']:
            explanation += f"Pawn promoted to {dict['pawn_promotion']['piece']}. "
        if dict['discovered_attack']['enable']:
            explanation += f"{dict['discovered_attack']['piece'][0]} moved and facilitates a discovered attack to {dict['discovered_attack']['piece'][1]}"

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

        dict = {}

        self.stockfish.move(move_san)
        is_checkmate = self.stockfish.board.is_checkmate()
        self.stockfish.undo()

        # get piece that delivers checkmate
        if is_checkmate:
            start_end_move = self.stockfish.start_end_from_san(move_san)
            index = self.stockfish.index_from_san(start_end_move[0])
            piece = BoardUtils.piece_at_index_str(self.stockfish.board, index)
            piece = BoardUtils.expand_piece_name(piece)
            dict['piece'] = piece
        dict['enable'] = is_checkmate
        return dict

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
        """
            Determine if the move results in a discovered attack.

            :param move_san: Move in standard algebraic notation
            :return: True if the move results in a discovered attack, False otherwise
        """

        dict = {}
        from_square = self.stockfish.board.parse_san(move_san).from_square
        to_square = self.stockfish.board.parse_san(move_san).to_square

        moved_piece_type = BoardUtils.piece_at_index_str(self.stockfish.board, from_square)
        moved_piece = BoardUtils.expand_piece_name(moved_piece_type)

        squares_before_move = self.stockfish.captures_except_square_allowing_duplicates(from_square)

        self.stockfish.move(move_san)
        self.stockfish.board.turn = not self.stockfish.board.turn

        squares_after_move = self.stockfish.captures_except_square_allowing_duplicates(to_square)

        self.stockfish.undo()

        for attacked_square in squares_after_move:
            if squares_after_move.count(attacked_square) > squares_before_move.count(attacked_square):
                dict['enable'] = True
                attacked_piece_type = self.stockfish.piece_at_san(attacked_square)
                attacked_piece = BoardUtils.expand_piece_name(str(attacked_piece_type))
                dict['piece'] = [moved_piece, attacked_piece]
                return dict

        dict['enable'] = False
        return dict

    def _is_a_castling(self, move_san):
        enable = self.stockfish.board.is_castling(self.stockfish.board.parse_san(move_san))
        from_square = self.stockfish.board.parse_san(move_san).from_square
        to_square = self.stockfish.board.parse_san(move_san).to_square
        if chess.square_rank(from_square) < chess.square_rank(to_square):
            side = "KingSide"
        else:
            side = "QueenSide"

        return dict({"enable": enable, "side": side})

    def _is_pawn_promotion(self, move_san):
        enable = False
        piece_type = ""
        start_end_move = self.stockfish.start_end_from_san(move_san)
        start_index = self.stockfish.index_from_san(start_end_move[0])
        end_index = self.stockfish.index_from_san(start_end_move[1])
        start_piece = BoardUtils.piece_at_index_str(self.stockfish.board, start_index)
        if start_piece == 'P':
            self.stockfish.move(move_san)
            end_piece = BoardUtils.piece_at_index_str(self.stockfish.board, end_index)
            if end_piece != 'P':
                piece_type = end_piece
                self.stockfish.undo()
                enable = True
            self.stockfish.undo()

        if enable:
            piece = BoardUtils.expand_piece_name(piece_type)
            return dict({"enable": enable, "piece": piece})
        else:
            return dict({"enable": enable})

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
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_french_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_ruy_lopez_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_caro_kann_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_italian_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_scandinavian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_pirc_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_alekhine_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_scotch_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_vienna_game(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_queens_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_slav_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_king_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_nimzo_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_queens_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_catalan_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/pppp1ppp/4pn2/8/2PP4/6P1/PP2PP1P/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_bogo_indian_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqk2r/pppp1ppp/4pn2/8/1bPP4/5N2/PP2PPPP/RNBQKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_grunfeld_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_dutch_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_trompowsky_attack(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/pppppppp/5n2/6B1/3P4/8/PPP1PPPP/RN1QKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_benko_gambit(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/8/PP2PPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_london_system(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_benoni_defense(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkb1r/pp3ppp/3p1n2/2pP4/8/2N5/PP2PPPP/R1BQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_reti_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_english_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_birds_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_indian_attack(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_kings_fianchetto_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/6P1/PPPPPP1P/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_nimzowitsch_larsen_attack(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/8/1P6/P1PPPPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_polish_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR"):
            self.stockfish.undo()
            return True
        self.stockfish.undo()
        return False

    def _is_grob_opening(self, move_san):
        self.stockfish.move(move_san)
        if self.stockfish.board.fen().startswith("rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR"):
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
