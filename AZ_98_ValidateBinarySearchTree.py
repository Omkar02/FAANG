# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def isValidBST(root):
    return checkBST(root)


def checkBST(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True

    val = node.data
    if val <= low or val >= high:
        return False

    if not checkBST(node.rChild, val, high):
        return False

    if not checkBST(node.lChild, low, val):
        return False

    return True


# readyTree.printTree()
print(isValidBST(readyTree.getHead()))
