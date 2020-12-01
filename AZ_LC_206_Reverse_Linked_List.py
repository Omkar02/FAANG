# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Easy')

from Datastruct.masterLinkedList import l


def reverse(lis):
    head = lis.getHead()
    p1, p2 = None, head

    while p2:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3
    lis.head = p1
    lis.traverseList()


a = [1, 2, 3, 4, 5]
[l.insertStart(i) for i in a]
reverse(l)
