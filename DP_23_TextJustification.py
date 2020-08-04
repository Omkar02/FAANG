import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
the cost is calculated by the sum of the space left products
"""


def minLineText(textList, limit):
    dp = [[-1 for i in range(len(textList))]for j in range(len(textList))]

    for i in range(len(textList)):
        dp[i][i] = limit - len(textList[i])
        for j in range(i + 1, len(textList)):
            dp[i][j] = dp[i][j - 1] - len(textList[j]) - 1

    # [print(x)for x in dp]
    # print()

    for i in range(len(textList)):
        for j in range(i, len(textList)):
            if dp[i][j] < 0:
                dp[i][j] = float('inf')
            else:
                dp[i][j] = dp[i][j]**2
    # [print(x)for x in dp]

    minCost = [0] * len(textList)
    result = [-1] * len(textList)

    for i in range(len(textList) - 1, -1, -1):
        minCost[i] = dp[i][len(textList) - 1]
        result[i] = len(textList)
        for j in range(len(textList) - 1, i, -1):
            if dp[i][j - 1] == float('inf'):
                continue
            if minCost[i] > minCost[j] + dp[i][j - 1]:
                minCost[i] = minCost[j] + dp[i][j - 1]
                result[i] = j
    print(minCost)
    print(result)


limit = 10
textList = ['Tushar', 'Roy', 'Likes', 'To', 'Code']
print(minLineText(textList, limit))
