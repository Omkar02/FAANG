# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import tree


def branchSum(head):
    sums = []
    runningSum = 0
    getBranchSum(head, runningSum, sums)

    return sums


def getBranchSum(node, runningSum, sums):
    if not node:
        return

    newRunningSum = runningSum + node.data
    if not node.lChild and not node.rChild:
        sums.append(newRunningSum)
        return

    getBranchSum(node.lChild, newRunningSum, sums)
    getBranchSum(node.rChild, newRunningSum, sums)


array = [6, 2, 1, 3, 5, 8, 7, 9, 10]

for i in array:
    tree.insert(i)
tree.printTree()

print(f'The branchSum = {branchSum(tree.getHead())}')
