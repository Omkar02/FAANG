# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')


from Datastruct.masterTree import readyTree


readyTree.printTree()


def longestConsSeq(root):
    if not root:
        return -1
    ans = [float('-inf')]
    getLongestConsSeq(root, 0, root.data, ans)
    return ans[0]


def getLongestConsSeq(node, currLen, expected, maxLen):
    if not node:
        return

    if node.data == expected:
        currLen += 1
    else:
        currLen = 1
    maxLen[0] = max(maxLen[0], currLen)

    if node.lChild:
        getLongestConsSeq(node.lChild, currLen, node.data + 1, maxLen)
    if node.rChild:
        getLongestConsSeq(node.rChild, currLen, node.data + 1, maxLen)


print(longestConsSeq(readyTree.getHead()))
