# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l, r


def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    p1 = l1.getHead()
    p2 = l2.getHead()
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

    l1.head = l1.getHead() if l1.getHead().data < l2.getHead().data else l2.getHead()
    l1.traverseList()


arr = [1, 3, 6]
arr2 = [2, 4, 5]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)
for j in arr2:
    r.insertStart(j)


mergeTwoLists(l, r)
