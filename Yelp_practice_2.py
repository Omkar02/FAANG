# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


head = '+' * 10


class Itenary:
    def __init__(self, tickets):
        print(f'{head} 332. Reconstruct Itinerary {head}')
        self.routes = self.getRoutes(tickets)
        self.visited = set()
        self.locList = []
        self.getIternary('JFK')

    def getRoutes(self, tickets):
        routes = {}
        for scr, dst in tickets:
            if scr not in routes:
                routes[scr] = []
            routes[scr].append(dst)
            routes[scr].sort()
        return routes

    def getIternary(self, currLoc):
        self.locList.append(currLoc)
        if currLoc in self.visited:
            return
        self.visited.add(currLoc)
        if currLoc in self.routes:
            for nxtLoc in self.routes[currLoc]:
                self.getIternary(nxtLoc)

    def getLocList(self):
        return self.locList


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

# i = Itenary(tickets)
# print(i.getLocList())


def mergeInterval(intervals):
    print(f'{head} 56. Merge Intervals {head}')
    intervals.sort(key=lambda a: a[0])
    ans = []
    for i in intervals:
        if not ans:
            ans.append(i)
        # when to merge
        elif ans[-1][1] >= i[0]:
            ans[-1] = [ans[-1][0], i[1]] if ans[-1][1] < i[1] else ans[-1]
        else:
            ans.append(i)
    return ans


intervals = [[1, 4], [4, 5]]
# Output: [[1,5]]
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1,6],[8,10],[15,18]]
# print(mergeInterval(intervals))


def groupAnagram(strs):
    print(f'{head} 49. Group Anagrams {head}')
    grps = {}
    for i in strs:
        currSort = ''.join(sorted(i))
        if currSort not in grps:
            grps[currSort] = []
        grps[currSort].append(i)
    return [val for _, val in grps.items()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagram(strs))


def topKFreq(words, k):
    print(f'{head} 692. Top K Frequent Words {head}')
    freqCount = {s: words.count(s) for s in set(words)}
    return sorted([key for key in freqCount], key=lambda a: freqCount[a], reverse=True)[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
# Output: ["i", "love"]
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
# Output: ["the", "is", "sunny", "day"]
# print(topKFreq(words, k))


def wordBreak(word, wordDict):
    print(f'{head} 139. Word Break {head}')
    return _helpWordBreak(word, wordDict)


def _helpWordBreak(word, wordDict):
    print(word)
    if word in wordDict:
        return True
    if not word:
        return True

    for i in range(1, len(word) + 1):
        newStr = word[:i]
        print('\t', newStr)
        if newStr in wordDict and _helpWordBreak(word[i:], wordDict):
            return True
    return False


word = s = "leetcode"
wordDict = ["leet", "code"]

word = s = "applepenapple"
wordDict = ["apple", "pen"]
# print(wordBreak(word, wordDict))


def topKEle(nums, k):
    print(f'{head} 347. Top K Frequent Elements {head}')
    freqCount = {val: nums.count(val) for val in set(nums)}
    return sorted([v for v in freqCount], key=lambda a: freqCount[a], reverse=True)[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1, 2]

# print(topKEle(nums, k))

import random


class sol:
    def __init__(self, w):
        print(f'{head} 528.Pick Random {head}')
        self.tSum = sum(w)
        self.weight = [w[0] / self.tSum]
        for i in range(1, len(w)):
            self.weight.append(self.weight[-1] + w[i] / self.tSum)
        print(self.weight)

    def pickIndex(self):
        lo, hi, seed = 0, len(self.weight) - 1, random.random()
        print(seed)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.weight[mid] <= seed:
                lo = mid + 1
            else:
                hi = mid
        return lo


w = [1, 3]
# s = sol(w)
# for _ in range(5):
#     print(s.pickIndex())
import heapq


def meetingRoom(intervals):
    print(f'{head} 253.Meeting Rooms II {head}')
    intervals.sort(key=lambda a: a[0])
    minheap = []
    for i in intervals:
        print(minheap)
        if minheap and i[0] > minheap[0]:
            heapq.heappop(minheap)
            heapq.heappush(minheap, i[1])
        else:
            heapq.heappush(minheap, i[1])
    return len(minheap)


intervals = [(0, 30), (5, 10), (15, 20)]
# print(meetingRoom(intervals))


def wordLadder(beginWord, endWord, wordList):
    print(f'{head} 127. Word Ladder {head}')
    q = [[beginWord, [beginWord]]]
    while q:
        curWord, path = q.pop(0)
        for nxtWord in getNxtWord(curWord, wordList) - set(path):
            if nxtWord == endWord:
                return path + [endWord]

            q.append([nxtWord, path + [nxtWord]])
    return -1


def getNxtWord(word, wordList):
    toReturn = set()
    for w in wordList:
        wLen, wDiff = len(w), 0
        for i in range(wLen):
            if word[i] != w[i]:
                wDiff += 1
        if wDiff == 1:
            toReturn.add(w)
    return toReturn


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadder(beginWord, endWord, wordList))
print(['hit', 'hot', 'dot', 'dog', 'cog'])
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
