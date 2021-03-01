# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

head = '+' * 10
#                    0       1       2               3       4
# restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]


def findResturants(restaurants, veganFriendly, maxPrice, maxDistance):
    print(f'{head} 1333. Filter Restaurants by Vegan-Friendly, Price and Distance {head}')
    restaurants = sorted(restaurants, key=lambda a: (a[1], -a[3], -a[4]), reverse=True)
    if not veganFriendly:
        return [val[0] for val in restaurants if (val[3] <= maxPrice) and (val[4] <= maxDistance)]
    else:
        return [val[0] for val in restaurants if (val[3] <= maxPrice) and (val[4] <= maxDistance) and (val[2] == 1)]


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10

restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10

restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 30
maxDistance = 3
# print(findResturants(restaurants, veganFriendly, maxPrice, maxDistance))


def lenOfLongSubStringDup(s):
    print(f'{head} 3. Longest Substring Without Repeating Characters {head}')
    lookUp = {}
    sIdx = 0
    n = len(s)
    maxLen = float('-inf')
    p = [-1, -1]
    for idx in range(n):
        if s[idx] in lookUp:
            sIdx = max(sIdx, lookUp[s[idx]])
        currLen = idx - sIdx + 1
        if currLen > maxLen:
            maxLen = currLen
            p = [sIdx, idx]

        lookUp[s[idx]] = idx + 1
    return maxLen, s[p[0]:p[1] + 1]


s = "abcabcbb"
# s = "1234567ss89asdfghjklsdvcdssds"
# print(lenOfLongSubStringDup(s))


def genPrentencis(n):
    print(f'{head} 22. Generate Parentheses {head}')
    ans = []
    _genPrenHelp(n, '', ans, 0, 0)
    return ans


def _genPrenHelp(n, currStr, ans, lo, hi):
    if len(currStr) == n * 2:
        if _isValid(currStr):
            ans.append(currStr)
        return
    if lo < n:
        _genPrenHelp(n, currStr + '(', ans, lo + 1, hi)
    if hi < lo:
        _genPrenHelp(n, currStr + ')', ans, lo, hi + 1)


def _isValid(pren):
    val = 0
    for p in pren:
        val = val + 1 if p == '(' else val - 1
        if val < 0:
            return False
    return val == 0


# print(genPrentencis(3))

class gNode:
    def __init__(self, job):
        self.job = job
        self.prereq = []
        self.visited = False
        self.processing = False


class Graphs:
    def __init__(self, numCourses):
        print(head, '207. Course Schedule', head)
        self.allNodes = []
        self.isDepended = self._getDepended(numCourses)

    def _getDepended(self, numCourses):
        isDepended = {}
        for course in range(numCourses):
            isDepended[course] = gNode(course)
            self.allNodes.append(isDepended[course])
        return isDepended

    def _addPrereq(self, job, prereq):
        jobNode = self.isDepended[job]
        prereqNode = self.isDepended[prereq]

        jobNode.prereq.append(prereqNode)


def topologicalSort(nJob, dependency):
    cGraphs = createJobGraphs(nJob, dependency)
    return getOrderedJob(cGraphs)


def createJobGraphs(nJob, dependency):
    cGraphs = Graphs(nJob)
    for prereq, job in dependency:
        cGraphs._addPrereq(job, prereq)
    return cGraphs


def getOrderedJob(cGraphs):
    orderedJob = []
    nodes = cGraphs.allNodes
    while len(nodes):
        newNode = nodes.pop()
        containsCycle = dfs(newNode, orderedJob)
        if containsCycle:
            return False
    return True, list(reversed(orderedJob))


def dfs(node, oJob):
    if node.visited:
        return False
    if node.processing:
        return True
    node.processing = True
    for prereq in node.prereq:
        containsCycle = dfs(prereq, oJob)
        if containsCycle:
            return False, oJob
    node.visited = True
    node.processing = False
    oJob.append(node.job)


numCourses = 2
prerequisites = [[1, 0]]

# print(topologicalSort(numCourses, prerequisites))


def letterPermutation(s):
    print(head, '784. Letter Case Permutation', head)
    ans = []
    _letterPermu(s, '', 0, ans)
    return ans


def _letterPermu(s, currStr, idx, ans):
    if idx == len(s):
        ans.append(currStr)
        return

    if s[idx].isalpha():
        _letterPermu(s, currStr + s[idx].lower(), idx + 1, ans)
        _letterPermu(s, currStr + s[idx].upper(), idx + 1, ans)
    else:
        _letterPermu(s, currStr + s[idx], idx + 1, ans)


s = "a1b2"
# print(letterPermutation(s))


def combinationSum(candidates, target):
    print(head, '39. Combination Sum', head)
    ans = []
    _comboHelper(candidates, [], target, ans, 0)
    return ans


def _comboHelper(candidates, temp, target, ans, idx):
    if target < 0:
        return
    if target == 0:
        ans.append(temp)
        return
    for i in range(idx, len(candidates)):
        _comboHelper(candidates, temp + [candidates[i]], target - candidates[i], ans, i)


candidates = [2, 3, 6, 7]
target = 7

candidates = [2, 3, 5]
target = 8
# print(combinationSum(candidates, target))


def decodeString(s, idx):
    decoded = ""
    n = len(s)
    while idx < n:
        currChar = s[idx]
        if currChar.isnumeric():
            while s[idx + 1].isnumeric():
                currChar += s[idx + 1]
            multi = int(currChar)
            subStr, idx = decodeString(s, idx + 2)
            decoded += subStr * multi
            print(subStr, multi)
            continue
        if currChar == ']':
            break
        decoded += s[idx]
        idx += 1
    return decoded, idx + 1


# print(head, '394. Decode String', head)
s = "3[a]2[bc]"
s = "3[a3[b3[c]]]"
# print(decodeString(s, 0))
