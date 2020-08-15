# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree

# aka sum of all depths


def nodeDepth(head):
    return getnodeDepth(head, 0)


def getnodeDepth(node, depth):
    if not node:
        return 0

    depth += getnodeDepth(node.lChild, depth + 1) + getnodeDepth(node.rChild, depth + 1)
    return depth


readyTree.printTree()

print(f'Node depth = {nodeDepth(readyTree.getHead())}')
