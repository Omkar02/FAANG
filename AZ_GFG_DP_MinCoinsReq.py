# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def minCoins(denomitaion, target):
    dp = [float('inf') for _ in range(0, target + 1)]
    dp[0] = 0

    for den in denomitaion:
        for amm in range(target + 1):
            if den <= amm:
                dp[amm] = min(dp[amm], 1 + dp[amm - den])
    return dp[target]


def minCoins(denomitaion, target):
    dp = [float('inf') for _ in range(0, target + 1)]
    dp[0] = 0

    for den in denomitaion:
        for amm in range(target + 1):
            if den <= amm:
                dp[amm] = min(dp[amm], 1 + dp[amm - den])
    return dp[target]


denomitaion = [1, 2, 3]
target = 13
print(minCoins(denomitaion, target))
