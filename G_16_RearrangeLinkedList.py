import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')

from Datastruct.masterLinkedList import l

arr = [3, 0, 5, 2, 1, 4]
k = 3

for i in arr:
    l.insertStart(i)


def rearrangeLinkedList(linkedList, k):
    smallHead = None
    smallTail = None
    equalHead = None
    equalTail = None
    greterHead = None
    greaterTail = None

    node = linkedList.getHead()

    while node is not None:
        if node.data < k:
            smallHead, smallTail = growList(smallHead, smallTail, node)
            # print(smallHead, smalltail)
        elif node.data > k:
            greterHead, greaterTail = growList(greterHead, greaterTail, node)
            # print(greterHead, greaterTail)
        else:
            equalHead, equalTail = growList(equalHead, equalTail, node)

        prevNode = node
        node = node.nextNode
        prevNode.nextNode = None

    firstHead, firstTail = connectLinkedList(smallHead, smallTail, equalHead, equalTail)
    finalHead, _ = connectLinkedList(firstHead, firstTail, greterHead, greaterTail)

    linkedList.head = finalHead


def growList(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node
    if tail is not None:
        tail.nextNode = node

    return (newHead, newTail)


def connectLinkedList(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.nextNode = headTwo

    return (newHead, newTail)


rearrangeLinkedList(l, k)
l.traverseList()
