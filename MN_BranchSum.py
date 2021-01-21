# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree
# import sys

readyTree.printTree()


def branchSum(head):
    sums = []
    _helperBranchSum(node=head, sums=sums, rSum=0)
    return sums


def _helperBranchSum(node, sums, rSum):
    if not node:
        return
    cSum = node.data + rSum
    if not node.lChild and not node.rChild:
        sums.append(cSum)
        return
    _helperBranchSum(node.lChild, sums, cSum)
    _helperBranchSum(node.rChild, sums, cSum)


# print(branchSum(readyTree.getHead()))


def getTreeDepth(node):
    return _helperDepth(node, 0)


def _helperDepth(node, depth):
    if not node:
        return 0
    return depth + _helperDepth(node.lChild, depth + 1) + _helperDepth(node.rChild, depth + 1)


print(getTreeDepth(readyTree.getHead()))
