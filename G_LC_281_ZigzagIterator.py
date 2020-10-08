# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Medium')


from Datastruct.masterLinkedList import l, v


a = [1, 2, 7]
[l.insertStart(x) for x in a]
b = [3, 4, 5, 6]
[v.insertStart(x) for x in b]

l.traverseList()
v.traverseList()
# out = [1, 3, 2, 4, 5, 6]


def mergeZigZagList(l1, v1):
    if not l1:
        return v1
    if not v1:
        return l1
    if not l1 and not v1:
        return None
    l = l1.getHead()
    v = v1.getHead()
    p1 = l
    p2 = v
    p3 = None

    while p1 is not None and p2 is not None:
        p3 = p1.nextNode
        p1.nextNode = p2

        p1 = p2
        p2 = p3

    l1.traverseList()


mergeZigZagList(l, v)
