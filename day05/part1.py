def main():
    almanac = open('input.txt')

    alm = almanac.readlines()

    maps = []
    seeds = []
    mapSection = -1
    j = -1
    # break up the input aps
    for i in range(len(alm)):
        if i == 0:
            # grab the seeds, put them on their own
            for seed in alm[i].split(":")[1].split():
                seeds.append(int(seed))
            # seeds.sort()
        elif alm[i].find(":") > -1:
            # skip the headers and blank lines
            maps.append([])
            mapSection += 1
            j = 0
        elif len(alm[i]) > 1:
            maps[mapSection].append([])
            for item in alm[i].split():
                maps[mapSection][j].append(int(item))
            j += 1

    ranges = []

    # range = [
    #   [ map
    #       [ in/soil
    #           1
    #       ],
    #       [ out/fert
    #           1
    #       ]
    #   ]
    # ]

    # eacd sector
    for i in range(len(maps)):
        ranges.insert(i, [])
        ranges[i] = [[], []]
        # saves the inputs into the first, outputs into second
        for j in range(len(maps[i])):
            ranges[i][1].append(calculateRangeOfValues(maps[i][j][0], maps[i][j][2]))  # in
            ranges[i][0].append(calculateRangeOfValues(maps[i][j][1], maps[i][j][2]))  # out

    # print(ranges)
    values = [seeds]

    # cycle over range sections e.g. seed - soil
    for i in range(len(ranges)):
        print("doing ", i, "nth mapping")
        # create a section for soil ids
        values.append([None] * len(values[0]))

        # loop the values for this section: seeds
        for idIndex in range(len(values[i])):
            #print("checking val index ", idIndex, ": ", values[i][idIndex])
            # loop all seed ranges
            for r in range(len(ranges[i][0])):
                #print("is ", values[i][idIndex], " in ", ranges[i][0][r])
                isIn = isValueInRange(ranges[i][0][r], values[i][idIndex])
                if isIn > -1:
                    mappedVal = getMappedValues(ranges[i][1][r], isIn)
                    # print("yes, it maps in ", ranges[i][1][r], " to ", mappedVal)
                    values[i+1][idIndex] = mappedVal
                    break

            if values[i + 1][idIndex] is None:
                values[i + 1][idIndex] = values[i][idIndex]

    locs = values.pop()
    print(min(locs))


def getMappedValues(outputRange, index):
    return outputRange[index]

def calculateRangeOfValues(start, length):
    stop = start + length
    return range(start, stop)

def isValueInRange(valueRange, value):
    if value in valueRange:
        return valueRange.index(value)
    else:
        return -1



if __name__ == '__main__':
    main()