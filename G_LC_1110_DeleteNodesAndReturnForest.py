# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree

readyTree.printTree()


class forest:
    def __init__(self, trees):
        self.root = trees.getHead()
        self.remaning = []
        self.trees = trees

    def toDelete(self, treeBurned):
        self.removeNode(self.root, treeBurned)
        if self.root.data not in treeBurned:
            self.remaning.append(self.root.data)
        return self.remaning

    def removeNode(self, node, dNode):
        if not node:
            return None

        node.lChild = self.removeNode(node.lChild, dNode)
        node.rChild = self.removeNode(node.rChild, dNode)

        if node.data in dNode:
            if node.lChild:
                self.remaning.append(node.lChild.data)
            if node.rChild:
                self.remaning.append(node.rChild.data)

            return None

        return node


treeBurned = [5, 8]
f = forest(readyTree)
print(f.toDelete(treeBurned))
