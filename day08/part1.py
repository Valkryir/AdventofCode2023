def main():
    fileIn = open('input.txt').readlines()

    ddict = {}
    i = 0
    for line in fileIn:
        if i > 1:
            a = line.split(" = ")
            b = a[1].replace("(", "").replace(")", "").split(", ")

            ddict.update({a[0]: [
                b[0].split()[0],
                b[1].split()[0]
            ]})

        i += 1

    dIndex = 0
    directions = fileIn[0].strip()
    dLen = len(directions)

    currNodes = []

    for node in ddict:
        if node[2] == "A":
            currNodes.append(node)

    print(currNodes)



    stepsArr = []

    steps = 0

    for nodeIndex in range(len(currNodes)):

        isCached = None
        jump = 1
        cNode = currNodes[nodeIndex]
        while not cNode[2] == "Z":

            if directions[dIndex] == "L":
                cNode = ddict[cNode][0]

            elif directions[dIndex] == "R":
                cNode = ddict[cNode][1]

            steps += jump
            dIndex += jump

            if dIndex >= dLen:
                dIndex = 0

        stepsArr.append(steps)
        steps = 0

    print(stepsArr)


if __name__ == '__main__':
    main()
