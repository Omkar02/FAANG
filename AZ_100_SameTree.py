# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree


def isSameTree(root1, root2):
    stack = [(root1, root2)]
    while stack:
        p, q = stack.pop()
        if p and q and p.data == q.data:
            stack.extend([(p.lChild, q.lChild), (p.rChild, q.rChild)])
        elif p or q:
            return False

    return True


print(isSameTree(readyTree.getHead(), readyTree.getHead()))
