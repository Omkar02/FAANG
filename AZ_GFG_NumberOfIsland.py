# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class earth:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rowLen = len(self.matrix)
        self.colLen = len(self.matrix[0])
        self.visited = set()
        self.numberOfIsland = 0

    def getIsland(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if (r, c) not in self.visited and self.matrix[r][c] == '1':
                    self.depthFirstSearch(r, c)
                    self.numberOfIsland += 1

    def depthFirstSearch(self, row, col):
        if (row, col) in self.visited:
            return

        self.visited.add((row, col))
        neighbour = self.getNeighbour(row, col)

        for surrounding in neighbour:
            self.depthFirstSearch(surrounding[0], surrounding[1])

    def getNeighbour(self, r, c):
        rowRange = range(0, self.rowLen)
        colRange = range(0, self.colLen)

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        neighbour = []
        for paths in direction:
            newR, newC = r + paths[0], c + paths[1]
            if (newR in rowRange and newC in colRange) and (self.matrix[newR][newC] == '1'):
                neighbour.append([newR, newC])
        return neighbour


area = [['1', '1', '1', '0'],
        ['1', '1', '0', '0'],
        ['0', '0', '0', '1'],
        ['1', '0', '1', '1']]
e = earth(area)
e.getIsland()

[print(x) for x in e.matrix]
print(e.numberOfIsland)
