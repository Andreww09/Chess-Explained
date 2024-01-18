import chess
import chess.engine


def get_best_move(board):
    with chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe") as engine:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        return result.move


board = chess.Board()
# asa ne referim la pozitiile de pe tabla
# 56 57 58 59 60 61 62 63
# 48 49 50 51 52 53 54 55
# 40 41 42 43 44 45 46 47
# 32 33 34 35 36 37 38 39
# 24 25 26 27 28 29 30 31
# 16 17 18 19 20 21 22 23
#  8  9 10 11 12 13 14 15
#  0  1  2  3  4  5  6  7

# Make some example moves
moves = ["e2e4", "c7c5", "a2a4", "d7d6", "b2b3", "c8g4", "f2f3", "g4h5", "b1c3", "b8a6", "h2h3", "d8d7", "f1b5"]
for move in moves:
    board.push_uci(move)

best_move = get_best_move(board)
print(board)

for capture in board.generate_legal_captures():
    print(capture)
# False - black, True - white
print(board.is_attacked_by(False, 51))
print(board.is_pinned(False, 51))
print(board.color_at(51))

print(board.attackers(True, 51))
print("Best move according to Stockfish: {}".format(best_move))
