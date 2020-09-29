# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Hard')


class matrix:
    def __init__(self, mat):
        self.mat = mat
        self.rowLen = len(self.mat)
        self.colLen = len(self.mat[0])

    def update(self, r, c, val):
        self.mat[r][c] = val

    def sumRange(self, startRow, startCol, endRow, endCol):
        totalSum = 0
        rowRange = range(startRow, endRow + 1)
        colRange = range(startCol, endCol + 1)
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if r in rowRange and c in colRange:
                    totalSum += self.mat[r][c]
        return totalSum


mat = [[3, 0, 1, 4, 2],
       [5, 6, 3, 2, 1],
       [1, 2, 0, 1, 5],
       [4, 1, 0, 1, 7],
       [1, 0, 3, 0, 5]]
m = matrix(mat)

print(m.sumRange(2, 1, 4, 3))
m.update(3, 2, 2)
print(m.sumRange(2, 1, 4, 3))
