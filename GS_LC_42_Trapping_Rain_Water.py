# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Hard')
cnt = [0]


def rainWater(walls):
    n = len(walls)
    cWater = 0
    i, j = 0, n - 1
    lMax, rMax = walls[i], walls[j]
    while i < j:
        lMax, rMax = max(lMax, walls[i]), max(rMax, walls[j])
        if lMax <= rMax:
            cWater += lMax - walls[i]
            i += 1
        else:
            cWater += rMax - walls[j]
            j -= 1
    return cWater


walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# walls = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(rainWater(walls))
print(cnt)
