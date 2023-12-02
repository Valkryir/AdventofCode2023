import re

numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def main():
    print("getting calibrations")

    # inputFile = "test2.txt"
    inputFile = "input.txt"

    inputData = open(inputFile, "rt")

    sum = 0

    for line in inputData:

        numbersInLine = []

        for i in range(len(numbers)):
            inString = line.find(numbers[i])

            while inString > -1:
                numbersInLine.append(dict(pos=inString, val=i + 1))
                inString = line.find(numbers[i], inString+1)

        for i in range(len(line)):
            if line[i].isdigit():
                numbersInLine.append(dict(pos=i, val=line[i]))

        lowestPos = numbersInLine[0].get('pos')
        lowestDigit = numbersInLine[0].get('val')
        highestPos = numbersInLine[0].get('pos')
        highestDigit = numbersInLine[0].get('val')

        for i in numbersInLine:
            if i.get('pos') > highestPos:
                highestPos = i.get('pos')
                highestDigit = i.get('val')
            if i.get('pos') < lowestPos:
                lowestPos = i.get('pos')
                lowestDigit = i.get('val')

        formatter = "{}{}"

        val = formatter.format(lowestDigit, highestDigit)

        sum = sum + int(val)

        # line = re.sub("([a-z|\n])", "", line)

        # line = line[0] + line[-1]

        # sum += int(line)

    print(sum)


if __name__ == '__main__':
    main()