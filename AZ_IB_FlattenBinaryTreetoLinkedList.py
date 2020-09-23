# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree

cnt = [0]


def treeToList(tree):
    head = te = tree.getHead()
    treeHelper(head)
    while te is not None:
        print(te.data, end=' --> ')
        te = te.rChild
    print('None')


def treeHelper(node):
    if not node:
        return

    left = node.lChild
    right = node.rChild

    node.lChild = None

    treeHelper(left)
    treeHelper(right)

    node.rChild = left

    curr = node
    while curr.rChild is not None:
        curr = curr.rChild

    curr.rChild = right


treeToList(readyTree)
# def treeToList(tree):
#     te = curr = tree.getHead()
#     while curr is not None:
#         if curr.lChild:
#             if curr.rChild:
#                 nxt = curr.lChild
#                 while nxt.rChild:

#                     nxt = nxt.rChild
#                 nxt.rChild = curr.rChild

#             curr.rChild = curr.lChild
#             curr.lChild = None
#         curr = curr.rChild

#     while te is not None:
#         print(te.data, end=' --> ')
#         te = te.rChild
#     print('None')


# readyTree.printTree()


treeToList(readyTree)
# print(cnt)
