# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

head = '+' * 10


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.data_pos = {}

    def insert(self, val):
        if val in self.data_pos:
            return False
        self.data_pos[val] = len(self.data)
        self.data.append(val)
        print(self.data)
        return True

    def remove(self, val):
        print(self.data_pos)
        if val not in self.data_pos:
            return False
        lastVal = -1
        valIdx = self.data_pos[val]

        self.data_pos[self.data[-1]] = self.data_pos[val]

        self.data[lastVal], self.data[valIdx] = self.data[valIdx], self.data[lastVal]

        self.data_pos.pop(val)
        self.data.pop()
        print(self.data, self.data_pos)
        return True

    def random(self):
        return random.choice(self.data) if self.data else []


# import random
# # print(dir(random))

# r = RandomizedSet()
# print(r.insert(1))
# print(r.insert(2))
# print(r.insert(1))
# print(r.insert(3))


# print(r.random())


# print(r.remove(1))
# print(r.remove(3))


def findPosiInfinite(arr, key):
    lo, hi, val = 0, 1, arr[0]
    while val < key:
        lo = hi
        hi = 2 * hi
        val = arr[hi]
    return binarySearch(arr, lo, hi, key)


def binarySearch(arr, lo, hi, key):
    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return binarySearch(arr, lo, mid - 1, key)
    return binarySearch(arr, mid + 1, hi, key)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
# print(findPosiInfinite(arr, 10))


def findValEqIndex(arr):
    return iBS(arr, 0, len(arr) - 1)


def iBS(arr, lo, hi):
    if lo > hi:
        return -1

    midIdx = (lo + hi) // 2
    midVal = arr[midIdx]

    if midIdx == midVal:
        return midIdx

    left = iBS(arr, lo, min(midVal, midIdx - 1))
    if left >= 0:
        return left

    return iBS(arr, max(midVal, midIdx + 1), hi)


arr = [-10, -1, 3, 11, 30, 50, 100]
print(findValEqIndex(arr))
