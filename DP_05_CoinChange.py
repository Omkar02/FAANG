import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
formula :\
    if j >= coins[i]:
        if dp[j] > 1 + dp[j - coins[i]]:
            dp[j] = 1 + dp[j - coins[i]]
            position[j] = i

"""


def minCoin(coins, target):
    dp = [float('inf') for i in range(target + 1)]
    dp[0] = 0
    position = [None for i in range(target + 1)]

    for i in range(len(coins)):
        for j in range(target + 1):
            if j >= coins[i]:
                if dp[j] > 1 + dp[j - coins[i]]:
                    dp[j] = 1 + dp[j - coins[i]]
                    position[j] = i
                # dp[j] = min(dp[j], 1 + dp[j - i])

    return dp[target], buildSeq(position, coins)


def buildSeq(position, coins):
    seq = []
    start = len(position) - 1
    while start != 0:
        j = position[start]
        seq.append(coins[j])
        start -= coins[j]

    return seq


coins = [1, 5, 6, 8]
target = 50
print(minCoin(coins, target))
