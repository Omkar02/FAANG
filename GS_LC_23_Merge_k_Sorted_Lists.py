# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Linked-List', Difficult='Hard')


from Datastruct.masterLinkedList import l, v, r, m


i, j, k = [1, 4, 5], [1, 3, 4], [2, 6]
[l.insertStart(a) for a in i]
[v.insertStart(a) for a in j]
[r.insertStart(a) for a in k]


def mergeK_linked_list(allHeads, m):
    priorityQueu = []
    for l in allHeads:
        if l:
            priorityQueu.append((l.data, l))

    while priorityQueu:
        priorityQueu.sort(key=lambda a: a[0])
        val, node = priorityQueu.pop(0)
        m.insertStart(val)
        node = node.nextNode
        if node:
            priorityQueu.append((node.data, node))
    print(m.traverseList())


allHeads = [l.getHead(), v.getHead(), r.getHead()]
mergeK_linked_list(allHeads, m)
