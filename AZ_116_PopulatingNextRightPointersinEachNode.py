# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


def connect(root):
    if not root:
        return None

    q = [root]
    while q:
        size = len(q)
        for i in range(size):
            node = q.pop(0)

            if i < size - 1:
                node.next = q[0]

            if node.lChild:
                q.append(node.lChild)

            if node.rChild:
                q.append(node.rChild)
