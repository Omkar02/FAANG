# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

def delNodes(root, to_delete):
    remaning = []

    removeNode(root, to_delete, remaning)
    if root.data not in to_delete:
        remaning.append(root.data)
    # print(remaning)
    return remaning


def removeNode(node, to_delete, remaning):
    if node is None:
        return None

    node.lChild = removeNode(node.lChild, to_delete, remaning)
    node.rChild = removeNode(node.rChild, to_delete, remaning)

    if node.data in to_delete:
        if node.lChild is not None:
            remaning.append(node.lChild.data)
        if node.rChild is not None:
            remaning.append(node.rChild.data)

        return None

    return node


from Datastruct.masterTree import readyTree

readyTree.printTree()

deleteNode = [2, 9]
data = delNodes(readyTree.getHead(), deleteNode)
result = []
print(data)
readyTree.printTree()
