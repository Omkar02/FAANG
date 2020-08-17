# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def diagonalSum(node, verticalDistance, SumsDict):
    if not node:
        return
    if verticalDistance not in SumsDict:
        SumsDict[verticalDistance] = 0
    SumsDict[verticalDistance] += node.data

    diagonalSum(node.lChild, verticalDistance + 1, SumsDict)
    diagonalSum(node.rChild, verticalDistance, SumsDict)

    return SumsDict


SumsDict = {}
print(f'the diagonalSum = {diagonalSum(readyTree.getHead(),0,SumsDict)}')
