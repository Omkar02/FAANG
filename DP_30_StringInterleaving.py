import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def isWoven(one, two, three):
    if len(one) + len(two) != len(three):
        return False

    dp = [[False for i in range(len(one) + 1)]for j in range(len(two) + 1)]
    dp[0][0] = True

    for i in range(1, len(one) + 1):
        dp[0][i] = True if one[i - 1] == three[i - 1] else False

    for j in range(1, len(two) + 1):
        dp[j][0] = True if two[j - 1] == three[j - 1] else False

    for i in range(1, len(two) + 1):
        for j in range(1, len(one) + 1):
            if three[i + j - 1] == two[i - 1]:
                dp[i][j] = True if dp[i - 1][j] else False
            if three[i + j - 1] == one[j - 1]:
                dp[i][j] = True if dp[i][j - 1] else False
    # [print(x) for x in dp]
    return dp[-1][-1]


three = 'aaxaby'
one = 'aab'
two = 'axy'

three = 'aaafaaa'
one = 'aaa'
two = 'aaaf'

print(isWoven(one, two, three))
