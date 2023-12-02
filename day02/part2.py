import re

def main():
    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    colors = [
        'red',
        'blue',
        'green'
    ]

    gameTallies = []

    gamePowers = []

    print("getting games")

    games = open('input.txt', 'rt')

    sum = 0

    for game in games:
        line = game.split(":")
        rounds = line[1].split(';')
        gameId = line[0]

        gameTally = cubes.copy()

        for gameRound in rounds:
            draws = gameRound.split(',')
            for draw in draws:
                for color in colors:

                    if draw.find(color) > -1:
                        no = int(re.sub("([a-z|\n| ])", "", draw))

                        if gameTally[color] < no:
                            gameTally[color] = no
        print(gameTally)
        power = gameTally['red'] * gameTally['blue'] * gameTally['green']
        gamePowers.append(power)
        # game here
        sum += power

    print(sum)



if __name__ == '__main__':
    main()
