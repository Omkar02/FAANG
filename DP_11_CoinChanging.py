import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
formula
    dp[i] = min(dp[i],dp[i-coun[j]])
"""


def coinChange(target, coins):
    dp = [float('inf') for i in range(0, target + 1)]
    dp[0] = 0

    for denom in coins:
        for j in range(target + 1):
            if denom <= j:
                dp[j] = min(dp[j], 1 + dp[j - denom])
    return dp[target]


target = 13
coins = [7, 2, 3, 6]

print(coinChange(target, coins))
