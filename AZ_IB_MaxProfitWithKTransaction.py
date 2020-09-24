# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def maxProfit(price, k):
    n = len(price)
    dp = [[0 for i in range(n)] for j in range(k + 1)]

    for tr in range(1, k + 1):
        currMax = float('-inf')
        for d in range(1, n):
            currMax = max(currMax, dp[tr - 1][d - 1] - price[d - 1])
            dp[tr][d] = max(dp[tr][d - 1], currMax + price[d])

    return dp[-1][-1]


price = [3, 2, 6, 5, 0, 3]
k = 2

print(maxProfit(price, k))
