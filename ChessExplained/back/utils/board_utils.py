import chess


class BoardUtils:
    @staticmethod
    def is_same_rank(square1, square2):
        return chess.square_rank(square1) == chess.square_rank(square2)

    @staticmethod
    def is_same_file(square1, square2):
        return chess.square_file(square1) == chess.square_file(square2)

    @staticmethod
    def is_same_diagonal(square1, square2):
        if abs(chess.square_rank(square1) - chess.square_rank(square2)) == abs(
                chess.square_file(square1) - chess.square_file(square2)):
            return True
        return False

    @staticmethod
    def get_attackers_at_square(board, square):
        attackers = board.attackers(board.turn, square)

        return attackers

    @staticmethod
    def is_battery_compatible(piece1, piece2):
        if (piece1.piece_type == chess.BISHOP or piece1.piece_type == chess.QUEEN) and (
                piece2.piece_type == chess.BISHOP or piece2.piece_type == chess.QUEEN):
            return True
        elif (piece1.piece_type == chess.ROOK or piece1.piece_type == chess.QUEEN) and (
                piece2.piece_type == chess.ROOK or piece2.piece_type == chess.QUEEN):
            return True

        return False

    @staticmethod
    def is_pin_compatible(piece1, piece2, piece3):
        # If piece3 is not more valuable than piece2, then it is not a pin
        if piece3.piece_type <= piece2.piece_type:
            return False

        # If piece3 is not more valuable than piece1, then it is not a pin
        if piece3.piece_type <= piece1.piece_type:
            return False

        return True

    @staticmethod
    def get_attackers_at_index(board, color, poz):

        attackers = board.attackers(color, poz)
        return attackers

    @staticmethod
    def piece_at_index_str(board, index):
        return str(board.piece_at(index)).upper()

    @staticmethod
    def expand_piece_name(piece):
        if piece == 'P' or piece == 'p':
            return 'Pawn'
        elif piece == 'N' or piece == 'n':
            return 'Knight'
        elif piece == 'B' or piece == 'b':
            return 'Bishop'
        elif piece == 'R' or piece == 'r':
            return 'Rook'
        elif piece == 'Q' or piece == 'q':
            return 'Queen'
        elif piece == 'K' or piece == 'k':
            return 'King'
        raise Exception("Invalid Piece Type")

    @staticmethod
    def get_evaluation_score(eval_first_item):
        """
            Evaluate the current board

            :return: evaluation score
        """
        if eval_first_item[0] == 'M':
            return -100000 if eval_first_item[5] == '-' else 100000

        eval_first_item = eval_first_item[eval_first_item.find('('):]
        eval_first_item = eval_first_item.strip('()')
        return int(eval_first_item)
