# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def isBalanced(node):
    if not node:
        return True

    leftDepth = getDepth(node.lChild)
    rightDepth = getDepth(node.rChild)

    return abs(leftDepth - rightDepth) <= 1 and isBalanced(node.lChild) and isBalanced(node.rChild)


def getDepth(node):
    if not node:
        return 0

    return max(getDepth(node.lChild), getDepth(node.rChild)) + 1


print(isBalanced(readyTree.getHead()))
