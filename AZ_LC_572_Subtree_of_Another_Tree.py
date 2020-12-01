# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree, tree


def sameSubTree(t1, t2):
    if not t1:
        return False
    if t1.data == t2.data and dfs(t1, t2):
        return True
    return sameSubTree(t1.lChild, t2) or sameSubTree(t1.rChild, t2)


def dfs(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.data == t.data and dfs(s.lChild, t.lChild) and dfs(s.rChild, t.rChild)


array = [2, 1, 3]
for i in array:
    tree.insert(i)
readyTree.printTree()
tree.printTree()

print(sameSubTree(readyTree.getHead(), tree.getHead()))
