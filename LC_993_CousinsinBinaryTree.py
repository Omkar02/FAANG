# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


def isCousins(childOne, childTwo, head):
    if not childOne or not childTwo:
        return -1

    childOneHeight = getHeight(childOne, head, 0)
    childTwoHeight = getHeight(childTwo, head, 0)
    print(childOneHeight, childTwoHeight)
    sameParent = getParent(head, childOne, childTwo)

    return True if childOneHeight == childTwoHeight and not sameParent else False


def getParent(head, childOne, childTwo):
    if not head:
        return False

    a = head.lChild.data == childOne and head.rChild.data == childTwo if head.lChild and head.rChild else False
    b = head.lChild.data == childTwo and head.rChild.data == childOne if head.lChild and head.rChild else False

    return a or b or getParent(head.lChild, childOne, childTwo) or getParent(head.rChild, childOne, childTwo)


def getHeight(val, node, depth):
    if not node:
        return 0
    if val == node.data:
        return depth

    l = getHeight(val, node.lChild, depth + 1)
    r = getHeight(val, node.rChild, depth + 1)

    return l if l != 0 else r


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


nodeOne = 7
nodeTwo = 1
print(f'Is Cousin = {isCousins(nodeOne,nodeTwo,readyTree.getHead())}')
