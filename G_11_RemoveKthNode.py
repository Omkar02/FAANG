import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')

from Datastruct.masterLinkedList import l


arr = [1, 2, 3, 4, 5, 6]
# arr = [1, 2]
for i in arr:
    l.insertStart(i)

# l.traverseList()



def removeKNodeFromEnd(head, k):
    print(f'Removed {k} node: ',end = '')
    first = head
    second = head
    count = 1
    while count <= k and second is not None:
        second = second.nextNode
        count += 1

    if second is None:
        head.data = first.nextNode.data
        head.nextNode = first.nextNode.nextNode
        l.traverseList()
        return

    while second.nextNode is not None:
        second = second.nextNode
        first = first.nextNode

    first.nextNode = first.nextNode.nextNode
    l.traverseList()


removeKNodeFromEnd(l.getHead(), 3)
