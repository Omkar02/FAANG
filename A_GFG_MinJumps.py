# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def getMinJumps(array):
    steps = maxReach = array[0]
    jumps = 0
    n = len(array)
    currMax = float('-inf')
    for i in range(1, n - 1):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            steps = maxReach - i
            jumps += 1

        if i >= maxReach:
            return 'inf'
    return jumps + 1


array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(getMinJumps(array))
