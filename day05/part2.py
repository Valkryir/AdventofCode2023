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
            ss = alm[i].split(":")[1].split()
            for seed in range(0, len(ss), 2):
                start = int(ss[seed])
                stop = int(ss[seed + 1]) + start
                if len(seeds) > 1 and start < seeds[0].start:
                    seeds.insert(0, range(start, stop))
                else:
                    seeds.append(range(start, stop))
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

    # eacd sector
    for i in range(len(maps)):
        ranges.insert(i, [])
        ranges[i] = [[], []]
        # saves the inputs into the first, outputs into second, sort the inputs, match the outputs to same position
        for j in range(len(maps[i])):
            if ranges[i][0] != [] and ranges[i][0][j - 1].start > maps[i][j][1]:
                ranges[i][1].insert(j - 1, calculateRangeOfValues(maps[i][j][0], maps[i][j][2]))
                ranges[i][0].insert(j - 1, calculateRangeOfValues(maps[i][j][1], maps[i][j][2]))
            else:
                ranges[i][1].append(calculateRangeOfValues(maps[i][j][0], maps[i][j][2]))  # in
                ranges[i][0].append(calculateRangeOfValues(maps[i][j][1], maps[i][j][2]))  # out

    locs = []
    i = 0

    outputs = [seeds]

    # seed > soil > fert > etc
    for mapOfRanges in ranges:
        dprint("checking", i, "nth map")
        j = 0
        # 55 > 68
        outputs.append([])
        dprint("input ranges:", mapOfRanges)
        dprint("seed ranges:", outputs[i])
        for seed in outputs[i]:
            k = 0
            isSeedRangeMapped = False
            dprint("seed: ", seed)
            # 98>100, 50>98
            for indvRange in mapOfRanges[0]:

                # only check if even fits
                # if seed range doesnt end before the input range ends or seed range starts after inpiut range ends
                dprint("seed", seed, "v. inMap", indvRange)
                if not isSeedRangeMapped:

                    # seed range ends before inMap range starts
                    if seed.stop <= indvRange.start:
                        dprint("seed range ends before inMap range starts, go next")

                    # seed range starts after inMap range stops, go next
                    elif seed.start >= indvRange.stop:
                        dprint("seed range starts after inMap range stops, go next")

                    # seed range starts before inMap range starts
                    elif seed.start <= indvRange.start:
                        dprint("seed range starts before inMap range starts")

                        # seed range ends before inMap range ends, so first part falls off
                        if seed.stop <= indvRange.stop:
                            dprint("seed range ends before inMap range ends")
                            outMap = mapOfRanges[1][k]
                            diff = outMap.start - indvRange.start
                            dprint("diff = ", diff)
                            outputRange = range(
                                indvRange.start + diff, seed.stop + diff
                            )
                            dprint("pass on to next inputs", outputRange)
                            outputs[i + 1].append(outputRange)
                            isSeedRangeMapped = True
                            if (seed.start != indvRange.start):
                                falloff = range(
                                    seed.start, indvRange.start
                                )
                                dprint("send over falloff", falloff, "to seed pile")
                                outputs[i].append(falloff)

                        elif seed.stop >= indvRange.stop:
                            dprint("seed range ends after inMap range ends, so falls off end and start")
                            outMap = mapOfRanges[1][k]
                            diff = outMap.stop - indvRange.stop
                            dprint("map to", mapOfRanges[1][k])
                            dprint("diff = ", diff)
                            outputRange = range(
                                seed.start + diff, indvRange.stop + diff
                            )
                            dprint("pass on to next inputs", outputRange)
                            outputs[i + 1].append(outputRange)
                            isSeedRangeMapped = True

                            if seed.start != indvRange.start:
                                underfalloff = range(
                                    seed.start, indvRange.start
                                )
                                dprint("send under falloff", underfalloff, "to seed pile")
                                outputs[i].append(underfalloff)

                            if seed.stop != indvRange.stop:
                                overfalloff = range(
                                    indvRange.stop, seed.stop
                                )
                                dprint("send over falloff", overfalloff, "to seed pile")
                                outputs[i].append(overfalloff)

                    # seed range starts after inMap range starts
                    elif seed.start > indvRange.start:
                        dprint("seed range starts after inMap range starts")

                        if seed.stop <= indvRange.stop:
                            dprint("seed range ends in inMap range, so fits in")
                            outMap = mapOfRanges[1][k]
                            diff = outMap.start - indvRange.start

                            outputRange = range(
                                seed.start + diff, seed.stop + diff
                            )
                            dprint("pass on to next inputs", outputRange)
                            outputs[i + 1].append(outputRange)

                            isSeedRangeMapped = True

                        elif seed.stop >= indvRange.stop:
                            dprint("seed range ends after inMap range, send over falloff to pile")

                            outMap = mapOfRanges[1][k]
                            diff = outMap.start - indvRange.start

                            outputRange = range(
                                seed.start + diff, indvRange.stop + diff
                            )
                            dprint("pass on to next inputs", outputRange)
                            outputs[i + 1].append(outputRange)

                            overFalloff = range(
                                indvRange.stop, seed.stop
                            )
                            dprint("send over falloff to seed pile", overFalloff)
                            outputs[i].append(overFalloff)
                            isSeedRangeMapped = True

                k += 1

            if not isSeedRangeMapped:
                dprint("no matches found, pass as is")
                outputs[i + 1].append(seed)

            j += 1

        i += 1

    locs = outputs[6]

    lowest = outputs[7][0].start

    for o in outputs[7]:
        dprint(o)
        if lowest > o.start >= 0:
            lowest = o.start
    dprint("")

    print("Lowest ", lowest)
    if lowest != 46:
        print("FAIL!")
    else:
        print("PASS!")


def getMappedValues(outputRange, index):
    return outputRange[index]


def sumOfRanges(rangeArray):
    total = 0
    for ranger in rangeArray:
        total += len(ranger)

    return total


def calculateRangeOfValues(start, length):
    stop = start + length
    return range(start, stop)


def isValueInRange(valueRange, value):
    if value in valueRange:
        return valueRange.index(value)
    else:
        return -1


def splitRange(start, reach):
    ranges = []
    halfReachEven = reach % 2
    if halfReachEven == 0:
        halfReach = int(reach / 2)
        ranges.append(range(start, start + halfReach))
        ranges.append(range(start + halfReach, start + halfReach + halfReach))
    else:
        halfReach = int((reach - 1) / 2)
        ranges.append(range(start, start + halfReach))
        ranges.append(range(start + halfReach, start + halfReach + halfReach + 1))

    return ranges

def dprint(self, *args):
    debug = True
    if debug:
        print(self, *args)



if __name__ == '__main__':
    main()
