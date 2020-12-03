# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def averageOfLevels(root):
    if not root:
        return []
    avg = []
    q = [root]
    while q:
        avg.append(sum(n.data for n in q) / len(q))
        t = []
        for node in q:
            if node.lChild:
                t.append(node.lChild)
            if node.rChild:
                t.append(node.rChild)
        q = t
    return avg


print(averageOfLevels(readyTree.getHead()))
