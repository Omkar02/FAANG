import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# formula:
#     points = [A1, A2, ....., An]
#     [Ai, Aj]

#     option1 = Ai + min(dp[i + 2][j],
#                        dp[i + 1][j - 1])

#     option2 = Aj + min(dp[i + 1][j - 1],
#                        dp[i][j - 2])

#     dp[i][j] = max(option2, option1)


def optimalGame(points):
    n = len(points)
    dp = [[points[i] if i == j else -1 for i in range(n)]for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i > j:
                dp[i][j] = 0

    for length in range(n):
        for j in range(length, n):
            i = j - length
            x = 0
            if i + 2 <= j:
                x = dp[i + 2][j]
            y = 0
            if i + 1 <= j - 1:
                y = dp[i + 1][j - 1]
            z = 0
            if i <= j - 2:
                z = dp[i][j - 2]
            option1 = points[i] + min(x, y)
            option2 = points[j] + min(y, z)
            dp[i][j] = max(option2, option1)
    [print(x) for x in dp]


points = [3, 9, 1, 2]
print(optimalGame(points))

# [3, 9, 4, 11]
# [0, 9, 9, 10]
# [0, 0, 1, 2]
# [0, 0, 0, 2]
