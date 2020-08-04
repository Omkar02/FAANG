import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxSubSquare(matrix):
    n = len(matrix[0])
    m = len(matrix)
    maxOfAll = 0
    index = [-1, -1]

    dp = [[0 for i in range(n + 1)]for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j],
                                   dp[i - 1][j - 1])

        if maxOfAll < dp[i][j]:
            maxOfAll = dp[i][j]
            index = [i - 1, j - 1]

    [print(x)for x in dp]
    return maxOfAll, index


matrix = [[0, 0, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1]]

print(maxSubSquare(matrix))
