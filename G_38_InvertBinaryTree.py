import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Meduim')


from Datastruct.masterTree import readyTree

readyTree.printTree()


def invertBinaryTree(node):
    if not node:
        return

    swap(node)
    invertBinaryTree(node.lChild)
    invertBinaryTree(node.rChild)


def swap(node):
    node.lChild, node.rChild = node.rChild, node.lChild


invertBinaryTree(readyTree.getHead())

readyTree.printTree()
