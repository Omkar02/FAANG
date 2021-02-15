# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()
cnt = [0]


"Print a Binary Tree in Vertical Order"


def BTVO(node, level, ans):
    cnt[0] += 1
    if not node:
        return

    if level not in ans:
        ans[level] = []

    ans[level].append(node.data)

    BTVO(node.lChild, level - 1, ans)
    BTVO(node.rChild, level + 1, ans)


ans = {}
# BTVO(readyTree.getHead(), 0, ans)
# print(ans)
# print(cnt)

"Level Order Traversal in Spiral Form"


def LOTS(node):
    one = [node]
    two = []
    ans = []
    while len(one) != 0 or len(two) != 0:
        while len(one) != 0:
            te = one.pop()
            ans.append(te.data)
            if te.rChild:
                two.append(te.rChild)
            if te.lChild:
                two.append(te.lChild)

        while len(two) != 0:
            te = two.pop()
            ans.append(te.data)
            if te.lChild:
                one.append(te.lChild)
            if te.rChild:
                one.append(te.rChild)

    return ans


print(LOTS(readyTree.getHead()))

"Connect Nodes at same Level (Level Order Traversal)"


def CNSL(node):

    queue = []
    queue.append(node)
    queue.append(None)
    while queue:
        p = queue.pop(0)
        if p:
            p.nextRight = queue[0]
            print(f'{p.data} -- > {p.nextRight.data if p.nextRight else None}')
            if p.lChild:
                queue.append(p.lChild)
            if p.rChild:
                queue.append(p.rChild)
        elif queue:
            queue.append(None)


# val = readyTree.getHead()
# # CNSL(val)
# ans(val)
