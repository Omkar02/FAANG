import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')

from Datastruct.masterLinkedList import l


arr = [1, 2, 3, 4, 5]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)


def shiftLinkedList(linkedList, k):
    head = linkedList.getHead()
    tail = head
    length = 1

    while tail.nextNode is not None:
        tail = tail.nextNode
        length += 1

    offset = abs(k) % length
    if offset == 0:
        return linkedList

    newOffset = length - offset if k > 0 else offset

    newtail = head
    for i in range(1, newOffset):
        newtail = newtail.nextNode

    newHead = newtail.nextNode
    newtail.nextNode = None
    tail.nextNode = head

    linkedList.head = newHead

    linkedList.traverseList()


k = 3

shiftLinkedList(l, k)
