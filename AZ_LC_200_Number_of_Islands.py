# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class earth:
    def __init__(self, pleatue):
        self.pleatue = pleatue
        self.visited = set()
        self.rowLen = len(self.pleatue)
        self.colLen = len(self.pleatue[0])
        self.noIsland = 0

    def countIsland(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if (r, c) not in self.visited and self.pleatue[r][c] == '1':
                    self.dfs(r, c)
                    self.noIsland += 1

        return self.noIsland

    def dfs(self, row, col):
        if (row, col) in self.visited:
            return

        self.visited.add((row, col))

        neighbour = self.getNeighbour(row, col)
        for r, c in neighbour:
            self.dfs(r, c)

    def getNeighbour(self, r, c):
        neighbour = []
        rowRange = range(0, self.rowLen)
        colRange = range(0, self.colLen)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in direction:
            newR, newC = r - d[0], c - d[1]
            if (newR in rowRange and newC in colRange) and (self.pleatue[newR][newC] == '1'):
                neighbour.append([newR, newC])
        return neighbour


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]]

# grid = [['1', '1', '1', '0'],
#         ['1', '1', '0', '0'],
#         ['0', '0', '0', '1'],
#         ['1', '0', '1', '1']]

e = earth(grid)
print(e.countIsland())
