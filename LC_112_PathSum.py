# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree


def hasPathSum(tree):
    ans = []
    root = tree.getHead()

    getPathSum(root, ans, 0)
    return ans


def getPathSum(node, ans, currSum):
    if not node:
        return

    currSum += node.data

    if node.lChild is None and node.rChild is None:
        ans.append(currSum)

    getPathSum(node.lChild, ans, currSum)
    getPathSum(node.rChild, ans, currSum)


readyTree.printTree()
print(hasPathSum(readyTree))
