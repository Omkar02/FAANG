# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()


def maxAveragesubtree(root, maxAvg):
    if not root:
        return (0, 0)

    rVal = root.data
    lSum, lCnt = maxAveragesubtree(root.lChild, maxAvg)
    rSum, rCnt = maxAveragesubtree(root.rChild, maxAvg)
    totalSum = rVal + lSum + rSum
    totalCnt = lCnt + rCnt + 1

    currAvg = totalSum / totalCnt
    maxAvg[0] = max(maxAvg[0], currAvg)

    return totalSum, totalCnt


maxAvg = [float('-inf')]
maxAveragesubtree(readyTree.getHead(), maxAvg)
print(maxAvg)
