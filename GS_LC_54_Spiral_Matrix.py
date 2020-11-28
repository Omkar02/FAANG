# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def spiralTraverse(mat):
    if not mat:
        return 0
    ans = []
    sRow, eRow = 0, len(mat) - 1
    sCols, eCols = 0, len(mat[0]) - 1

    while sRow <= eRow and sCols <= eCols:

        for c in range(sCols, eCols + 1):
            ans.append(mat[sRow][c])

        for r in range(sRow + 1, eRow + 1):
            ans.append(mat[r][eCols])

        for c in reversed(range(sCols, eCols)):
            ans.append(mat[eRow][c])

        for r in reversed(range(sRow + 1, eRow)):
            ans.append(mat[r][sCols])
        sRow += 1
        eRow -= 1
        sCols += 1
        eCols -= 1

    return ans


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(spiralTraverse(mat))


def spiralTraverse(mat):
    if not mat:
        return -1

    out = []
    sRow, eRow = 0, len(mat) - 1
    sCol, eCol = 0, len(mat[0]) - 1

    while sRow <= eRow and sCol <= eCol:

        for c in range(sCol, eCol + 1):
            out.append(mat[sRow][c])

        for r in range(sRow + 1, eRow + 1):
            out.append(mat[r][eCol])

        for c in reversed(range(sCol, eCol)):
            out.append(mat[eRow][c])

        for r in reversed(range(sRow + 1, eRow)):
            out.append(mat[r][sCol])

        sRow += 1
        eRow -= 1
        sCol += 1
        eCol -= 1
    return out


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(spiralTraverse(mat))
