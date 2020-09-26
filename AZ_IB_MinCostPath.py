# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


board = [[1, 3, 2],
         [4, 3, 1],
         [5, 6, 1]]

# board = [[1, 2, 3],
#          [4, 8, 2],
#          [1, 5, 3]]


def minPath(board):
    r, c = len(board), len(board[0])
    dp = [[0 for _ in range(c)]for _ in range(r)]

    dp[0][0] = board[0][0]
    for row in range(1, r):
        dp[row][0] = dp[row - 1][0] + board[row][0]
    for col in range(1, c):
        dp[0][col] = dp[0][col - 1] + board[0][col]

    for row in range(1, r):
        for col in range(1, c):
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + board[row][col]
    [print(x) for x in dp]

    return dp[-1][-1]


print(minPath(board))
