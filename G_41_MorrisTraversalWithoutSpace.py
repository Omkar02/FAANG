# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')


from Datastruct.masterTree import readyTree, tree

readyTree.printTree()

# Algo:
#     if lChild is None - - -> print and current = rChild
#     else
#         prev = lChild


def inOrderTraverse(node):
    current = node
    order = []

    while current is not None:
        if current.lChild is None:
            order.append(current.data)
            current = current.rChild
        else:
            prev = current.lChild
            while prev.rChild is not None and prev.rChild is not current:
                prev = prev.rChild
            if prev.rChild is None:
                prev.rChild = current
                current = current.lChild

            else:
                prev.rChild = None
                order.append(current.data)
                current = current.rChild
    return order


print(f'inOrderTraverse = {inOrderTraverse(readyTree.getHead())}')
