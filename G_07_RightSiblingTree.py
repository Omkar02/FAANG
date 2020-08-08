import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import tree, BST


nodes = [5, 3, 2, 4, 7, 6]


for i in nodes:
    tree.insert(i)

tree.printTree()


def rightSiblingTree(tree):
    node = tree.getHead()
    mutate(node, None, None)
    return tree


def mutate(node, parent, isLeft):
    if node is None:
        return
    lChild, rChild = node.lChild, node.rChild
    mutate(lChild, node, True)
    if parent is None:
        node.rChild = None
    elif isLeft:
        node.rChild = parent.rChild
    else:
        if parent.rChild is None:
            node.rChild = None
        else:
            node.rChild = parent.rChild.lChild
    mutate(rChild, node, False)


a = rightSiblingTree(tree)
a.printTree()
