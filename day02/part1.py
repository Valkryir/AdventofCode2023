import re


def main():
    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    colors = [
        'red',
        'blue',
        'green'
    ]

    possibleGames = []

    print("getting games")

    games = open('input.txt', 'rt')

    sum = 0

    for game in games:
        line = game.split(":")
        sets = line[1].split(';')
        gameId = line[0]

        gameBroken = False
        print("checking " + gameId)
        print(sets)
        print()
        for set in sets:
            # gameTally = cubes.copy()
            draws = set.split(',')
            for draw in draws:
                for color in colors:

                    if draw.find(color) > -1:
                        no = int(re.sub("([a-z|\n| ])", "", draw))

                        if cubes[color] < no:
                            gameBroken = True
                            break

                if gameBroken:
                    break

        if not gameBroken:
            print("game not broken")
            sum += int(re.sub("([a-z|A-Z|\n| ])", "", gameId))

        print("#########")

    print(sum)


if __name__ == '__main__':
    main()
