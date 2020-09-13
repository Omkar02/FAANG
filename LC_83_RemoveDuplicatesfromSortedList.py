# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l


def deleteDuplicates(root):
    node = root.getHead()
    if not node:
        return

    while node is not None and node.nextNode is not None:
        if node.data == node.nextNode.data:
            node.nextNode = node.nextNode.nextNode

        else:
            node = node.nextNode

    root.traverseList()


arr = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6]

for x in arr:
    l.insertStart(x)


l.traverseList()
deleteDuplicates(l)
