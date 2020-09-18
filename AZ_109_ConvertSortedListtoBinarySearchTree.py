# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Medium')

from Datastruct.masterTree import tree


# min height bst
def sortedListToBST(array):
    res = []
    l, h = 0, len(array) - 1
    mid = (l + h) // 2
    heBinary(array, l, h, res)
    # heBinary(array, mid + 1, h, res)

    return res


def heBinary(array, l, h, res):
    if l > h:
        return

    piviot = (l + h) // 2
    print(array[piviot])
    tree.insert(array[piviot])

    heBinary(array, l, piviot - 1, res)
    heBinary(array, piviot + 1, h, res)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
node = sortedListToBST(array)

tree.printTree()
