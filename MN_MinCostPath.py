# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def minCostPath(board):
    row, col = len(board), len(board[0])
    dp = [[0 for _ in range(col)]for _ in range(row)]

    dp[0][0] = board[0][0]

    for i in range(1, col):
        dp[0][i] = board[0][i] + dp[0][i - 1]

    for j in range(1, row):
        dp[j][0] = board[j][0] + dp[j - 1][0]

    for x in range(1, row):
        for y in range(col):
            dp[x][y] = board[x][y] + min(dp[x - 1][y],
                                         dp[x - 1][y - 1],
                                         dp[x][y - 1])
    return dp[-1][-1]


board = [[1, 3, 5, 8],
         [4, 2, 1, 7],
         [4, 3, 2, 3]]
print(minCostPath(board))
