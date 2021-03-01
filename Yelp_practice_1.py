# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


head = '+' * 10


def minIndexSum(list1, list2):
    print(f'{head} 599. Minimum Index Sum of Two Lists {head}')
    ans = []
    minVal = float('inf')

    lookUp = {val: i for i, val in enumerate(list1)}
    for j, val in enumerate(list2):
        if val in lookUp:
            if (lookUp[val] + j) < minVal:
                ans = []
                minVal = lookUp[val] + j
                ans.append(val)
            elif (lookUp[val] + j) == minVal:
                ans.append(val)
    return ans


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
# Output: ["KFC", "Burger King", "Tapioca Express", "Shogun"]
# print(minIndexSum(list1, list2))


def LongestCommPre(strs):
    print(f'{head} 14. Longest Common Prefix {head}')
    ans = ''
    for pre in zip(*strs):
        if len(set(pre)) != 1:
            break
        ans += pre[-1]
    return ans


strs = ["flower", "flow", "flight"]
# print(LongestCommPre(strs))


def isomorString(s, t):
    print(f'{head} 205. Isomorphic Strings {head}')
    if len(s) != len(t):
        return False

    sCharMap, tCharMap = {}, {}

    for v, w in zip(s, t):
        if (v in sCharMap and sCharMap[v] != w) or (w in tCharMap and tCharMap[w] != v):
            return False

        sCharMap[v], tCharMap[w] = w, v
    return True


s = "egg"
t = "add"

# print(isomorString(s, t))


def twoSum(nums, target):
    print(f'{head} 1. Two Sum {head}')
    nums.sort()
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        currSum = nums[lo] + nums[hi]
        if currSum == target:
            return (lo, hi)
        elif currSum < target:
            lo += 1
        else:
            hi -= 1
    return (-1, -1)


nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]
# print(twoSum(nums, target))


def reverseLinkedList(lList):
    print(f'{head} 206. Reverse Linked List {head}')
    p1, p2 = None, lList.getHead()
    lList.traverseList()

    while p2:
        p3 = p2.nextNode
        p2.nextNode = p1

        p1 = p2
        p2 = p3

    lList.head = p1
    lList.traverseList()


# from Datastruct.masterLinkedList import v
# [v.insertStart(val) for val in [1, 2, 3, 4, 5]]
# reverseLinkedList(v)


def intersectionArr(num1, num2):
    print(f'{head} 349. Intersection of Two Arrays {head}')

    def getInterSec(sOne, sTwo):
        return [x for x in sOne if x in sTwo]

    s, t = set(num1), set(num2)
    if len(s) > len(t):
        return getInterSec(t, s)
    else:
        return getInterSec(s, t)


num1 = [1, 2, 2, 1]
num2 = [2, 2]

num1 = [4, 9, 5]
num2 = [9, 4, 9, 8, 4]
# print(intersectionArr(num1, num2))


def validAnageam(s, t):
    print(f'{head} 242. Valid Anagram {head}')
    return len(s) == len(t) and ''.join(sorted(s)) == ''.join(sorted(t))


s = "anagram"
t = "nagaram"

s = "rat"
t = "car"
# print(validAnageam(s, t))


def stringCompression(chars):
    print(f'{head} 443. String Compression {head}')
    ans = ''
    idx = 0
    n = len(chars)

    while idx < n:
        curr = chars[idx]
        cnt = 1
        while idx < n - 1 and curr == chars[idx + 1]:
            cnt += 1
            idx += 1
        ans += f'{curr}{cnt}'
        idx += 1
    return list(ans)


chars = ["a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "a"]
# print(stringCompression(chars))


def destinationCity(paths):
    print(f'{head} 1436. Destination City {head}')
    routes = {val: False for x in paths for val in x}
    for scr, dst in paths:
        if scr in routes:
            routes[scr] = True

    for r in routes:
        if not routes[r]:
            return r
    return -1


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths = [["B", "C"], ["D", "B"], ["C", "A"]]
# print(destinationCity(paths))


def isPrefixOfWord(sentence, searchWord):
    print(f'{head} 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence {head}')
    sentence = sentence.split()
    for idx, s in enumerate(sentence):
        if len(s) < len(searchWord):
            continue

        prefix = s[0:len(searchWord)]
        if prefix == searchWord:
            return idx + 1

    return -1


sentence = "i love eating burger"
searchWord = "burg"
# Output: 4
sentence = "this problem is an easy problem"
searchWord = "pro"
# Output: 2

print(isPrefixOfWord(sentence, searchWord))
