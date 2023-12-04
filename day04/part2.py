def main():
    cards = open('input.txt')

    winnings = 0
    matches = 0

    cardList = []

    cardList = cards.readlines()

    cards = cardList
    cardNo = 1
    for card in cards:
        cardSplit = card.split(":")

        cardNo = int(cardSplit[0].split()[1])
        #print("cardNo ", cardNo)
        card = cardSplit[1].split("|")

        # no param on split takes all whitespace out
        winningNumbers = card[0].split()
        myNumbers = card[1].split()

        matchesScore = 0

        for myNo in myNumbers:
            for winningNo in winningNumbers:
                if myNo == winningNo:
                    matchesScore += 1

        #print("won ", matchesScore, " more cards")
        while matchesScore > 0:
            if not (matchesScore + cardNo) > len(cardList)-1:
                cards.append(cardList[matchesScore + cardNo-1])
            matchesScore -= 1

    print(len(cards))
    if len(cards) == 8172507:
        print("PASSED!")


if __name__ == '__main__':
    main()
