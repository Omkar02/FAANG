# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def isSymmetric(root):
    return check(root, root)


def check(nodeOne, nodeTwo):
    if not nodeOne and not nodeTwo:
        return True

    if not nodeOne or not nodeTwo:
        return False

    return nodeOne.data == nodeTwo.data and check(nodeOne.rChild, nodeTwo.lChild) and check(nodeOne.lChild, nodeTwo.rChild)


print(isSymmetric(readyTree.getHead()))
