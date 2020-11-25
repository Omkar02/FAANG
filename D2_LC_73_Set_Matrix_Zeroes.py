# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def matrixZeros(mat):
    histRow, histCol = set(), set()
    row = len(mat)
    col = len(mat[0])
    for r in range(row):
        for c in range(col):
            if mat[r][c] == 0:
                histRow.add(r)
                histCol.add(c)

    for r in range(row):
        for c in range(col):
            if r in histRow or c in histCol:
                mat[r][c] = 0


mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
matrixZeros(mat)
[print(x)for x in mat]
