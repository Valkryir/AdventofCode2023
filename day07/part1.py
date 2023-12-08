
def main():
    input = open('test.txt').readlines()

    tokens = [
        'A',
        'K',
        'Q',
        'J',
        'T',
        '9',
        '8',
        '7',
        '6',
        '5',
        '4',
        '3',
        '2'
    ]

    tokenStrength = tokens.copy()
    tokenStrength.reverse()

    hands = []
    # [hand, tieBreaker]

    for handIndex in range(len(input)):
        i = input[handIndex].split()
        hands.append([
            i[0], int(i[1])])

    # [hand index, base rank, tiebreaker] ascending
    handTypes = [[], [], [], [], [], [], []]

    for hi in range(len(hands)):
        for token in tokens:
            c = hands[hi][0].count(token)
            if c == 5:
                print("it's five of a kind")
                handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                break
            if c == 4:
                print("it's four of a kind")
                handTypes[5].append([hi, hands[hi][0], hands[hi][1]])
                break
            if c == 3:
                # check for full house
                isFullHouse = False
                for t2 in tokens:
                    if t2 != token:
                        c2 = hands[hi][0].count(t2)
                        if c2 == 2:
                            print("it's full house")
                            handTypes[4].append([hi, hands[hi][0], hands[hi][1]])
                            isFullHouse = True
                            break

                if isFullHouse:
                    break

                print("it's three of a kind")
                handTypes[3].append([hi, hands[hi][0], hands[hi][1]])
                break

            if c == 2:
                isTwoPair = False
                for t2 in tokens:
                    if t2 != token:
                        c2 = hands[hi][0].count(t2)
                        if c2 == 2:
                            print("it's a two pair")
                            handTypes[2].append([hi, hands[hi][0], hands[hi][1]])
                            isTwoPair = True
                            break
                if isTwoPair:
                    break

                print("it's a one pair")
                handTypes[1].append([hi, hands[hi][0], hands[hi][1]])
                break
        else:
            print("its a high card (all distinct)")
            handTypes[0].append([hi, hands[hi][0], hands[hi][1]])

    print("")
    for h in handTypes:
        print(h)
    print("")


    nextRank = 1
    ranking = []

    # sort hands into ranking
    for handType in handTypes:
        handsOfType = len(handType)

        if handsOfType != 0:
            if handsOfType == 1:
                print("h:", handType[0])
                ranking.append([handType[0][1], nextRank * handType[0][2]])
                nextRank += 1
            else:
                handType = sortHandsByStrength(handType, tokenStrength)
                for hand in handType:
                    print("ha:", hand[1])
                    ranking.append([hand[1], nextRank * hand[2]])
                    nextRank += 1

    print(ranking)
    # 765 * 1
    # 220 * 2
    # 28 * 3
    # 684 * 4
    # 483 * 5

    finalSum = 0
    for r in ranking:
        print(r[1])
        finalSum += r[1]

    print("f:", finalSum)
    # not 250001735



def sortHandsByStrength(handsToSort, tokenStrength):
    for hand in range(len(handsToSort)):
        # sort asc
        if hand+1 < len(handsToSort) and isHandAStrongerThanHandB([handsToSort[hand]], [handsToSort[hand + 1]], tokenStrength):
            h = handsToSort[hand]
            print("a: ", h)
            handsToSort[hand] = handsToSort[hand + 1]
            handsToSort[hand + 1] = h

    return handsToSort


def isHandAStrongerThanHandB(handA, handB, tokenStrength):
    for i in range(len(handA)):
        if handA[0][i] != handB[0][i]:
            strA = tokenStrength.index(handA[0][1][0][i])
            strB = tokenStrength.index(handB[0][1][0][i])
            if strA > strB:
                return True
            else:
                return False

if __name__ == '__main__':
    main()
