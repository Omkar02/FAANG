# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def maxSquareSumMatrix(mat):
    row, col = len(mat), len(mat[0])
    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    maxVal = float('-inf')
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            dp[r][c] = mat[r - 1][c - 1] + min(dp[r - 1][c],
                                               dp[r - 1][c - 1],
                                               dp[r][c - 1])
            maxVal = max(maxVal, dp[r][c])
    return maxVal


mat = [[0, 0, 1, 1, 1],
       [1, 0, 1, 1, 1],
       [0, 1, 1, 1, 1],
       [1, 0, 1, 1, 1]]
# print(maxSquareSumMatrix(mat))
