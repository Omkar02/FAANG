# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def validTree(tree):
    return isValid(tree.getHead(), float('-inf'), float('inf'))


def isValid(node, minVal, maxVal):
    if not node:
        return True

    val = node.data
    if val <= minVal or val >= maxVal:
        return False
    return isValid(node.rChild, val, maxVal) or isValid(node.lChild, minVal, val)


print(validTree(readyTree))
