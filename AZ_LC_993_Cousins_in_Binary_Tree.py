import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def findCousin(root, c1, c2):
    if not c1 or not c2:
        return False

    cOne = getHeight(c1, root, 0)
    cTwo = getHeight(c2, root, 0)

    sameParent = getParent(root, c1, c2)

    return True if cOne == cTwo and not sameParent else False


def getHeight(node, head, depth):
    if not head:
        return 0

    if node == head.data:
        return depth
    l = getHeight(node, head.lChild, depth + 1)
    r = getHeight(node, head.rChild, depth + 1)

    return l if not l else r


def getParent(head, c1, c2):
    if not head:
        return False
    a = head.lChild.data == c1 and head.rChild.data == c2 if head.lChild and head.rChild else False
    b = head.lChild.data == c2 and head.rChild.data == c1 if head.lChild and head.rChild else False

    return a or b or getParent(head.lChild, c1, c2) or getParent(head.rChild, c1, c2)


nodeOne = 7
nodeTwo = 1
print(f'Is Cousin = {findCousin(readyTree.getHead(),nodeOne,nodeTwo)}')
