# not 47102690, too low

height = 0
width = 0
partNumbers = []
gears = []


def main():
    global height
    global width
    global partNumbers
    global gears

    schematic = open('input.txt').readlines()

    PartNumberTally = 0

    height = len(schematic)
    width = len(schematic[0]) - 1

    print("width: " + str(width))
    print("height: " + str(height))

    row = 0
    partId = 0

    # go line by line
    for line in schematic:
        currentPart = ""
        addThisPart = False

        col = 0
        for char in line:
            if char.isdigit():
                currentPart += char

                if not addThisPart:
                    # check mid left
                    if isPunctuation(schematic, row, col - 1):
                        addThisPart = True
                    # check mid right
                    elif isPunctuation(schematic, row, col + 1):
                        addThisPart = True
                    # check center down
                    elif isPunctuation(schematic, row + 1, col):
                        addThisPart = True
                    # check center up
                    elif isPunctuation(schematic, row - 1, col):
                        addThisPart = True
                    # check left up
                    elif isPunctuation(schematic, row - 1, col - 1):
                        addThisPart = True
                    # check left down
                    elif isPunctuation(schematic, row + 1, col - 1):
                        addThisPart = True
                    # check right up
                    elif isPunctuation(schematic, row - 1, col + 1):
                        addThisPart = True
                    # check right down
                    elif isPunctuation(schematic, row + 1, col + 1):
                        addThisPart = True

                if col + 1 == width or not schematic[row][col + 1].isdigit():
                    if addThisPart:
                        partFootprint = []
                        partFootprintCol = col

                        for letter in currentPart:
                            partFootprint.append({
                                'row': row,
                                'col': partFootprintCol
                            })
                            partFootprintCol -= 1

                        part = {
                            'partNumber': currentPart,
                            'partId': partId,
                            'partLocations': partFootprint
                        }
                        partId += 1

                        # print(part)

                        partNumbers.append(part)

                    currentPart = ""
                    addThisPart = False

            col += 1

        row += 1

    gearSum = 0

    print(partNumbers)

    col = 0
    row = 0
    for line in schematic:
        print()
        for char in line:
            if char == '*':
                gears = []
                gears.append(isGear(schematic, row, col - 1))
                gears.append(isGear(schematic, row, col + 1))
                gears.append(isGear(schematic, row + 1, col))
                gears.append(isGear(schematic, row - 1, col))
                gears.append(isGear(schematic, row - 1, col - 1))
                gears.append(isGear(schematic, row + 1, col - 1))
                gears.append(isGear(schematic, row - 1, col + 1))
                gears.append(isGear(schematic, row + 1, col + 1))

                print(gears)

                gear1 = 0
                gear2 = 0
                for gear in gears:
                    if gear is not None:
                        if gear1 == 0:
                            gear1 = gear.get('partNumber')
                        elif gear2 == 0:
                            gear2 = gear.get('partNumber')

                gearPower = int(gear1) * int(gear2)
                print(gearPower)
                gearSum += gearPower

            col += 1
        row += 1
        col = 0

    print(gearSum)


def isPunctuation(schematic, row, col):
    global height
    global width

    if row >= height or col >= width:
        return False
    if row < 0 or col < 0:
        return False

    if not schematic[row][col] == '.' and not schematic[row][col].isdigit():
        return True
    else:
        return False


def isGear(schematic, row, col):
    global height
    global width
    global partNumbers
    global gears

    if row >= height or col >= width:
        return None

    if row < 0 or col < 0:
        return None

    if schematic[row][col].isdigit():
        print(row, " ", col, " @ ", schematic[row][col])
        for partNumber in partNumbers:
            print(partNumber)
            for loc in partNumber.get('partLocations'):
                if loc.get('col') == col and loc.get('row') == row:
                    for gear in gears:
                        if gear is not None:
                            if partNumber.get('partId') == gear.get('partId'):
                                return None
                    return partNumber

    else:
        return None


if __name__ == '__main__':
    main()
