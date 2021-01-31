# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# ---------------------------------------------- #
def kadensAlgo(arr):
    print('--- Kadens Algo ---')
    maxSum = float('-inf')
    currSum = 0
    l = r = 0
    n = len(arr)
    tmpIdx = 0
    for i in range(n):
        currSum += arr[i]

        if currSum > maxSum:
            maxSum = currSum
            l = tmpIdx
            r = i

        if currSum < 0:
            tmpIdx = i + 1
            currSum = 0
    return maxSum, arr[l:r + 1]


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(kadensAlgo(arr))

# ---------------------------------------------- #


class earth:
    def __init__(self, land):
        print('--- River Size ---')
        self.land = land
        self.allRiver = []
        self.visited = set()
        self.rowLen = len(land)
        self.colLen = len(land[0])
        self.currSize = 0
        self.getAllrivers()

    def getAllrivers(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if self.land[r][c] == 1:
                    self.calculateSize((r, c))
                    if self.currSize:
                        self.allRiver.append(self.currSize)
                        self.currSize = 0

    def calculateSize(self, cord):
        if cord in self.visited:
            return
        self.currSize += 1
        self.visited.add(cord)
        neighbours = self.getNeighbour(cord)
        for n in neighbours:
            self.calculateSize(n)

    def getNeighbour(self, cord):
        neig = []
        rowRange = range(0, self.rowLen)
        colRange = range(0, self.colLen)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in direction:
            newR, newC = cord[0] + d[0], cord[1] + d[1]
            if (newR in rowRange and newC in colRange) and (self.land[newR][newC] == 1):
                # if (newR, newC) not in self.visited:
                neig.append((newR, newC))
        return neig


land = [[1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]]
# e = earth(land)
# print(e.allRiver)
# [2, 1, 5, 2, 2]

# ---------------------------------------------- #


def isOneCycle(arr):
    print('--- Single Cycle Exitance --- ')
    n = len(arr)
    countElement = currIdx = 0

    while countElement < n:
        if countElement > 0 and currIdx == 0:
            return False
        countElement += 1
        currIdx = getNextIdx(currIdx, arr)
    return currIdx == 0


def getNextIdx(idx, arr):
    jump = arr[idx]
    nextIdx = (jump + idx) % len(arr)
    return nextIdx


# arr = [2, 3, 1, -4, -4, 2]
# print(isOneCycle(arr))
