import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


# Formula :


def eggDroping(noEggs, nofloar):
    dp = [[i if j == 1 else 0 for i in range(nofloar + 1)]for j in range(noEggs + 1)]
    [print(x)for x in dp]

    for i in range(2, noEggs + 1):
        for j in range(1, nofloar + 1):
            for k in range(1, j + 1):
                print([i - 1, k - 1], [i, j - k], [i, j, k])
            dp[i][j] = min(1 + max(dp[i - 1][k - 1],
                                   dp[i][j - k]) for k in range(1, j + 1))
    print()
    [print(x)for x in dp]


noEggs = 2
nofloar = 6
print(eggDroping(noEggs, nofloar))
