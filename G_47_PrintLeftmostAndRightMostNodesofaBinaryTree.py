# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()

# put 0 and len(n) nodes only


def leftAndRightMost(node):
    if not node:
        return

    q = [node]
    res = []
    while q:
        n = len(q)
        for i in range(n):
            currNode = q.pop(0)
            if i == 0 or i == n - 1:
                res.append(currNode.data)

            if currNode.lChild:
                q.append(currNode.lChild)

            if currNode.rChild:
                q.append(currNode.rChild)
    return res


print(f'The left and right most are = {leftAndRightMost(readyTree.getHead())}')
