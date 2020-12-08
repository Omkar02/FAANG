# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Easy')


from Datastruct.masterTree import readyTree

readyTree.printTree()


class TreeSting:
    def __init__(self):
        self.string = ''

    def treeToString(self, node):
        if not node:
            return None

        self.string += str(node.data)
        if node.lChild or node.rChild:  # if node is not a leaf
            self.string += "("
            self.treeToString(node.lChild)
            self.string += ")"
            if node.rChild:  # keep the rChild child if it exists
                self.string += "("
                self.treeToString(node.rChild)
                self.string += ")"


t = TreeSting()
t.treeToString(readyTree.getHead())
print(t.string)
