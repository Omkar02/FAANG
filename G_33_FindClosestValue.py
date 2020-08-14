import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import tree


def findClosest(node, target, closest):
    while node is not None:
        if abs(target - closest) > abs(target - node.data):
            if node.data != None:
                closest = node.data

        if target < node.data:
            node = node.lChild

        elif target > node.data:
            node = node.rChild

        else:
            closest = node.data
            break

    return closest


import random
arr = [5, 6, 7, 8, 9, 3, 2, 1, 10]
random.shuffle(arr)

for i in arr:
    tree.insert(i)

tree.printTree()
target = 10
closest = float('inf')
head = tree.getHead()
print(f'The closest = {findClosest(head, target, closest)}')
