# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def pathSum(root, target):
    if not root:
        return False
    if root.data == target and not root.lChild and not root.rChild:
        return True

    return pathSum(root.lChild, target - root.data) or pathSum(root.rChild, target - root.data)


print(pathSum(readyTree.getHead(), 9))
