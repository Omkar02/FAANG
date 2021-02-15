# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


from Datastruct.masterTree import readyTree, tree


def validteBST(head):
    print('Validate BST')
    return _helperValidate(head, float('-inf'), float('inf'))


def _helperValidate(node, minVal, maxVal):
    if not node:
        return True
    if node.data < minVal or node.data > maxVal:
        return False

    left = _helperValidate(node.lChild, minVal, node.data)
    right = _helperValidate(node.rChild, node.data, maxVal)

    return left and right


# print(validteBST(readyTree.getHead()))

# ---------------------------------------------- #


def createMinHeightTree(arr):
    print("Min Height Tree")
    _helpCreat(arr, 0, len(arr) - 1)
    # tree.insert(2)


def _helpCreat(arr, left, right):
    if left > right:
        return
    mid = (left + right) // 2

    tree.insert(arr[mid])

    _helpCreat(arr, left, mid - 1)
    _helpCreat(arr, mid + 1, right)


arr = [1, 2, 3, 4, 5, 6, 7]
# createMinHeightTree(arr)
# tree.printTree()


# ---------------------------------------------- #

def branchSum(root):
    print("-------Branch Sum---------")
    bSum = []
    _helpFindBranchSum(root, 0, bSum)
    return bSum


def _helpFindBranchSum(node, runningSum, bSum):
    if not node:
        return
    if not node.lChild and not node.rChild:
        bSum.append(runningSum)
        return
    currSum = node.data + runningSum
    _helpFindBranchSum(node.lChild, currSum, bSum)
    _helpFindBranchSum(node.rChild, currSum, bSum)


# print(branchSum(readyTree.getHead()))
# ---------------------------------------------- #

def invertBtree(root):
    print('--- Invert Binary Tree ---')
    _helpToInvert(root)


def _helpToInvert(node):
    if not node:
        return
    swapTheChild(node)
    _helpToInvert(node.lChild)
    _helpToInvert(node.rChild)


def swapTheChild(no):
    no.lChild, no.rChild = no.rChild, no.lChild


# readyTree.printTree()
# invertBtree(readyTree.getHead())
readyTree.printTree()

# ---------------------------------------------- #


def findMaxSumPath(root):
    _, maxPathSum = findMaxSum(root)
    return maxPathSum


def findMaxSum(node):
    if node is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(node.lChild)
    rightMaxSumAsBranch, rightmaxPathSum = findMaxSum(node.rChild)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = node.data
    maxSumAsbranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsbranch)  # triangle
    maxPathSum = max(leftMaxPathSum, rightmaxPathSum, maxSumAsRootNode)

    return (maxSumAsbranch, maxPathSum)


# print(findMaxSumPath(readyTree.getHead()))


# ---------------------------------------------- #
def leftSideView(node):
    print('--- Left Side View ---')
    leftSide = []
    q = [node]
    while len(q):
        n = len(q)
        for i in range(1, n + 1):
            tempNode = q.pop(0)
            if i == 1:
                leftSide.append(tempNode.data)

            if tempNode.lChild:
                q.append(tempNode.lChild)

            if tempNode.rChild:
                q.append(tempNode.rChild)
    return leftSide


# print(leftSideView(readyTree.getHead()))

# ---------------------------------------------- #
def verticalTree(node, level, ans):
    if not node:
        return
    if level not in ans:
        ans[level] = []
    ans[level].append(node.data)

    verticalTree(node.lChild, level - 1, ans)
    verticalTree(node.rChild, level + 1, ans)


ans = {}
# verticalTree(readyTree.getHead(), 0, ans)
# [print(ans[x]) for x in sorted(ans, key=lambda a:ans[a])]

# ---------------------------------------------- #


def levelOrderSpiral(root):
    one, two = [root], []
    ans = []
    while len(one) != 0 or len(two) != 0:
        while len(one) != 0:
            te = one.pop()
            ans.append(te.data)
            if te.rChild:
                two.append(te.rChild)
            if te.lChild:
                two.append(te.lChild)

        while len(two) != 0:
            te = two.pop()
            ans.append(te.data)
            if te.lChild:
                one.append(te.lChild)
            if te.rChild:
                one.append(te.rChild)
    return ans


# print(levelOrderSpiral(readyTree.getHead()))

# ---------------------------------------------- #

def countLeaves(node):
    if not node:
        return 0
    if not node.lChild and not node.rChild:
        return 1

    return countLeaves(node.lChild) + countLeaves(node.rChild)


# print(countLeaves(readyTree.getHead()))


# ---------------------------------------------- #
def isBalanced(node):
    if not node:
        return True
    lHeight = getHeight(node.lChild, 0)
    rHeight = getHeight(node.rChild, 0)

    if (abs(lHeight - rHeight) <= 1) and isBalanced(node.lChild) and isBalanced(node.rChild):
        return True
    return False


def getHeight(node, depth):
    if not node:
        return 0
    depth += 1 + max(getHeight(node.lChild, depth), getHeight(node.rChild, depth))
    return depth


print(isBalanced(readyTree.getHead()))
