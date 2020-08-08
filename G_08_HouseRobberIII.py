import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import tree, BST


def maxRobery(tree):
    node = tree.getHead()
    # print(v, maxMoney)
    return max(houseRobber(node))


def houseRobber(node):
    if node is None:
        return (0, 0)

    robLeft = houseRobber(node.lChild)
    # print(robLeft, 'L')
    robRight = houseRobber(node.rChild)
    # print(robRight,'R')

    return (node.data + robLeft[1] + robRight[1], max(robLeft[0],
                                                      robLeft[1]) + max(robRight[0],
                                                                        robRight[1]))


# left = self.dfs(root.left)
# right = self.dfs(root.right)
# return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))

nodes = [5, 3, 2, 4, 7, 6]


for i in nodes:
    tree.insert(i)

tree.printTree()
print(maxRobery(tree))
