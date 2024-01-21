from back.stockfish_tools import Stockfish
from back.stockfish_tools import StockfishExplainer

engine_path = "./stockfish/stockfish-windows-x86-64-modern.exe"
# engine_path = "../stockfish/stockfish-windows-x86-64-avx.exe"
stockfish = Stockfish(engine_path)

new_game = "7k/R7/8/4N3/2B5/8/8/6K1 w - - 0 1"

stockfish.setup(new_game)

stockfish_explainer = StockfishExplainer(stockfish)
print(stockfish_explainer.explain())

# # example of usage
# new_game = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# stockfish.setup(new_game)
# stockfish.move("e4")
# stockfish.move("e5")
# stockfish.undo()
# print("Current move: ", stockfish.turn())
# stockfish.switch_turn()
# print("Changed turn: ", stockfish.turn())
# stockfish.switch_turn()
# stockfish.move("e5")
# stockfish.move("Nf3")
# stockfish.move("d5")
# stockfish.move("a3")
# stockfish.move("Bg4")
# stockfish.display()
# print("Current attacked pieces: ", stockfish.attacked_pieces())
# print("Current legal SAN moves: ", stockfish.moves())
# print("All legal square moves(start_square, end_square): ", stockfish.squares())
# print("Current legal SAN moves by d2: ", stockfish.moves_by("d2"))
# print("Current legal SAN moves by e4: ", stockfish.moves_by("e4"))
# print("Current legal SAN moves by a3: ", stockfish.moves_by("a3"))
# print("Current legal square moves by d2: ", stockfish.squares_by("d2"))
# print("Current legal square moves by e4: ", stockfish.squares_by("e4"))
# print("Current legal square moves by a3: ", stockfish.squares_by("a3"))
# print("All legal captures: ", stockfish.captures())
# print("All legal captures in SAN: ", stockfish.captures_san())
# print("All legal captures by e4: ", stockfish.captures_by("e4"))
# print("All legal captures by f3: ", stockfish.captures_by("f3"))
# print("All legal SAN captures by e4: ", stockfish.captures_by_san("e4"))
# print("All legal SAN captures by f3: ", stockfish.captures_by_san("f3"))
# print("Possible capture pieces: ", stockfish.capture_pieces())
# print("Possible capture pieces in SAN: ", stockfish.capture_pieces_san())
# print("Possible capture pieces by e4: ", stockfish.capture_pieces_by("e4"))
# print("Possible capture pieces by f3: ", stockfish.capture_pieces_by("f3"))
# print("Possible capture SAN pieces by e4: ", stockfish.capture_pieces_by_san("e4"))
# print("Possible capture SAN pieces by f3: ", stockfish.capture_pieces_by_san("f3"))
# print("Best move: ", stockfish.best_move())
# print("Best 2 move sequence: ", stockfish.best_move_sequence(2))
# print("Board evaluation: ", stockfish.evaluation())
# print("Get index from SAN: ", stockfish.index_from_san("e4"))
# print("Get piece from SAN: ", stockfish.piece_at_san("e4"))
# print("Get piece from index: ", stockfish.piece_at_index_str(28))




#stockfish_explainer = StockfishExplainer(stockfish)
#print(stockfish_explainer.explain())

# if anybody needs for testing :)

# print a board with numbers
# for i in range(8):
#     for j in range(8):
#         print(i * 8 + j, end=" ")
#
#     print()


# SAN notation example
# Qd2

# FEN notation example
# 4k3/4q3/8/8/4B3/4R3/4R3/4K3 w - - 2 2
