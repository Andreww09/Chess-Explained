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
    def get_attackers_at_index(board, color, poz):

        attackers = board.attackers(color, poz)
        return attackers

    @staticmethod
    def piece_at_index_str(board, index):
        return str(board.piece_at(index)).upper()
