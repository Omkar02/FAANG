import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# sorted array
# O(n+k) time | O(1) space
def kMissingElement(array, k):
    if k > max(array):
        return k + len(array)
    idx = array[0]
    arrIdx = 0
    while idx <= k + len(array) - 1:
        if arrIdx < len(array) and array[arrIdx] == idx:
            print('----HIT-----')
            arrIdx += 1
            idx += 1
            continue
        idx += 1

    return idx


array = [4, 7, 9, 10]
K = 1200

# array = [1, 2, 4]
# K = 3
print(kMissingElement(array, K))

# unsorted

array = [3, 4, -1, 1]
array = [1, 2, 0]


def uKMissingElement(array):
    idx = 0
    while True:
        if idx not in array:
            return idx
        idx += 1


print(uKMissingElement(array))
