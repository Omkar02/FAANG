# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()
cnt = [0]

"Count Leaves in Binary Tree"


def CL(node):
    cnt[0] += 1
    if not node:
        return 0

    if not node.lChild and not node.rChild:
        return 1

    return CL(node.lChild) + CL(node.rChild)


# print(CL(readyTree.getHead()))
# print(cnt)

"Check for Balanced Tree"


def BT(node, cache):
    # cnt[0] += 1
    if not node:
        return True

    lHeight = getH(node.lChild, cache)
    rHeight = getH(node.rChild, cache)

    if (abs(lHeight - rHeight) <= 1) and BT(node.lChild, cache) and BT(node.rChild, cache):
        return True
    return False


def getH(node, cache):
    print(cache)
    cnt[0] += 1
    if node in cache:
        print('hit')
        return cache[node]
    if not node:
        return 0
    cache[node] = max(getH(node.lChild, cache), getH(node.rChild, cache)) + 1
    return cache[node]


class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


# print(BT(readyTree.getHead(), {}))
# print(cnt[0])
# root = Node(1)
# root.lChild = Node(2)
# root.rChild = Node(3)
# root.lChild.lChild = Node(4)
# root.lChild.rChild = Node(5)
# root.lChild.lChild.lChild = Node(8)
# print(BT(root, {}))
# print(cnt)


"Serialize and Deserialize a Binary Tree"


def serialize(node, s=""):
    if not node:
        s += "# "
        return s
    s += (str(node.data) + " ")
    s = serialize(node.lChild, s=s)
    s = serialize(node.rChild, s=s)
    return s


# print(serialize(readyTree.getHead()))

i = 0


def deserialize(s):
    global i
    if s[i] == "#":
        if(i < len(s) - 2):
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        node = Node(s[i:sp])
        i = sp + 1
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node


# print(deserialize(serialize(readyTree.getHead())))


"Maximum Path Sum"


def MPS(node):
    _, maxSum = _FMS(node)
    return maxSum


def _FMS(node):
    if not node:
        return (0, 0)

    mLSB, mLMP = _FMS(node.lChild)
    mRSB, mRMP = _FMS(node.rChild)

    mChild = max(mLSB, mRSB)
    val = node.data

    mSB = max(mChild + val, mChild)

    mRoot = max(mSB, mLSB + val + mRSB)
    maxSum = max(mLMP, mRMP, mRoot)
    return (mSB, maxSum)


# print(MPS(readyTree.getHead()))
