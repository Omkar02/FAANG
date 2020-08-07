import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


def flipBinaryTree(node):
    if node is None:
        return
    swap(node)
    flipBinaryTree(node.left)
    flipBinaryTree(node.right)


def swap(node):
    node.left, node.right = node.right, node.left
