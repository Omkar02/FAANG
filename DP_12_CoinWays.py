import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def coinWays(coins, target):
    dp = [[1 if i == 0 else 0 for i in range(target + 1)]for j in range(len(coins))]

    for i in range(len(coins)):
        for j in range(target + 1):
            if j >= coins[i]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    [print(x) for x in dp]
    return dp[-1][-1]


coins = [1, 2, 3]
target = 5
print(coinWays(coins, target))
