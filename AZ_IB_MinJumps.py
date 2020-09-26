# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


arr = [1, 1, 1, 1, 4]


def getMinJump(arr):
    if arr[0] == 0:
        return 'inf'
    maxReach = steps = arr[0]
    jumps = 0
    n = len(arr)
    ans = []
    for i in range(1, n - 1):

        maxReach = max(maxReach, arr[i] + i)
        steps -= 1

        if not steps:
            jumps += 1
            steps = maxReach - i

        if i >= maxReach:
            return -1
    return jumps + 1


print(getMinJump(arr))
