# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def getDiagnols(node, depth, diNode):
    if not node:
        return

    if depth not in diNode:
        diNode[depth] = []
    diNode[depth].append(node.data)

    getDiagnols(node.lChild, depth + 1, diNode)
    getDiagnols(node.rChild, depth, diNode)

    return diNode


print(getDiagnols(readyTree.getHead(), 0, {}))
