# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

from Datastruct.masterLinkedList import l
from Datastruct.masterTree import readyTree
### Count set bits in an Integer ###


def count_set_bits(n):
    set_bits = 0
    while n:
        set_bits += n & 1
        n >>= 1
    return set_bits


n = 20
# print(count_set_bits(n))


### Set the K-th bit of a given number ###

def set_k_bit(n, k):
    return ((1 << k) | n)


n, k = 10, 2
# print(set_k_bit(n, k))

### swap nibble ###


def swapNibble(n):
    return ((n & 0x0F) << 4 | (n & 0xF0) >> 4)


n = 100
# print(swapNibble(n))


### check palidrome ###

def isPali(string):
    # print([(i, len(string) - 1 - i)for i in range(len(string) // 2 + 1)])
    return all(string[i] == string[len(string) - 1 - i] for i in range(len(string) // 2))


string = 'ababa'
# print(isPali(string))


### circular list traverse ###

def ll_traverse(head):
    curr = head
    while curr:
        print(curr.data, end=' -> ')
        curr = curr.nextNode
        if curr == head:
            break
    print('Null')


a = [1, 2, 3, 4, 5]
# [l.insertStart(i) for i in a]
# l.traverseList()
# ll_traverse(l.getHead())


### Reverse words in a given string ###

def reverse_words_string(string):
    return ' '.join(string.split(' ')[::-1])


string = 'i like this program very much'
# print(reverse_words_string(string))


### ZigZag Tree Traversal ###

def zig_zag_traverse(root):
    isLeftToRight = True
    currentLevel = [root]
    nextLevel = []
    ans = []

    while currentLevel:
        currNode = currentLevel.pop()
        ans.append(currNode.data)

        if isLeftToRight:
            if currNode.lChild:
                nextLevel.append(currNode.lChild)
            if currNode.rChild:
                nextLevel.append(currNode.rChild)
        else:
            if currNode.rChild:
                nextLevel.append(currNode.rChild)
            if currNode.lChild:
                nextLevel.append(currNode.lChild)
        if len(currentLevel) == 0:
            isLeftToRight = not isLeftToRight
            nextLevel, currentLevel = currentLevel, nextLevel
    return ans


# print(zig_zag_traverse(readyTree.getHead()))
# readyTree.printTree()

### Counting Sort ###


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        print(i, len(count), array[i])
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
    return output


arr = [5, 9, 0, 3, 8, 5, 1, 9]
# print(countingSort(arr))

### Count all possible paths from top left to bottom right ###


def count_all_paths(n, m, cache):
    curr = (n, m)
    if curr in cache:
        return cache[curr]
    if n == 1 or m == 1:
        return 1
    cache[curr] = count_all_paths(n - 1, m, cache) + count_all_paths(n, m - 1, cache)
    return cache[curr]


m = 10
n = 20
# print(count_all_paths(n, m, {}))


### Missing number in array ###
def find_missing(arr):
    return sum([i for i in range(min(arr), max(arr) + 1)]) - sum(arr)


arr = [1, 2, 3, 5]
arr = [1, 2, 4, 5, 6]
# print(find_missing(arr))

### all Permutation ###


def per(arr, i, j, ans):
    if i == j:
        ans.append(''.join(arr))
    for k in range(i, j + 1):
        arr[k], arr[i] = arr[i], arr[k]
        per(arr, i + 1, j, ans)
        arr[k], arr[i] = arr[i], arr[k]


ans = []
arr = ['a', 'b', 'c']
# per(arr, 0, len(arr) - 1, ans)
# print(ans)


### reverse Bit ###
def reverse_Bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result


# print(reverse_Bits(1))


### Min-height BST ###


def min_height_BST(arr):
    ans = []
    _construct_tree(arr, 0, len(arr) - 1, ans)
    return ans


def _construct_tree(arr, startIdx, endIdx, ans):
    if endIdx < startIdx:
        return
    mid = (startIdx + endIdx) // 2
    ans.append(arr[mid])
    _construct_tree(arr, startIdx, mid - 1, ans)
    _construct_tree(arr, mid + 1, endIdx, ans)


arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
# print(min_height_BST(arr))


### Is the array is a max heap ###
def isHeap(arr):
    n = len(arr)
    for i in range(((n - 2) // 2) + 1):
        if (arr[2 * i + 1] > arr[i]) or (((2 * i + 2) < n) and arr[2 * i + 2] > arr[i]):
            return False
    return True


arr = [90, 15, 10, 7, 12, 2]
arr = [9, 15, 10, 7, 12, 11]
# print(isHeap(arr))


### Reverse Level Order Traversal  ###


def reverse_level_order(head):
    currentLevel = [head]
    nextLevel = []
    ans = []

    while currentLevel:
        node = currentLevel.pop(0)
        ans.insert(0, node.data)

        if node.rChild:
            nextLevel.append(node.rChild)
        if node.lChild:
            nextLevel.append(node.lChild)

        if len(currentLevel) == 0:
            currentLevel, nextLevel = nextLevel, currentLevel

    return ans


# readyTree.printTree()
# print(reverse_level_order(readyTree.getHead()))


### Number of jumps for a thief to cross walls ###

def num_of_jumps(heights, X, Y):
    jumps = 0
    for i in range(len(heights)):
        jumps += 1
        if heights[i] > X:
            h = heights[i] - (X - Y)
            # jumps += h / (X - Y)
            if (h % (X - Y) > 1):
                jumps += 1
    return int(jumps)


# Input:
heights = [11, 11]
X = 10
Y = 1
# Output: 4

# He needs to make 2 jumps for first wall
# and 2 jumps for second wall.

heights = [11, 10, 10, 9]
X = 10
Y = 1
# Output: 5
# print(num_of_jumps(heights, X, Y))
