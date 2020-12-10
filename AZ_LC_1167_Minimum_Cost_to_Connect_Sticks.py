# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def minCostToConn(sticks):
    q = sticks
    cost = 0
    while len(q) > 1:
        q.sort()
        stickOne = q.pop(0)
        stickTwo = q.pop(0)
        cost += stickOne + stickTwo
        q.append(stickOne + stickTwo)

    return cost


sticks = [2, 4, 3]
sticks = [1, 8, 3, 5]
print(minCostToConn(sticks))
