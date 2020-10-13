# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class earth:
    def __init__(self, ocean):
        self.ocean = ocean
        self.rowLen = len(self.ocean)
        self.colLen = len(self.ocean[0])
        self.pacific = set()
        self.atlantic = set()

    def pacificAtlantic(self):
        for r in range(self.rowLen):
            self.calculateFlow(self.pacific, r, 0)
            self.calculateFlow(self.atlantic, r, self.rowLen - 1)

        for c in range(self.colLen):
            self.calculateFlow(self.pacific, 0, c)
            self.calculateFlow(self.atlantic, self.colLen - 1, c)

        return list(self.pacific.intersection(self.atlantic))

    def calculateFlow(self, water, r, c):
        water.add((r, c))
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rowRange = range(self.rowLen)
        colRange = range(self.colLen)
        for dx, dy in direction:
            new_x, new_y = r + dx, c + dy
            if new_x in rowRange and new_y in colRange and (new_x, new_y) not in water and self.ocean[new_x][new_y] >= self.ocean[r][c]:
                self.calculateFlow(water, new_x, new_y)


ocean = [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]]
e = earth(ocean)
cal = e.pacificAtlantic()
cal = sorted(cal)
ans = sorted(list(map(tuple, [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])))
print(cal == ans)
