from back.stockfish_tools import Stockfish
from back.stockfish_tools import StockfishExplainer

engine_path = "./stockfish/stockfish-windows-x86-64-modern.exe"
stockfish = Stockfish(engine_path)

new_game = "4k3/4n3/8/8/8/8/5R2/4RK2 w - - 0 1"

stockfish.setup(new_game)

stockfish_explainer = StockfishExplainer(stockfish)
print(stockfish_explainer.explain())
