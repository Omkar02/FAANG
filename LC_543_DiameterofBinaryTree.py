# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree


def diameterOfBinaryTree(tree):
    root = tree.getHead()
    ans = 1

    def depth(node):
        nonlocal ans

        if not node:
            return 0
        l = depth(node.lChild)
        r = depth(node.rChild)

        ans = max(ans, l + r + 1)

        return max(l, r) + 1
    return depth(root) - 1


readyTree.printTree()
print(diameterOfBinaryTree(readyTree))
