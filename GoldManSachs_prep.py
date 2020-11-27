# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


"Longest Substring Without Repeating Characters"


def LSWRC(string):
    maxLen = 0
    currIdx = 0
    n = len(string)
    mp = {}
    for i in range(n):
        if string[i] in mp:
            currIdx = max(currIdx, mp[string[i]])
        maxLen = max(maxLen, i - currIdx + 1)
        mp[string[i]] = i + 1

    return maxLen


# print(LSWRC('babbbbav'))


"Median of Two Sorted Arrays"
from Datastruct.masterHeap import maxHeap, minHeap
lower = maxHeap([])
greater = minHeap([])
median = None
va = [lower, greater, median]


def insert(nu):
    if not va[0].length or nu < va[0].peek():
        va[0].length += 1
        va[0].insert(nu)
    else:
        va[1].length += 1
        va[1].insert(nu)
    rebalanceHeap()
    updateMedium()


def rebalanceHeap():
    if va[0].length - va[1].length == 2:
        va[1].insert(va[0].remove())
        va[0].length -= 1
        va[1].length += 1
    elif va[1].length - va[0].length == 2:
        va[0].insert(va[1].remove())
        va[1].length -= 1
        va[0].length += 1


def updateMedium():
    if va[0].length == va[1].length:
        va[2] = (va[0].peek() + va[1].peek()) / 2
    elif va[0].length > va[1].length:
        va[2] = va[0].peek()
    else:
        va[2] = va[1].peek()


arr = [5, 10, 100, 200, 6, 13, 14]
result = []
for i in arr:
    insert(i)
    result.append(va[2])
    # print(result)
# print(f'the contineous Mediam = {result}')
