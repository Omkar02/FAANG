# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()
cnt = [0]


"Diameter of a Binary Tree"


def DBT(root, ans):
    if not root:
        return 0

    lheight = DBT(root.lChild, ans)

    rheight = DBT(root.rChild, ans)

    ans[0] = max(ans[0], 1 + lheight + rheight)

    return 1 + max(lheight,
                   rheight)


# print(DBT(readyTree.getHead(), [float('-inf')]))


"BST Contains Dead End"


def deadEnd(root, Min, Max):
    if root == None:
        return False

    if Min == Max:
        return True

    return (deadEnd(root.lChild, Min, root.data - 1) or
            deadEnd(root.rChild, root.data + 1, Max))


# print(deadEnd(readyTree.getHead(), float('-inf'), float('inf')))


"Count BST nodes that lie in a given range"


def nRange(node, rMin, rMax):
    if not node:
        return 0

    val = node.data

    if val == rMax and val == rMin:
        return 1

    # root.data <= high and root.data >= low
    if val <= rMax and val >= rMin:
        return 1 + nRange(node.lChild, rMin, rMax) + nRange(node.rChild, rMin, rMax)

    elif val < rMin:
        return nRange(node.rChild, rMin, rMax)

    else:
        return nRange(node.lChild, rMin, rMax)


# print(nRange(readyTree.getHead(), 2, 8))


"K’th smallest element in BST using"


def kSmall(node, idx, k):
    if not node:
        return (None, idx)
    left, idx = kSmall(node.lChild, idx, k)
    if left:
        return (left, idx)

    idx += 1
    if idx == k:
        return (node.data, idx)
    return kSmall(node.rChild, idx, k)


k = 4
# print(kSmall(readyTree.getHead(), 0, k))
