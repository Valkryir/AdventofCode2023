import re


def main():
    print("getting calibrations")

    # inputFile = "test1.txt"
    inputFile = "input.txt"

    inputData = open(inputFile, "rt")

    sum = 0

    for line in inputData:
        line = re.sub("([a-z|\n])", "", line)

        line = line[0] + line[-1]

        sum += int(line)

    print(sum)


if __name__ == '__main__':
    main()
