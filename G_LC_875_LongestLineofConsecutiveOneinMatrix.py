# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def longestLine(mat):
    currLineLength = 0
    maxLineLenght = float('-inf')
    rowLen = len(mat)
    colLen = len(mat[0])

    for r in range(rowLen):
        for c in range(colLen):
            currLineLength = getLineLen(mat, r, c)
            maxLineLenght = max(maxLineLenght, currLineLength)

    return maxLineLenght


def getLineLen(mat, r, c):
    len1 = 0
    for i in range(len(mat[0])):
        if i + c < len(mat[0]) and mat[r][c + i] == 1:
            len1 += 1
        else:
            break
    len2 = 0
    for i in range(len(mat)):
        if i + r < len(mat) and mat[r + i][c] != 1:
            len2 += 1
        else:
            break

    len3 = 0
    for i in range(max(len(mat[0]), len(mat))):
        if r + i < len(mat) and c + i < len(mat[0]) and mat[r + i][c + i] == 1:
            len3 += 1

        else:
            break

    len4 = 0
    for i in range(max(len(mat[0]), len(mat))):
        if r + i < len(mat) and c - i > 0 and mat[r + i][c - i] == 1:
            len4 += 1

        else:
            break

    return max(len1, len2, len3, len4)


mat = [[0, 1, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1]]

# mat = [[0, 0],
#        [1, 1]]
print(longestLine(mat))
