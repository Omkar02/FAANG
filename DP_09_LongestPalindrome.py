"""
----there is diff in seq and sustring
     --seq means non-continuse
     ---substring is contineouse
"""
import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
Formula =
    if s[i]==s[j]:
        dp[i][j] = 2+ d[i+1][j-1] the left-down one
    else:
        dp[i][j] = max(dp[i][j-1],dp[i+1][j])the left and the dowm
"""


def longPaliSeq(string):
    n = len(string)
    dp = [[0 for i in range(n)]for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for gap in range(2, n + 1):
        for i in range(n + 1 - gap):
            j = gap + i - 1

            if string[i] == string[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1],
                               dp[i + 1][j])
    [print(X) for X in dp]
    return dp[0][-1], buildSeq(dp, string)


def buildSeq(dp, string):
    seq = []
    i, j = 0, len(string) - 1
    while j > 0:
        if dp[i][j] != dp[i][j - 1] and dp[i][j] != dp[i + 1][j]:

            seq.append(string[j]) if string[j] not in seq else ''

            if dp[i][j] - 2 != dp[i + 1][j - 1]:
                break
            i += 1
            j -= 1

        if dp[i][j] == dp[i + 1][j]:
            seq.append(string[j])if string[j] not in seq else ''
            i += 1

        if dp[i][j] == dp[i][j - 1]:
            j = -1

    return seq


string = 'agbdba'
print(longPaliSeq(string))
