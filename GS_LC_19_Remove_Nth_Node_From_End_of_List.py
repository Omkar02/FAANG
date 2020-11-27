# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l


def removeN_node(lList, n):
    if not n:
        return
    head = lList.getHead()
    p1 = p2 = head

    while n:
        p2 = p2.nextNode
        n -= 1
        if not p2 and n:
            return - 1
    if not p2:
        lList.head = p1.nextNode
        lList.traverseList()
        return

    while p2.nextNode:
        p1 = p1.nextNode
        p2 = p2.nextNode

    p1.nextNode = p1.nextNode.nextNode
    lList.traverseList()


head = [1, 2, 3, 4, 5]
n = 2
[l.insertStart(i) for i in head]
removeN_node(l, 0)
