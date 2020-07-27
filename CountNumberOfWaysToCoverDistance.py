import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# 1, 2 and 3 steps.
# n = 3


def numberWays(steps, distPoint):
    ways = [0 for x in range(distPoint + 1)]
    ways[0] = 1
    for i in range(1, distPoint + 1):
        for j in range(len(steps)):
            if i >= steps[j]:
                ways[i] += ways[i - steps[j]]
    return ways[distPoint]


print(numberWays([1, 2, 3], 3))
