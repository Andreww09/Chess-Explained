from Util import Util


def main():
    games = Util.import_data("./Datasets/games.txt")

    repeated, counts = Util.get_frequent_last_three(games)
    for game, count in zip(repeated, counts):
        print(game, end=" ")
        print(count)
    print(len(repeated))
    print(len(games))


if __name__ == '__main__':
    main()
