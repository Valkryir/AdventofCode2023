def main():

    raceResults = open('input.txt').readlines()

    times = []
    dists = []
    waysToWin = []
    margin = 1

    acceleration = 1

    #strip and clean
    for entry in raceResults[0].split(":")[1].split():
        times.append(int(entry))

    for entry in raceResults[1].split(":")[1].split():
        dists.append(int(entry))

    #do some stuff per race
    for raceIndex in range(len(times)):
        print("race", raceIndex)
        raceTime = times[raceIndex]
        raceDist = dists[raceIndex]
        waysToWin.append([])

        for buttonHeldTime in range(0, raceTime+1):
            print("try holding button for", buttonHeldTime)
            speed = buttonHeldTime * acceleration
            print("boat will move", speed, "mm per ms")
            timeToMove = raceTime - buttonHeldTime
            print("boat can travel for", timeToMove, "ms")
            distance = timeToMove * speed
            print("boat will go", distance, "mm")

            if distance > raceDist:
                waysToWin[raceIndex].append(buttonHeldTime)

        margin *= len(waysToWin[raceIndex])

    print(margin)


if __name__ == '__main__':
    main()