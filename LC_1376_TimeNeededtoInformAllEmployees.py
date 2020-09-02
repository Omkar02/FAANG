import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


def numOfMinutes(n, headID, manager, informTime):
    levelMap = {}
    for i in range(n):
        if manager[i] not in levelMap:

            levelMap[manager[i]] = []
        levelMap[manager[i]].append(i)
    print(f'levelMap = {levelMap}')
    time = 0

    maxTime = float('-inf')
    q = [(-1, 0)]

    while q:

        currNode, currTime = q.pop(0)
        maxTime = max(maxTime, currTime)
        if currNode in levelMap:
            for subWorker in levelMap[currNode]:
                q.append((subWorker, currTime + informTime[subWorker]))
    return maxTime


n = 7
headID = 6
manager = [1, 2, 3, 4, 5, 6, -1]
informTime = [0, 6, 5, 4, 3, 2, 1]

n = 6
headID = 2
manager = [2, 2, -1, 2, 2, 2]
informTime = [0, 0, 1, 0, 0, 0]
print(numOfMinutes(n, headID, manager, informTime))
