# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def minJumps(jumps):
    n = len(jumps)
    maxReach = steps = jumps[0]
    j = 0
    for i in range(1, n - 1):
        steps -= 1
        maxReach = max(maxReach, jumps[i] + i)
        if not steps:
            j += 1
            steps = maxReach - i
        if i >= maxReach:
            return -1
    return j + 1


jumps = [1, 0, 3, 4]
print(minJumps(jumps))
