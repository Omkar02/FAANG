# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l
[l.insertStart(i) for i in range(1, 6)]
l.traverseList()


def reverseList(llist):
    p1, p2 = None, llist.getHead()
    while p2 is not None:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3
    llist.head = p1
    llist.traverseList()


reverseList(l)
