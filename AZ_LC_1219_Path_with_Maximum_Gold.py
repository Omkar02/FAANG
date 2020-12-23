# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


class gold_mine:
    def __init__(self, mine):
        self.mine = mine
        self.rowLen = len(self.mine)
        self.colLen = len(self.mine[0])
        self.visited = set()
        self.maxVal = float('-inf')
        self.curMax = 0
        self.path = None
        self.tePath = []

    def getMaxPath(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if self.mine[r][c] != 0:
                    self.curMax = 0
                    self.dfs(r, c)
                    # self.maxVal = max(self.maxVal, self.curMax)
                    if self.curMax > self.maxVal:
                        self.maxVal = self.curMax
                        self.path = self.tePath[::]
                    self.visited = set()
                    self.tePath = []
        return self.maxVal

    def dfs(self, row, col):
        if (row, col) in self.visited:
            return

        self.visited.add((row, col))
        self.curMax += self.mine[row][col]
        self.tePath.append(self.mine[row][col])
        print(self.curMax, self.tePath)

        neighbours = self.getNeigh(row, col)
        for neighR, neighC in neighbours:
            self.dfs(neighR, neighC)

    def getNeigh(self, row, col):
        rowRange = range(self.rowLen)
        colRange = range(self.colLen)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        neighbours = []
        for x, y in directions:
            newR, newC = row + x, col + y
            # if r < 0 or r >= rows or c < 0 or c >= cols
            if newR in rowRange and newC in colRange and self.mine[newR][newC] != 0 and (newR, newC) not in self.visited:
                neighbours.append((newR, newC))

        return neighbours


mine = [[0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]]
g = gold_mine(mine)
print(g.getMaxPath())
print(g.path)
