def main():

    histories = open('input.txt').readlines()

    graphs = []
    for hist in histories:
        graph = [[]]
        hist = hist.split()
        for h in hist:
            graph[0].append(int(h))
        graphs.append(graph)

    for graph in graphs:
        seqIndex = 0
        for seq in graph:
            if not isAllValsZero(graph[seqIndex]):
                graph.append([])
                valIndex = 0
                for val in graph[seqIndex]:
                    if valIndex < len(seq) - 1:
                        diff = seq[valIndex + 1] - val
                        graph[seqIndex+1].append(diff)

                    valIndex += 1
            seqIndex += 1

    finalSum = 0

    for graph in graphs:
        seqLen = len(graph)
        seqIndex = seqLen - 1
        while seqIndex >= 0:
            valBelow = 0

            if seqIndex < seqLen - 1:
                valBelow = graph[seqIndex+1][-1]

            valLeft = graph[seqIndex][-1]

            graph[seqIndex].append(valLeft + valBelow)

            if seqIndex == 0:
                finalSum += valLeft + valBelow

            seqIndex -= 1

    printArray(graphs)
    print(finalSum)

    # not 1702219394
    #     1702218515

def isAllValsZero(arrVals):
    for val in arrVals:
        if val != 0:
            return False

    return True

def printArray(arrayToPrint):
    for arr in arrayToPrint:
        for ar in arr:
            print(ar)
        print("")

if __name__ == '__main__':
    main()