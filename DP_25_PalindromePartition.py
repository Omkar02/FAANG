import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def paligromePartion(string):
    n = len(string)
    dp = [[False for i in range(n)]for j in range(n)]

    for i in range(n):
        dp[i][i] = True

    for gap in range(2, n + 1):
        for i in range(0, n - gap):
            j = i + gap - 1

            if gap == 2:
                dp[i][j] = string[i] == string[j]
            else:
                dp[i][j] = string[i] == string[j] and dp[i + 1][j - 1]
    [print(x) for x in dp]

    cuts = [float("inf") for _ in range(n)]
    for i in range(n):
        if dp[0][i]:
            cuts[i] = 0
        else:
            for j in range(1, i + 1):
                if dp[j][i]:
                    cuts[i] = min(cuts[i], 1 + cuts[j - 1])

    print(cuts)
    return(cuts[-1])


string = 'abcbm'
print(paligromePartion(string))

#     a b c b m
# a
# b
# c
# b
# m
