from lib.Stockfish.Stockfish import Stockfish
from lib.Stockfish.StockfishExplainer import StockfishExplainer

engine_path = "./stockfish/stockfish-windows-x86-64-modern.exe"
# engine_path = "../stockfish/stockfish-windows-x86-64-avx.exe"
stockfish = Stockfish(engine_path)

# Making moves
moves = ["e4", "c5", "a4", "d6", "b3", "Bg4", "f3", "Bh5", "Nc3", "Na6", "h3", "Qd7", "Bb5"]
for move in moves:
    stockfish.make_move(move)

stockfish.display_board()

new_game = "3k4/8/8/3n4/8/8/4Q3/3K4 b - - 0 1"
stockfish.setup_game(new_game)

# print board evaluation
print("Board evaluation:", stockfish.list_all_captures())

best_move = stockfish.get_best_move()
print("Best move according to Stockfish:", best_move)

stockfish_explainer = StockfishExplainer(stockfish)
print(stockfish_explainer.explain())
