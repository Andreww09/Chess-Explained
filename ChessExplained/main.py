from back.stockfish_tools import Stockfish
from back.stockfish_tools import StockfishExplainer

engine_path = "./stockfish/stockfish-windows-x86-64-modern.exe"
stockfish = Stockfish(engine_path)

new_game = "7k/R7/8/4N3/2B5/8/8/6K1 w - - 0 1"

stockfish.setup(new_game)

stockfish_explainer = StockfishExplainer(stockfish)
print(stockfish_explainer.explain())
