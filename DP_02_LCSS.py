import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
if string1[i]==string2[j]:
    dp[i][j] == 1+dp[i-1][j-1]
else:
    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
"""


def LongestCommonSeq(sOne, sTwo):
    dp = [[0 for i in range(len(sOne) + 1)]for j in range(len(sTwo) + 1)]

    for i in range(1, len(sTwo) + 1):
        for j in range(1, len(sOne) + 1):
            if sTwo[i - 1] == sOne[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # [print(x) for x in dp]

    return f'The longest Val = {dp[-1][-1]} | The String = {buildSeq(dp, sOne, sTwo)}'


def buildSeq(dp, sOne, sTwo):
    i = len(dp) - 1
    j = len(dp[0]) - 1
    seq = []

    while i > 0:
        if dp[i][j] - 1 == dp[i - 1][j - 1]:
            seq.append(sOne[i])
            i -= 1
            j -= 1
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
    return ''.join(seq)


sOne = 'abcdaf'
sTwo = 'acbcf'
print(LongestCommonSeq(sOne, sTwo))
