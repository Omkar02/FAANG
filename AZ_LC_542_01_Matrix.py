# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


# BFS
class board:
    def __init__(self, mat):
        self.mat = mat
        self.distance = [[float('-inf') for y in x] for x in self.mat]
        self.rowLen = len(self.mat)
        self.colLen = len(self.mat[0])
        self.direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def getDistance(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if self.mat[r][c]:
                    self._bfs_helper(r, c)
        [print(x) for x in self.mat]

    def _bfs_helper(self, row, col):
        rowRange = range(self.rowLen)
        colRange = range(self.colLen)
        stack = [[row, col, 0]]
        while stack:
            r, c, dVal = stack.pop(0)
            if not self.mat[r][c]:
                self.mat[row][col] = dVal
                return 0

            for dRow, dCol in self.direction:
                newR = dRow + r
                newC = dCol + c
                if newR in rowRange and newC in colRange:
                    stack.append((newR, newC, dVal + 1))


mat = [[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]]

# Output = [[0, 0, 0],
#           [0, 1, 0],
#           [0, 0, 0]]

b = board(mat)
b.getDistance()
