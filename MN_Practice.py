# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

from Datastruct.masterLinkedList import l


def findAllSubString(string):
    ans = []
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            ans.append(string[i:j])
    ans = sorted(ans, key=lambda a: len(a))
    def x(a): return [c[::-1] for c in a]
    return ans, x(ans)


# print(findAllSubString('abc'))
nums = [13, 2, 1, 5, 3, 15]
k = 15
# ans - {13, 2}, {15},


def findSum(nums, k):
    curr = 0
    start = 0
    ans = []
    te = []
    n = len(nums)
    for i in range(n):
        if nums[i] == k:
            ans.append([nums[i]])
        else:
            curr += nums[i]
            te.append(nums[i])
            print(curr, te, nums[i])
            if curr == k:
                ans.append(te)
                te = []
                curr = 0
            if curr > k:
                print('-------')
                curr -= nums[start]
                start += 1
                te.pop(0)
    return ans


# print(findSum(nums, k))

def checkPrime(nums):
    if nums <= 1:
        return False
    for i in range(2, nums):
        if nums % i != 0:
            return False
    return True


# print(checkPrime(2))


'Given an unsorted array, how will you find maximum sum of pair of elements? In O(n)'


def findLargestSumPair(arr):
    largePair = [0, 0]
    n = len(arr)
    for i in range(n):
        updateLargest(arr[i], largePair)

    return largePair


def updateLargest(val, arr):
    if val > arr[1]:
        helpUpdate(val, arr, 1)
    elif val > arr[0]:
        helpUpdate(val, arr, 0)


def helpUpdate(val, arr, index):
    for i in range(len(arr)):
        if index == i:
            arr[i] = val
        else:
            arr[i] = arr[i + 1]


arr = [12, 34, 10, 6, 40]
# print(findLargestSumPair(arr))

'How will you reverse a linked list without any extra buffer and in O(n) time complexity'


# p1 < - 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> Null


def reveseLinkedList(lList):
    p1 = None
    p2 = lList.getHead()

    while p2:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3
    lList.head = p1
    lList.traverseList()


# [l.insertStart(i) for i in range(6)]
# l.traverseList()
# reveseLinkedList(l)


'Given a sorted array containing numbers from 1 to n , a number is missing in the array . How will you find it?  '


def findMissing(arr):
    minVal, maxVal = min(arr), max(arr)
    return sum([i for i in range(minVal, maxVal + 1)]) - sum(arr)


def findMissing(arr):
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i] + 1
    return -1


arr = [1, 2, 3, 4, 5]
# print(findMissing(arr))


'Find all cube root within the range'


def findCubeRoot(a, b):
    a_cubeRoot = getCubeRoot(a)
    b_cubeRoot = getCubeRoot(b)
    print(a_cubeRoot, b_cubeRoot)
    cubeRoot = []
    for i in range(a_cubeRoot, b_cubeRoot):
        currCube = i**3
        if (currCube >= a and currCube < b):
            cubeRoot.append(currCube)
    return cubeRoot


def getCubeRoot(n) -> int:
    return int(n**(1 / 3))


a, b = 24, 576
print(findCubeRoot(a, b))
