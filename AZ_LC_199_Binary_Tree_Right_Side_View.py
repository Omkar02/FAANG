# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')
from Datastruct.masterTree import readyTree
readyTree.printTree()


def rightSideView(root):
    if not root:
        return
    ans = []
    q = [root]
    while q:
        ans.append(q[0].data)
        newQ = []
        for node in q:
            if node.lChild:
                newQ.append(node.lChild)
            if node.rChild:
                newQ.append(node.rChild)
        q = newQ
    return ans


print(rightSideView(readyTree.getHead()))
