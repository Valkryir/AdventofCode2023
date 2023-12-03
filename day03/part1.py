
# not 531387, 528898, 526404 too high

height = 0
width = 0

def main():
    global height
    global width

    schematic = open('case1.txt').readlines()

    PartNumberTally = 0

    height = len(schematic)
    width = len(schematic[0])-1

    print("width: " + str(width))
    print("height: " + str(height))

    row = 0

    partNumbers = []

    #go line by line
    for line in schematic:
        lastChar = ""
        currentPart = ""
        addThisPart = False

        print("line: " + str(row+1))

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

                print("col: " + str(col) + ", width: " + str(width))
                if col+1 == width or not schematic[row][col+1].isdigit():
                    if addThisPart:
                        print("Part + Tally: " + currentPart + " + " + str(PartNumberTally) + " = "
                              + str(PartNumberTally + int(currentPart)))
                        PartNumberTally += int(currentPart)

                    currentPart = ""
                    addThisPart = False

            col += 1

        row += 1

    print(PartNumberTally)


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


if __name__ == '__main__':
    main()
