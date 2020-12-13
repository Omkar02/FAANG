# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


class bNode:
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


def constBSTwith(preorder, inorder):
    if not preorder or not inorder:
        return
    if len(preorder) == 1:
        return bNode(preorder[0])

    root = bNode(preorder[0])
    rootIdx = inorder.index(preorder[0])

    leftPreorder = preorder[1:rootIdx + 1]
    leftInorder = inorder[:rootIdx]

    rightPreorder = preorder[rootIdx + 1:]
    rightInorder = inorder[rootIdx + 1:]

    root.lChild = constBSTwith(leftPreorder, leftInorder)
    root.rChild = constBSTwith(rightPreorder, rightInorder)

    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(constBSTwith(preorder, inorder))

#   3
#  / \
# 9  20
#   /  \
#  15   7
