# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')

from Datastruct.masterTree import readyTree


def maxPathSum(node):
    _, maxSum = findMaxSum(node)
    return maxSum


def findMaxSum(node):
    if not node:
        return(0, 0)
    lmbs, lmps = findMaxSum(node.lChild)
    rmbs, rmps = findMaxSum(node.rChild)

    mbs = max(lmbs, rmbs)
    val = node.data

    msb = max(mbs + val, val)
    msr = max(lmbs + val + rmbs, msb)
    mps = max(lmps, rmps, msr)

    return (msb, mps)


readyTree.printTree()
print(maxPathSum(readyTree.getHead()))
