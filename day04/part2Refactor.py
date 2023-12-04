cardDefs = []

def main():
    cards = open('input.txt')

    winnings = 0
    matches = 0

    cardList = cards.readlines()

    cardNo = 1
    for card in cardList:
        card = card.split(":")[1].split("|")

        # no param on split takes all whitespace out
        winningNumbers = card[0].split()
        myNumbers = card[1].split()

        matchesScore = 0

        for myNo in myNumbers:
            for winningNo in winningNumbers:
                if myNo == winningNo:
                    matchesScore += 1

        cardDefs.append([int(cardNo), matchesScore])

        cardNo += 1

    cards = cardDefs

    # print(cardDefs)
    cardCount = 0

    for card in cards:
        cardCount += 1
        cardCount += countCardWins(card)

    print("Cards: ", cardCount)
    if cardCount == 8172507:
        print("PASSED!")


def countCardWins(card):
    global cardDefs

    # print(card)

    matchesScore = card[1]
    cardNo = card[0]
    count = matchesScore
    # print(" checking cards of ", card[0])
    while matchesScore > 0:
        if (matchesScore + cardNo-1) < len(cardDefs):
            # print(" check card of ", matchesScore + cardNo-1, " within ", cardNo)
            count += countCardWins(cardDefs[matchesScore + cardNo-1])
            # print(" done checking ", matchesScore + cardNo-1)
        matchesScore -= 1

    return count

if __name__ == '__main__':
    main()
