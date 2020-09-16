# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l


def hasCycle(linkedList):
    first = linkedList.getHead().nextNode
    second = linkedList.getHead().nextNode.nextNode

    while first != second:
        if not second:
            return
        first = first.nextNode
        second = second.nextNode.nextNode
        print(f'{first.data} | {second.data}')

    first = linkedList.getHead()

    while first != second:
        first = first.nextNode
        second = second.nextNode

    return first.data


arr = [0, 1, 2, 4, 10, 5, 6, 7, 8, 9]
for i in arr:
    l.insertStart(i)
l.insertLoop()

print(f'The Loop starts = {hasCycle(l)}')
