# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()
cnt = [0]


"Lowest Common Ancestor"


def LCA(node, n1, n2):
    cnt[0] += 1
    if not node:
        return

    if node.data > n1 and node.data > n2:
        return LCA(node.lChild, n1, n2)
    if node.data < n1 and node.data < n2:
        return LCA(node.rChild, n1, n2)
    return node.data


# print(LCA(readyTree.getHead(), 7, 10))
# print(cnt)

"Convert a given Binary Tree to Doubly Linked List"


class BDL:
    def __init__(self):
        self.head = None

    def BToDLL(self, node):
        if not node:
            return

        self.BToDLL(node.rChild)
        node.rChild = self.head

        if self.head:
            self.head.lChild = node

        self.head = node
        self.BToDLL(node.lChild)

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -->')
            curr = curr.rChild
        print('Null')
# b = BDL()
# b.BToDLL(readyTree.getHead())
# b.printLL()


"Determine if Two Trees are Identical"


def TIT(node1, node2):
    if not node1 and not node2:
        return True

    if node1 and node2:
        return node1.data == node2.data and TIT(node1.lChild, node2.lChild) and TIT(node1.rChild, node2.rChild)

    return False


# print(TIT(readyTree.getHead(), readyTree.getHead()))


"Symmetric Tree (Mirror Image of itself)"


def ST(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2:
        if node1.data == node2.data:
            return ST(node1.lChild, node2.rChild) and ST(node1.rChild, node2.lChild)

    return False


# class Node:
#     def __init__(self, key):
#         self.data = key
#         self.lChild = None
#         self.rChild = None


# root = Node(1)
# root.lChild = Node(2)
# root.rChild = Node(2)
# root.lChild.lChild = Node(3)
# root.lChild.rChild = Node(4)
# root.rChild.lChild = Node(4)
# root.rChild.rChild = Node(3)
# print(ST(root, root))
