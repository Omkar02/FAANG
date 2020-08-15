# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import tree


def minHeightBST(arr):
    arr.sort()
    seq = []
    minHeightBstHelper(arr, 0, len(arr) - 1, seq)
    return seq


def minHeightBstHelper(arr, left, right, seq):
    if left > right:
        return
    mid = (left + right) // 2
    seq.append(arr[mid])
    # print(arr[left], arr[mid], arr[right])
    minHeightBstHelper(arr, left, mid - 1, seq)
    minHeightBstHelper(arr, mid + 1, right, seq)


import random
arr = [5, 6, 7, 8, 9, 3, 2, 1, 10]
random.shuffle(arr)
minH = minHeightBST(arr)
print(minH)
for i in minH:
    tree.insert(i)

tree.printTree()
