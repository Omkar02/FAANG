# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


class numMatrix:
    def __init__(self, mat):
        self.mat = mat
        self.rowLen = len(mat)
        self.colLen = len(mat[0])
        self.ans = 0

    def sumRange(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        for r in range(x1, x2 + 1):
            for c in range(y1, y2 + 1):
                self.ans += self.mat[r][c]

        return self.ans


mat = [[3, 0, 1, 4, 2],
       [5, 6, 3, 2, 1],
       [1, 2, 0, 1, 5],
       [4, 1, 0, 1, 7],
       [1, 0, 3, 0, 5]]

p1 = (2, 1)
p2 = (4, 3)

p1 = (1, 1)
p2 = (2, 2)
n = numMatrix(mat)
print(n.sumRange(p1, p2))
