import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')

from Datastruct.masterLinkedList import l


arr = [0, 1, 2, 4, 10, 5, 6, 7, 8, 9]
for i in arr:
    l.insertStart(i)
l.insertLoop()


def findLoop(head):
    first = head.nextNode
    second = head.nextNode.nextNode

    while first != second:
        if second:
            first = first.nextNode
            second = second.nextNode.nextNode

        else:
            return

    first = head
    while first != second:
        first = first.nextNode
        second = second.nextNode

    return first.data


print(findLoop(l.getHead()))
