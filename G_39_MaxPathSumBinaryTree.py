import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')


from Datastruct.masterTree import readyTree

# readyTree.printTree()
#   __6_
#  /    \
#  2    8
# / \  / \
# 1 3  7 9_
#    \     \
#    5    10


def maxPathSum(node):
    _, maxSum = getMaxPathSum(node)
    return maxSum


def getMaxPathSum(node):
    if not node:
        return (0, 0)

    leftMaxAsBranch, leftMaxAsPath = getMaxPathSum(node.lChild)
    rightMaxAsBranch, rightMaxAaPath = getMaxPathSum(node.rChild)

    maxChildSum = max(leftMaxAsBranch, rightMaxAsBranch)

    value = node.data
    maxBranchSum = max(value, maxChildSum + value)
    maxIncRoot = max(maxBranchSum, leftMaxAsBranch + value + rightMaxAsBranch)

    maxOverall = max(leftMaxAsPath, rightMaxAaPath, maxIncRoot)

    return (maxBranchSum, maxOverall)


print(f'MaxPath  = {maxPathSum(readyTree.getHead())}')
