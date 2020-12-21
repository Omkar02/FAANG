# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()


class longest:
    def __init__(self, head=None):
        self.maxLen = float('-inf')
        self.findConsecutive(head, head.data, 0)

    def findConsecutive(self, node, expected, currLen):
        if not node:
            return

        if node.data == expected:
            # print(node.data, expected)
            currLen += 1

        else:
            # print()
            currLen = 1

        self.maxLen = max(self.maxLen, currLen)

        self.findConsecutive(node.lChild, node.data + 1, currLen)
        self.findConsecutive(node.rChild, node.data + 1, currLen)


l = longest(readyTree.getHead())
print(l.maxLen)
