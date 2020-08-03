import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def minCostPath(paths):
    path = [[0, 0]]
    i, j = 0, 0
    val = 0
    while i < len(paths) - 2 or j < len(paths[0]):
        print(i, j, f'----------------{i}{j}-------------')

        least, i, j = getMinNeigh(paths, i, j)
        val += least
        path.append([i, j])
    print(path, val)


def getMinNeigh(dp, i, j):
    return (dp[i + 1][j], i + 1, j) if dp[i + 1][j] < dp[i][j + 1] else (dp[i][j + 1], i, j + 1)


allPaths = [[1, 3, 3, 1],
            [4, 2, 1, 1],
            [4, 3, 2, 30]]


print(minCostPath(allPaths))
