# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')

from Datastruct.masterLinkedList import l


def rotate(l, k):

    size = l.size
    k = k % size

    if k == 0:
        l.traverseList()
        return
    p1 = p2 = l.getHead()
    c = 0
    while c < k:
        p2 = p2.nextNode
        c += 1

    while p2.nextNode is not None:
        p1 = p1.nextNode
        p2 = p2.nextNode
    temp = p1.nextNode
    p1.nextNode = None
    prevHead = l.getHead()

    l.head = temp
    p2.nextNode = prevHead
    l.traverseList()


arr = [1, 2, 3, 4, 5]
k = 10
[l.insertStart(x) for x in arr]
l.traverseList()


rotate(l, k)
