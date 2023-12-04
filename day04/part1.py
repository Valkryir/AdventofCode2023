def main():
    cards = open('input.txt')

    winnings = 0
    matches = 0

    for card in cards:
        card = card.split(":")[1].split("|")

        # no param on split takes all whitespace out
        winningNumbers = card[0].split()
        myNumbers = card[1].split()

        matchesScore = 0

        for myNo in myNumbers:
            for winningNo in winningNumbers:
                if myNo == winningNo:
                    if matchesScore == 0:
                        matchesScore = 1
                    else:
                        matchesScore = matchesScore * 2

        winnings += matchesScore

    print(winnings)



if __name__ == '__main__':
    main()