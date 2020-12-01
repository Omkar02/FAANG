# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')

from Datastruct.masterTree import readyTree, tree
readyTree.printTree()


def allPaths(root, ans, temp):
    if not root:
        return
    if not root.lChild and not root.rChild:
        temp += [root.data]
        ans.append(temp)

    else:
        allPaths(root.lChild, ans, temp + [root.data])
        allPaths(root.rChild, ans, temp + [root.data])


ans = []
allPaths(readyTree.getHead(), ans, [])
print(ans)
