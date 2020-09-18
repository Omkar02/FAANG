# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def minPathSum(grid):
    dp = [[0 for x in grid[0]] for y in grid]

    for x in range(len(grid[0])):

        if x != 0:
            print(dp[0][x - 1], grid[0][x], dp[0][x])
            dp[0][x] = dp[0][x - 1] + grid[0][x]
        else:
            dp[0][x] = grid[0][0]

    for y in range(1, len(grid)):
        dp[y][0] = dp[y - 1][0] + grid[y][0]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j],
                                        dp[i][j - 1])
    [print(x) for x in dp]

    return dp[-1][-1]


grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

print(minPathSum(grid))
