def main():
    input = open('input.txt').readlines()

    tokens = [
        'A',
        'K',
        'Q',
        'T',
        '9',
        '8',
        '7',
        '6',
        '5',
        '4',
        '3',
        '2',
        'J'
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
            if token != "J":
                c = hands[hi][0].count(token)
                if c == 5:
                    print("it's five of a kind", hands[hi][0])
                    handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                    break
                if c == 4:
                    if hands[hi][0].count("J") == 1:
                        print("it's five of a kind", hands[hi][0])
                        handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    else:
                        print("it's four of a kind", hands[hi][0])
                        handTypes[5].append([hi, hands[hi][0], hands[hi][1]])
                        break
                if c == 3:
                    # check for full house
                    isFullHouse = identifyFullHouse(tokens, token, hands, hi, 2)

                    if hands[hi][0].count("J") == 2:
                        print("it's five of a kind", hands[hi][0])
                        handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif hands[hi][0].count("J") == 1:
                        print("it's four of a kind", hands[hi][0])
                        handTypes[5].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif isFullHouse:
                        print("it's full house", hands[hi][0])
                        handTypes[4].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    else:
                        print("it's three of a kind", hands[hi][0])
                        handTypes[3].append([hi, hands[hi][0], hands[hi][1]])
                        break

                if c == 2:
                    # check for full house
                    isFullHouse = identifyFullHouse(tokens, token, hands, hi, 3)

                    isTwoPair = False
                    for t2 in tokens:
                        if t2 != token:
                            c2 = hands[hi][0].count(t2)
                            if c2 == 2:
                                isTwoPair = True
                                break

                    if hands[hi][0].count("J") == 3:
                        print("it's five of a kind", hands[hi][0])
                        handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif hands[hi][0].count("J") == 2:
                        print("it's four of a kind", hands[hi][0])
                        handTypes[5].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif isFullHouse:
                        print("it's full house", hands[hi][0])
                        handTypes[4].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif hands[hi][0].count("J") == 1:
                        print("it's three of a kind", hands[hi][0])
                        handTypes[3].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    elif isTwoPair:
                        print("it's a two pair", hands[hi][0])
                        handTypes[2].append([hi, hands[hi][0], hands[hi][1]])
                        break
                    else:
                        print("it's a one pair", hands[hi][0])
                        handTypes[1].append([hi, hands[hi][0], hands[hi][1]])
                    break
            elif token == "J":
                c = hands[hi][0].count(token)
                if c == 5:
                    print("it's five of a kind", hands[hi][0])
                    handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                    break
                if c == 4:
                    print("it's five of a kind", hands[hi][0])
                    handTypes[6].append([hi, hands[hi][0], hands[hi][1]])
                    break
        else:
            if hands[hi][0].count("J") == 1:
                print("it's one pair", hands[hi][0])
                handTypes[1].append([hi, hands[hi][0], hands[hi][1]])
            elif hands[hi][0].count("J") == 2:
                print("it's three of a kind", hands[hi][0])
                handTypes[3].append([hi, hands[hi][0], hands[hi][1]])
            elif hands[hi][0].count("J") == 3:
                print("it's four of a kind", hands[hi][0])
                handTypes[5].append([hi, hands[hi][0], hands[hi][1]])
            else:
                print("its a high card (all distinct)", hands[hi][0])
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
                ranking.append([handType[0][1], nextRank * handType[0][2]])
                nextRank += 1
            else:
                handType = sortHandsByStrength(handType, tokenStrength)
                for hand in handType:
                    ranking.append([hand[1], nextRank * hand[2]])
                    nextRank += 1

    # print("sorted:")
    # i = 1
    # for h in ranking:
    #     print("r:", i, "-", h)
    #     i += 1
    print("")
    # 765 * 1
    # 220 * 2
    # 28 * 3
    # 684 * 4
    # 483 * 5

    finalSum = 0
    for r in ranking:
        finalSum += r[1]

    print("f:", finalSum)
    # not 250246117, too high
    # not 250321821, too high
    # not 250510144, too high
    # not 250042040, too high
    # 249666369


def sortHandsByStrength(handsToSort, tokenStrength):
    for i in range(len(handsToSort)):
        for hand in range(len(handsToSort)):
            # sort asc
            if hand + 1 < len(handsToSort) and isHandAStrongerThanHandB([handsToSort[hand]], [handsToSort[hand + 1]], tokenStrength):
                h = handsToSort[hand]
                handsToSort[hand] = handsToSort[hand + 1]
                handsToSort[hand + 1] = h

    return handsToSort


def isHandAStrongerThanHandB(handA, handB, tokenStrength):
    isHandAStronger = False
    # print("is ", handA[0][1], "stronger than", handB[0][1])
    for i in range(len(handA[0][1])):
        # print("is ", handA[0][1][i], "same as ", handB[0][1][i])
        if handA[0][1][i] != handB[0][1][i]:
            # print("no, is ", handA[0][1][i], "stronger than ", handB[0][1][i])
            strA = tokenStrength.index(handA[0][1][i])
            strB = tokenStrength.index(handB[0][1][i])
            if strA > strB:
                # print("yes")
                return True
            else:
                # print("no")
                return False
                break

    print(isHandAStronger)
    return isHandAStronger


def identifyFullHouse(tokens, token, hands, hi, qty):
    for t2 in tokens:
        if t2 != token:
            c2 = hands[hi][0].count(t2)
            j2 = hands[hi][0].count("J")
            if c2 + j2 == qty:
                return True

    return False


if __name__ == '__main__':
    main()

    # tokens = [
    #     'A',
    #     'K',
    #     'Q',
    #     'J',
    #     'T',
    #     '9',
    #     '8',
    #     '7',
    #     '6',
    #     '5',
    #     '4',
    #     '3',
    #     '2'
    # ]
    #
    # tokenStrength = tokens.copy()
    # tokenStrength.reverse()
    #
    # handA = [
    #     [0, "JKKK2"],
    #     []
    # ]
    #
    # handB = [
    #     [0, "QQQQ2"],
    #     []
    # ]
    #
    # isHandAStrongerThanHandB(handA, handB, tokenStrength)
