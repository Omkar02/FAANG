import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


# '''
# The painter’s partition problem
# We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit
# time to paint 1 unit of board. The problem is to find the minimum time to get
# this job done under the constraints that any painter will only paint continuous sections of boards,
# say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.

# Examples:

# Input : k = 2, A = {10, 10, 10, 10}
# Output : 20.
# Here we can divide the boards into 2
# equal sized partitions, so each painter
# gets 20 units of board and the total
# time taken is 20.

# '''


def sum(arr, frm, to):
    total = 0
    for i in range(frm, to + 1):
        total += arr[i]
        print('     ', arr[frm:to + 1])
    return total


def paintersProblem(arr, lengthOfarray, kPainter):
    dp = [[0 for i in range(lengthOfarray + 1)] for j in range(kPainter + 1)]

    # print('---for K = 1')
    for i in range(1, lengthOfarray + 1):
        dp[1][i] = sum(arr, 0, i - 1)
    # [print(x) for x in dp]
    # print('---for n = 1')
    for i in range(1, kPainter + 1):
        dp[i][1] = arr[0]
    [print(x) for x in dp]

    for i in range(2, kPainter + 1):
        for j in range(2, lengthOfarray + 1):
            bestSoFar = float('inf')
            for painter in range(1, j + 1):
                # print(f'-------{bestSoFar}---{dp[i - 1][painter]}---{sum(arr, painter, j - 1)}')
                #------------------max the each painter and take their min-------------------
                bestSoFar = min(bestSoFar,
                                max(dp[i - 1][painter],  # preveious task the the same painter
                                    sum(arr, painter, j - 1)))  # task by a painter

            # [print(x) for x in dp]
            dp[i][j] = bestSoFar
    [print(x) for x in dp]

    return dp[kPainter][lengthOfarray]


arr = [10, 20, 60, 50, 30, 40]
n = len(arr)
k = 6
print(paintersProblem(arr, n, k))

# [0, 0, 0, 0, 0, 0, 0]
# [0, 10, 30, 90, 140, 170, 210]
# [0, 10, 0, 0, 0, 0, 0]
# [0, 10, 0, 0, 0, 0, 0]
# [0, 10, 0, 0, 0, 0, 0]
# [0, 10, 0, 0, 0, 0, 0]
# [0, 10, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]


# [0, 0, 0, 0, 0, 0, 0]
# [0, 10, 30, 90, 140, 170, 210]
# [0, 10, 20, 60, 90, 90, 120]
# [0, 10, 20, 60, 60, 80, 90]
# [0, 10, 20, 60, 60, 60, 70]
# [0, 10, 20, 60, 60, 60, 60]
# [0, 10, 20, 60, 60, 60, 60]
# 60
