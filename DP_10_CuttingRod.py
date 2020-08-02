import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

'''
formula
    if j >= i:
        dp[i][j] = max(dp[i - 1][j],
                       val[i] + dp[i][j - 1])
    else:
        dp[i][j] = dp[i - 1][j]
'''


def cuttingRod(lenRod, cost):
    dp = [0 for i in range(lenRod + 1)]

    for lenght in range(1, lenRod + 1):
        maxVal = float('-inf')
        for j in range(1, lenght + 1):
            maxVal = max(maxVal, cost[j - 1] + dp[lenght - j])
        dp[lenght] = maxVal
    return dp[-1]


lenRod = 8
cost = [3, 5, 8, 9, 10, 20, 22, 25]
print(cuttingRod(lenRod, cost))
