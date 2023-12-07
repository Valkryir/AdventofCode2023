def main():

    raceResults = open('input.txt').readlines()

    times = ""
    dists = ""
    waysToWin = []
    margin = 1

    acceleration = 1

    #strip and clean
    for entry in raceResults[0].split(":")[1].split():
        times += entry

    for entry in raceResults[1].split(":")[1].split():
        dists += entry

    times = int(times)
    dists = int(dists)

    #do some stuff per race
    raceTime = times
    raceDist = dists

    for buttonHeldTime in range(0, raceTime+1):
        speed = buttonHeldTime * acceleration
        timeToMove = raceTime - buttonHeldTime
        distance = timeToMove * speed

        if distance > raceDist:
            waysToWin.append(buttonHeldTime)


    print(len(waysToWin))


if __name__ == '__main__':
    main()