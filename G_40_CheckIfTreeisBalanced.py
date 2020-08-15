import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')


from Datastruct.masterTree import readyTree, tree


def isBalanced(node):
    if not node:
        return True

    lHeight = getHeight(node.lChild)
    rHeight = getHeight(node.rChild)

    if (abs(lHeight - rHeight) <= 1) and isBalanced(node.lChild) and isBalanced(node.rChild):
        return True

    return False


def getHeight(node):
    if not node:
        return 0

    return max(getHeight(node.lChild), getHeight(node.rChild)) + 1


print(isBalanced(readyTree.getHead()))

arr = [6, 2, 4, 6, 7, 2, 1, 10]


for i in arr:
    tree.insert(i)

# tree.printTree()
print(isBalanced(tree.getHead()))
