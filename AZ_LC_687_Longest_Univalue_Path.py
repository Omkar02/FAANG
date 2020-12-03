import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import tree
node = [5, 4, 5, 1, 1, 5, 5, 5]
[tree.insert(x) for x in node]
tree.printTree()

maxVal = [float('-inf')]


def longestUnivalPath(root):
    if not root:
        return 0

    leftLen = longestUnivalPath(root.lChild)
    rightLen = longestUnivalPath(root.rChild)
    leftArrow = rightArrow = 0

    if root.lChild and root.lChild.data == root.data:
        leftArrow = leftLen + 1

    if root.rChild and root.rChild.data == root.data:
        rightArrow = rightLen + 1

    return max(leftArrow, rightArrow)


print(longestUnivalPath(tree.getHead()))
