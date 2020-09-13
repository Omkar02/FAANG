# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

def isBalanced(root):
    if not root:
        return True

    leftDepth = getDepth(root.lChild)
    rightDepth = getDepth(root.rChild)

    if abs(leftDepth - rightDepth) <= 1 and isBalanced(root.lChild) and isBalanced(root.rChild):
        return True

    return False


def getDepth(node):
    if not node:
        return 0

    return max(getDepth(node.lChild), getDepth(node.rChild)) + 1


from Datastruct.masterTree import readyTree, tree


node = [3, 9, 20, 15, 7]

for i in node:
    tree.insert(i)

tree.printTree()



print(f'Is Balanced = {isBalanced(tree.getHead())}')
print(f'Is Balanced = {isBalanced(readyTree.getHead())}')
