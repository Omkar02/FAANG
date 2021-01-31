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
