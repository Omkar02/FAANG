import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def getVertical(node, depth, veNode):
    if not node:
        return

    if depth not in veNode:
        veNode[depth] = []
    veNode[depth].append(node.data)

    getVertical(node.lChild, depth - 1, veNode)
    getVertical(node.rChild, depth + 1, veNode)

    return veNode


readyTree.printTree()
order = getVertical(readyTree.getHead(), 0, {})

for i in sorted(order):
    print(order[i])
