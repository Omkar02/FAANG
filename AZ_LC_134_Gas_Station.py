# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def canCompleteCircuit(gas, cost):
    n = len(gas)
    tank = 0
    diffSum = 0
    start = 0

    for i in range(n):
        tank += (gas[i] - cost[i])
        diffSum += (gas[i] - cost[i])
        if tank < 0:
            start = i + 1
            tank = 0

    return start if start < n and diffSum >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
