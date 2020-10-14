# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')
import math


def numSquares(n):
    dp = [float("inf") for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        # print(i)
        for j in range(1, int(math.sqrt(i)) + 1):
            # print('\t', j)
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp


n = 12
print(numSquares(n))
