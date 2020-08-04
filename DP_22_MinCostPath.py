import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def minCostPath(paths):
    dp = [[0 for x in range(len(paths[0]))]for y in range(len(paths))]
    totalVal = paths[-1][-1]
    i, j = len(paths) - 1, len(paths[0]) - 1
    seq = []

    while True:
        seq.append([i, j])
        if i > 0 and j > 0 and paths[i - 1][j] < paths[i][j - 1]:
            totalVal += paths[i - 1][j]
            i -= 1

        elif i > 0 and j > 0 and paths[i - 1][j] > paths[i][j - 1]:
            totalVal += paths[i][j - 1]
            j -= 1

        else:
            seq.append([0, 0])
            totalVal += paths[0][0]
            break

    return totalVal, list(reversed(seq))


def getMinNeigh(dp, i, j):
    return (dp[i + 1][j], i + 1, j) if dp[i + 1][j] < dp[i][j + 1] else (dp[i][j + 1], i, j + 1)


allPaths = [[1, 3, 5, 8],
            [4, 2, 1, 7],
            [4, 3, 2, 3]]


print(minCostPath(allPaths))
