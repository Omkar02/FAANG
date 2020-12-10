# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree
readyTree.printTree()

ans = []


def boundryScan(node):
    if not node:
        return
    ans.append(node.data)
    isLeft(node.lChild)

    isLeaf(node.lChild)
    isLeaf(node.rChild)

    isRight(node.rChild)


def isLeft(node):
    if not node:
        return

    if node.lChild:
        ans.append(node.data)
        isLeft(node.lChild)
    elif node.rChild:
        ans.append(node.data)
        isLeft(node.rChild)


def isRight(node):
    if not node:
        return
    if node.rChild:
        isRight(node.rChild)
        ans.append(node.data)
    elif node.lChild:
        isRight(node.lChild)
        ans.append(node.lChild)


def isLeaf(node):
    if not node:
        return
    isLeaf(node.lChild)

    if not node.lChild and not node.rChild:
        ans.append(node.data)

    isLeaf(node.rChild)


boundryScan(readyTree.getHead())
print(ans)
