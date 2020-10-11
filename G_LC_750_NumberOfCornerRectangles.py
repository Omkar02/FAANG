# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def countRectangel(grid):
    coordsTable, coords = getCoordsTable(grid)
    return getRectangelCount(coords, coordsTable)


def getCoordsTable(grid):
    coordsTable = {}
    coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                coordsTable[(r, c)] = True
                coords.append((r, c))
    return coordsTable, coords


def getRectangelCount(coords, coordsTable):
    rectangleCount = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isInUpperRight([x1, y1], [x2, y2]):
                continue

            if (x1, y2) in coordsTable and (x2, y1) in coordsTable:
                rectangleCount += 1
    return rectangleCount


def isInUpperRight(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return x2 > x1 and y1 > y2


grid = [[1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]]


grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
print(countRectangel(grid))
