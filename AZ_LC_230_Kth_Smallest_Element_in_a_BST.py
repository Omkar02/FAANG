# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import readyTree
readyTree.printTree()

cnt = [0]


def k_smallest_val(root, k):
    if not root:
        return
    stack = []

    while True:
        while root:
            cnt[0] += 1
            stack.append(root)
            root = root.lChild
        if not stack:
            return -1
        root = stack.pop()
        k -= 1
        if not k:
            return root.data
        root = root.rChild


print(k_smallest_val(readyTree.getHead(), 2))
print(cnt)
