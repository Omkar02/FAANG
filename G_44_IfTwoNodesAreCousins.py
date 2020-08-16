# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def isCousin(valueOne, valueTwo, head):
    if not head:
        return -1

    heightOne = getHeight(valueOne, head, 0)
    heightTwo = getHeight(valueTwo, head, 0)

    sameParent = getParent(head, valueOne, valueTwo)

    if heightOne == heightTwo and not sameParent:
        return True

    return False


def getHeight(val, node, depth):
    if not node:
        return 0
    if val == node.data:
        return depth
    left = getHeight(val, node.lChild, depth + 1)
    return left if left != 0 else getHeight(val, node.rChild, depth + 1)


def getParent(root, a, b):
    if not root:
        return
    return ((root.lChild == a and root.rChild == b) or
            (root.lChild == b and root.rChild == a) or
            getParent(root.lChild, a, b) or
            getParent(root.rChild, a, b))


nodeOne = 3
nodeTwo = 7
print(f'Is Cousin = {isCousin(nodeOne,nodeTwo,readyTree.getHead())}')
