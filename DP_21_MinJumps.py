import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def minJumps(jumps):
    pos = [None for i in range(len(jumps))]
    maxReach = jumps[0]
    steps = jumps[0]
    currPos = 0
    prevPos = -1
    noJumps = 0
    for i in range(1, len(jumps)):
        steps -= 1
        maxReach = max(maxReach, jumps[i] + i)
        if steps == 0:
            noJumps += 1
            steps = maxReach - i
            pos[i] = currPos
            currPos = i
        prevPos = currPos
    pos[-1] = prevPos
    print(noJumps + 1, pos)


# jumps = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
jumps = [1, 3, 5, 3, 2, 2, 6, 1, 6, 8, 9]
print(minJumps(jumps))
