import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
fromula :
    if st1[i] == st2[j]:
        dp[i][j] = 1+dp[i-1][j-1]
    else:
        dp[i][j] = 0
"""


def londestCommonSubstring(stringOne, stringTwo):
    dp = [[0 for i in range(len(stringOne) + 1)]for j in range(len(stringTwo) + 1)]
    maxSumSoFar = [-1, -1]
    maxVaule = 0

    for i in range(1, len(stringTwo) + 1):
        for j in range(1, len(stringOne) + 1):
            if stringOne[j - 1] == stringTwo[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if maxVaule < dp[i][j]:
                    maxVaule = dp[i][j]
                    maxSumSoFar = [i, j]

            else:
                dp[i][j] = 0
    [print(x) for x in dp]

    return maxVaule, buildSeq(dp, maxSumSoFar, stringOne)


def buildSeq(dp, maxIdx, string):
    seq = []
    i, j = maxIdx
    while i > 0:
        if dp[i][j] != 0:
            seq.append(string[i - 1])
            i -= 1
            j -= 1
        else:
            break
    return ''.join(reversed(seq))


stringOne = 'abcdaf'
stringTwo = 'zbcdf'

print('--->', londestCommonSubstring(stringOne, stringTwo))
