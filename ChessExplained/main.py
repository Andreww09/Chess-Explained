from lib.Stockfish.Stockfish import Stockfish
from lib.Stockfish.StockfishExplainer import StockfishExplainer

engine_path = "../stockfish/stockfish-windows-x86-64-modern.exe"
# engine_path = "../stockfish/stockfish-windows-x86-64-avx.exe"
stockfish = Stockfish(engine_path)

# Making moves
moves = ["e4", "c5", "a4", "d6", "b3", "Bg4", "f3", "Bh5", "Nc3", "Na6", "h3", "Qd7", "Bb5"]
for move in moves:
    stockfish.make_move(move)

stockfish.display_board()

new_game = "4k3/4q3/8/8/4B3/4R3/4R3/4K3 w - - 2 2"
stockfish.setup_game(new_game)

# print board evaluation
print("Board evaluation:", stockfish.list_all_captures())

best_move = stockfish.get_best_move()
print("Best move according to Stockfish:", best_move)

stockfish_explainer = StockfishExplainer(stockfish)
print(stockfish_explainer.explain())


# if anybody needs for testing :)

# print a board with numbers
# for i in range(8):
#     for j in range(8):
#         print(i * 8 + j, end=" ")
#
#     print()
