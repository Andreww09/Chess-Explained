class Util:
    @staticmethod
    def import_data(path):
        with open(path, "r") as file:
            games = file.read().split(sep="#\n")
            games = games[0:(len(games) - 1)]
        return games

    @staticmethod
    def get_frequent_last_three(games):
        repeated = []
        counts = []

        games = [game.replace("+", "").split(" ") for game in games]
        games = [tuple(game[-5:len(game):2]) for game in games]

        for last_three in games:
            if len(last_three) > 2:
                count = games.count(last_three)
                if count >= 2:
                    if last_three not in repeated:
                        repeated.append(last_three)
                        counts.append(count)
        return repeated, counts
