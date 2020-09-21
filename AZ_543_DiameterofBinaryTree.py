# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')


from Datastruct.masterTree import readyTree

readyTree.printTree()


class dia:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.depth(root)
        return self.ans - 1

    def depth(self, node):
        if not node:
            return 0

        L = self.depth(node.lChild)
        R = self.depth(node.rChild)

        self.ans = max(L + R + 1, self.ans)
        return max(L, R) + 1


d = dia()
print(d.diameterOfBinaryTree(readyTree.getHead()))
