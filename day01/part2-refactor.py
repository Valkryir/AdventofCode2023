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


        lowestDigit = -1

        for i in range(len(line)):
            if line[i].isdigit():
                lowestDigit = int(line[i])
                break
            else:
                for no in range(len(numbers)):
                    if line[i].startswith(numbers[no]):
                        lowestDigit = numbers[no]
                        break

                if lowestDigit > -1:
                    break;

        highestDigit = -1

        lineRev = line[::-1]

        for i in range(len(lineRev)):
            if line[i].isdigit():
                highestDigit = int(line[i])
                break
            else:
                for no in range(len(numbers)):
                    if line[i].startswith(numbers[no][::-1]):
                        highestDigit = numbers[no]
                        break

                if highestDigit > -1:
                    break;

        formatter = "{}{}"

        val = formatter.format(lowestDigit, highestDigit)

        sum = sum + int(val)

        # line = re.sub("([a-z|\n])", "", line)

        # line = line[0] + line[-1]

        # sum += int(line)

    print(sum)


if __name__ == '__main__':
    main()