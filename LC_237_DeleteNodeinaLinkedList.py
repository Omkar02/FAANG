import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l


def deleteNode(l, target):
    node = l.getHead()

    if target == node.data:
        temp = node.nextNode
        l.head = temp
        return

    while node.nextNode.data != target:
        if not node.nextNode:
            node.nextNode = None
            return
        else:
            node = node.nextNode

    node.nextNode = node.nextNode.nextNode


arr = [4, 5, 1, 9]
target = 5

for x in arr:
    l.insertStart(x)

deleteNode(l, target)
l.traverseList()
