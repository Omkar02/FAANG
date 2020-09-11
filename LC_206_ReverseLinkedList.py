# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Easy')


from Datastruct.masterLinkedList import l


def reverseList(l):
    p1, p2 = None, l.getHead()

    while p2 is not None:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3

    l.head = p1
    l.traverseList()


arr = [1, 2, 3, 4, 5]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)
reverseList(l)
