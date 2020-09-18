# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def levelOrder(root):
    q = [root]
    res = []
    while q:
        temp = []
        size = len(q)
        for _ in range(size):
            currNode = q.pop(0)
            temp.append(currNode.data)

            if currNode.lChild:
                q.append(currNode.lChild)

            if currNode.rChild:
                q.append(currNode.rChild)

        res.append(temp)
    return res


readyTree.printTree()
print(levelOrder(readyTree.getHead()))
