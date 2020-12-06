import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def cityScheduling(costs):
    costs = sorted(costs, key=lambda x: x[0] - x[1])
    idx = 0
    half = len(costs) // 2
    totalCost = 0
    for aCost, bCost in costs:
        totalCost += aCost if idx < half else bCost
        idx += 1
    return totalCost


cost = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(cityScheduling(cost))
