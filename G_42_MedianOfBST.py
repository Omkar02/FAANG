# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree

readyTree.printTree()


def getMedium(head):
    order = []
    getInOrderTraverse(head, order)

    mid = len(order) // 2
    print(len(order))
    if len(order) % 2 != 0:
        return order[mid]
    else:
        val = order[mid - 1:mid + 1]
        print(val, order)
        return (val[0] + val[1]) / 2


def getInOrderTraverse(node, order):
    if not node:
        return
    getInOrderTraverse(node.lChild, order)
    order.append(node.data)
    getInOrderTraverse(node.rChild, order)


print(f'Medium = {getMedium(readyTree.getHead())}')

#        6
#     /    \
#    3       8
#  /   \    /  \
# 1     4  7    9
arr = [6, 3, 1, 4, 8, 7, 9]
for i in arr:
    tree.insert(i)
tree.printTree()
print(f'Medium = {getMedium(tree.getHead())}')
