# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


from Datastruct.masterLinkedList import l
[l.insertStart(x) for x in [1, 2, 3, 4, 5]]
l.traverseList()

# -------------------------------------------------------------#


def remove_k_node(head, k):
    print('--- Remove K Node from End --- ')
    p1 = head
    p2 = head

    while k >= 0:
        p2 = p2.nextNode
        k -= 1

    if not p2:
        head.data = p1.nextNode.data
        head.nextNode = p1.nextNode.nextNode
        return
    while p2.nextNode is not None:
        p2 = p2.nextNode
        p1 = p1.nextNode

    p1.nextNode = p1.nextNode.nextNode
    l.traverseList()


k = 3
# remove_k_node(l.getHead(), k)
# -------------------------------------------------------------#


def reverseLinkedList(lList):
    print('--- Reverse Linked List --- ')
    p1, p2 = None, lList.getHead()
    while p2 is not None:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3
    lList.head = p1
    lList.traverseList()


reverseLinkedList(l)
# -------------------------------------------------------------#
# -------------------------------------------------------------#
