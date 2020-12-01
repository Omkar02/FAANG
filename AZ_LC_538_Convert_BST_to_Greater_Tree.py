# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree

total = [0]


def greaterTree(root):
    if not root:
        return
    greaterTree(root.rChild)
    total[0] += root.data
    root.data = total[0]
    greaterTree(root.lChild)


readyTree.printTree()
greaterTree(readyTree.getHead())
readyTree.printTree()
