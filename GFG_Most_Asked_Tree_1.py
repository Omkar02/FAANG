# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree

cnt = [0]

"------------------------------ Tree ------------------------------"

"Left View of Binary Tree"


def LVBT(node, level, maxLevel):

    cnt[0] += 1
    if not node:
        return
    if level > maxLevel[0]:
        print(node.data)
        maxLevel[0] = level

    LVBT(node.lChild, level + 1, maxLevel)
    LVBT(node.rChild, level + 1, maxLevel)


# print(LVBT(readyTree.getHead(), 1, [0]))
# print(cnt)

"Check if a binary tree is BST or not"


def isBST(node):
    maxVal = float('inf')
    minVal = float('-inf')
    return _hIsBST(node, minVal, maxVal)


def _hIsBST(node, minVal, maxVal):
    cnt[0] += 1
    if not node:
        return True

    if node.data > maxVal or node.data < minVal:
        return False

    return _hIsBST(node.lChild, minVal, node.data) and _hIsBST(node.rChild, node.data, maxVal)


# print(isBST(readyTree.getHead()))
# print(cnt)

"Print Bottom View of Binary Tree"


def BV(node, distance, level, ans):
    if not node:
        return

    if distance not in ans or level >= ans[distance][1]:
        ans[distance] = (node.data, level)

    BV(node.lChild, distance - 1, level + 1, ans)
    BV(node.rChild, distance + 1, level + 1, ans)


ans = {}
BV(readyTree.getHead(), 0, 0, ans)
# readyTree.printTree()
print([ans[x][0] for x in sorted(ans.keys())])
