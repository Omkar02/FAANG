# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree
import sys

readyTree.printTree()


def findClosest(head, target):
    closestVal = sys.maxsize
    node = head
    while node:
        if abs(target - closestVal) > abs(target - node.data):
            closestVal = node.data
        currVal = node.data
        if target < currVal:
            node = node.lChild
        elif target > currVal:
            node = node.rChild
        else:
            return node.data
    return closestVal


print(findClosest(readyTree.getHead(), 4))
