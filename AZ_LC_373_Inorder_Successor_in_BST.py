# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree


def inOrderSuccessor(root, node):
    if not root:
        return
    if node.rChild:
        return minValue(node.rChild)

    successor = None
    while root:
        if root.data < node.data:
            root = root.rChild
        elif root.data > node.data:
            successor = root
            root = root.lChild
        else:
            break
    return successor.data


def minValue(node):
    curr = node
    while curr:
        if not curr.lChild:
            break
        curr = curr.lChild

    return curr.data


readyTree.printTree()
root, node = readyTree.getHead(), readyTree.Serach(5)
print(f'the inOrder Successor = {inOrderSuccessor(root, node)}')
