import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import tree


def vaidateBst(root):
    return vaidateBstHelper(root, float('-inf'), float('inf'))


def vaidateBstHelper(node, minVal, maxval):
    print(minVal, maxval)
    if node is None:
        return True
    if node.data < minVal or node.data >= maxval:
        return False

    forLeft = vaidateBstHelper(node.lChild, minVal, node.data)
    forRight = vaidateBstHelper(node.rChild, node.data, maxval)
    return forLeft and forRight


import random
arr = [5, 6, 7, 8, 9, 3, 2, 1, 10]

random.shuffle(arr)
arr = [10, 1, 9, 3, 8, 7, 5, 6]
for i in arr:
    tree.insert(i)
print(vaidateBst(tree.getHead()))
tree.printTree()
