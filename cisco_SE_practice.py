# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def houseRobbery(num):
    temp = num[:]
    temp[1] = max(temp[0], temp[1])
    n = len(num)
    for i in range(1, n):
        temp[i] = max(temp[i - 1], temp[i - 2] + num[i])
    return temp[-1]


num = [1, 2, 3, 1]
num = [2, 7, 9, 3, 1]
# print(houseRobbery(num))


def sort_by_parity(num):
    return sorted(num, key=lambda a: a % 2)


num = [3, 1, 2, 4]
# print(sort_by_parity(num))


def maxSubarray(num):
    overAllMax = float('-inf')
    currMax = 0
    for i in num:
        print(i)
        currMax += i
        overAllMax = max(overAllMax, currMax)
        if currMax < 0:
            currMax = 0
    return overAllMax


num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maxSubarray(num))

# from Datastruct.masterTree import readyTree
# import sys
# readyTree.printTree()


def findtheClosest(node, target):
    return _theClosest(node, target, sys.maxsize)


def _theClosest(node, target, cVal):
    if not node:
        print(cVal)
        return cVal

    if abs(target - cVal) > abs(target - node.data):
        if node.data != None:
            cVal = node.data
    if target < node.data:
        _theClosest(node.lChild, target, cVal)
    elif target > node.data:

        _theClosest(node.rChild, target, cVal)
    else:
        print(cVal, '-')


# print(findtheClosest(readyTree.getHead(), 4))


def branchSum(node):
    if not node:
        return []
    sums = []
    _helBranch(node, sums, 0)
    return sums


def _helBranch(node, sums, runningSum):
    if not node:
        return
    newRunningSum = runningSum + node.data
    if not node.lChild and not node.rChild:
        sums.append(newRunningSum)
    _helBranch(node.lChild, sums, newRunningSum)
    _helBranch(node.rChild, sums, newRunningSum)


# print(branchSum(readyTree.getHead()))

def nodeDepth(node, depth):
    if not node:
        return 0
    depth += nodeDepth(node.lChild, depth + 1) + nodeDepth(node.rChild, depth + 1)
    return depth


# print(nodeDepth(readyTree.getHead(), 0))


def productSum(arr, multiplier=1):
    total = 0
    for val in arr:
        if type(val) is list:
            total += productSum(val, multiplier + 1)
        else:
            total += val
    return total * multiplier


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# print(productSum(arr))
