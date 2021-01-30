# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def spiralTraverse(mat):
    res = []
    startRow, endRow = 0, len(mat) - 1
    startCol, endCol = 0, len(mat[0]) - 1

    while startRow <= endRow and startCol <= endCol:

        for col in range(startCol, endCol + 1):
            res.append(mat[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            res.append(mat[row][endCol])
        for col in reversed(range(startCol, endCol)):
            res.append(mat[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            res.append(mat[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    return res


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]
print(spiralTraverse(mat))
