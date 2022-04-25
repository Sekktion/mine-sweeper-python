def generateMap(mapSize):
    playMap = []
    row = []
    for i in range(0,mapSize):
        for j in range(0,mapSize):
            row.append("0")
        playMap.append(row)
        row = []

    return playMap