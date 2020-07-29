import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

"""
formula :
    if Subset[i]>target[j]:
        dp[i][j]  = dp[i-1][j]
    else:
        dp[i][j] = dp[i-1][j] if dp[i-1][j]== True else dp[i-1][j-target[j]]
"""


def subsetSum(subset, target):
    dp = [[False for x in range(target + 1)]for y in range(len(subset) + 1)]
    for i in range(len(subset) + 1):
        dp[i][0] = True

    for i in range(1, len(subset) + 1):
        for j in range(1, target + 1):
            if j >= subset[i - 1]:
                dp[i][j] = dp[i - 1][j] if dp[i - 1][j] == True else dp[i - 1][j - subset[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # [print(x)for x in dp]

    return dp[-1][-1], buildSeq(dp, subset, target)


def buildSeq(dp, subset, target):
    i, j = len(dp) - 1, len(dp[0]) - 1
    seq = []
    while i > 0:
        if dp[i][j] != dp[i - 1][j]:
            seq.append(subset[i - 1])
            j -= subset[i - 1]

        i -= 1
    return seq


subset = [2, 3, 7, 8, 10]
target = 11

print(subsetSum(subset, target))
