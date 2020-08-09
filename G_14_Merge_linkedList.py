import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')

from Datastruct.masterLinkedList import l, r


arr = [1, 3, 6]
arr2 = [2, 4, 5]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)
for j in arr2:
    r.insertStart(j)

# l.traverseList()
# r.traverseList()


def mergeLinkedList(listOne, listTwo):
    p1 = listOne.getHead()
    p2 = listTwo.getHead()
    p3 = None

    while p1 is not None and p2 is not None:
        if p1.data < p2.data:
            p3 = p1
            p1 = p1.nextNode
        else:
            if p3 is not None:
                p3.nextNode = p2
            p3 = p2
            p2 = p2.nextNode
            p3.nextNode = p1
        if p1 is None:
            p3.nextNode = p2

    listOne.head = listOne.getHead() if listOne.getHead().data < listTwo.getHead().data else listTwo.getHead()
    listOne.traverseList()


mergeLinkedList(l, r)
