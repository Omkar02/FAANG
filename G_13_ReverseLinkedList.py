# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')

from Datastruct.masterLinkedList import l


arr = [1, 2, 3, 4, 5]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)


def reverseLinkedList(linkedList):
    p1, p2 = None, linkedList.getHead()
    l.traverseList()
    while p2 is not None:
        p3 = p2.nextNode
        p2.nextNode = p1
        p1 = p2
        p2 = p3
    linkedList.head = p1
    l.traverseList()


reverseLinkedList(l)
