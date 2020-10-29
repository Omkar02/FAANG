# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def coinChange(target, denom):
    dp = [float('inf') for i in range(target + 1)]
    dp[0] = 0
    for den in denom:
        for ammount in range(target + 1):
            if ammount >= den:
                dp[ammount] = min(dp[ammount], 1 + dp[ammount - den])
    return dp[-1]


denom = [1, 2, 3]
target = 6
# print(coinChange(target, denom))

'Given weights and values of n items, put these items in a knapsack of capacity W'
'to get the maximum total value in the knapsack. In other words, '
'given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and '
'weights associated with n items respectively. Also given an integer W which represents '
'knapsack capacity, find out the maximum value subset of val[] such that sum of the weights '
'of this subset is smaller than or equal to W. You cannot break an item, either pick the complete '
'item or don’t pick it (0-1 property).'

cnt = [0]


def knapsack(bagWeight, itemValue, itemWeight, idx, cache):
    cnt[0] += 1
    curr = (bagWeight, idx)
    if curr in cache:
        return cache[curr]
    if bagWeight == 0 or idx == 0:
        return 0

    if itemWeight[idx - 1] > bagWeight:
        cache[curr] = knapsack(bagWeight, itemValue, itemWeight, idx - 1)

    else:
        cache[curr] = max(itemValue[idx - 1] +
                          knapsack(bagWeight - itemWeight[idx - 1], itemValue, itemWeight, idx - 1, cache),
                          knapsack(bagWeight, itemValue, itemWeight, idx - 1, cache))

    return cache[curr]


'GOAL--TO--MAXIMIZE--THE--THE--VALUE--WITH--GINEN--WEIGHT'
itemValue = [60, 100, 120]
itemWeight = [10, 20, 30]
bagWeight = 50
idx = len(itemWeight)

# print(knapsack(bagWeight, itemValue, itemWeight, idx, {}))
# print(cnt)
"Longest--Common--SubSequence"


def LCS(stringOne, stringTwo, idx1, idx2, cache):
    cnt[0] += 1
    curr = (idx1, idx2)
    if curr in cache:
        return cache[curr]
    if not idx1 or not idx2:
        return 0

    if stringOne[idx1 - 1] == stringTwo[idx2 - 1]:
        cache[curr] = 1 + LCS(stringOne, stringTwo, idx1 - 1, idx2 - 1, cache)

    else:
        cache[curr] = max(LCS(stringOne, stringTwo, idx1 - 1, idx2, cache),
                          LCS(stringOne, stringTwo, idx1, idx2 - 1, cache))
    return cache[curr]


stringOne = "AGGTAB"
stringTwo = "GXTXAYB"

# print(LCS(stringOne, stringTwo, len(stringOne), len(stringTwo), {}))
# print(cnt)

'Matrix Multiplication'
# Input: p[] = {40, 20, 30, 10, 30}
# Output: 26000
# There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
# Let the input 4 matrices be A, B, C and D.  The minimum number of
# multiplications are obtained by putting parenthesis in following way
# (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30


def matrixMultiplicationChain(arrays, i, j, cache):
    curr = (i, j)
    if curr in cache:
        return cache[curr]
    cnt[0] += 1
    if i == j:
        return 0

    minVal = float('inf')

    for k in range(i, j):
        cache[curr] = matrixMultiplicationChain(arrays, i, k, cache) + matrixMultiplicationChain(arrays, k + 1, j, cache) + (arrays[i - 1] * arrays[k] * arrays[j])

        minVal = min(minVal, cache[curr])

    return minVal


arrays = [1, 2, 3, 4, 3]
arrays = [40, 20, 30, 10, 30]
# print(matrixMultiplicationChain(arrays, 1, len(arrays) - 1, {}))
# print(cnt)
"subset sum problem top down"


def isSubsetSum(arrays, idx, cSum, cache):
    cnt[0] += 1
    curr = (cSum, idx)
    if curr in cache:
        return cache[curr]

    if cSum == 0:
        return True

    if idx == 0:
        return False

    if arrays[idx - 1] > cSum:
        cache[curr] = isSubsetSum(arrays, idx - 1, cSum, cache)

    cache[curr] = isSubsetSum(arrays, idx - 1, cSum - arrays[idx - 1], cache) or isSubsetSum(arrays, idx - 1, cSum, cache)

    return cache[curr]


arrays = [3, 34, 4, 12, 5, 2]
target = 9

# print(isSubsetSum(arrays, len(arrays), target, {}))
# print(cnt)


"Minimum--Edit--Distance"


def minEditDist(sOne, sTwo, idx1, idx2):
    cnt[0] += 1
    if not idx1:
        return idx2

    if not idx2:
        return idx1

    if sOne[idx1 - 1] == sTwo[idx2 - 1]:
        return minEditDist(sOne, sTwo, idx1 - 1, idx2 - 1)

    return 1 + min(minEditDist(sOne, sTwo, idx1 - 1, idx2 - 1),
                   minEditDist(sOne, sTwo, idx1 - 1, idx2),
                   minEditDist(sOne, sTwo, idx1, idx2 - 1))


sOne = "sunday"
sTwo = "saturday"

# print(minEditDist(sOne, sTwo, len(sOne), len(sTwo)))
# print(cnt)


"Longest--increase--Subseq"


def LIS(arrays):
    tl = [1 for _ in arrays]
    n = len(arrays)
    for i in range(1, n):
        for j in range(0, i):
            if arrays[i] > arrays[j] and tl[i] < tl[j] + 1:
                tl[i] = tl[j] + 1

    return max(tl)


# arrays = [10, 22, 9, 33, 21, 50, 41, 60]
# print(LIS(arrays))


"Optimal Binary Search Tree"

# Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}
# There can be following possible BSTs
#     10                12                 20         10              20
#       \             /    \              /             \            /
#       12          10     20           12               20         10
#         \                            /                 /           \
#          20                        10                12             12
#      I               II             III             IV             V
# Among all possible BSTs, cost of the fifth BST is minimum.
# Cost of the fifth BST is 1*50 + 2*34 + 3*8 = 142


def optimalSearchTree(keys, freq, n):
    return treeHelper(freq, 0, n - 1, {})


def treeHelper(frq, i, j, cache):
    curr = (i, j)
    cnt[0] += 1
    if curr in cache:
        return cache[curr]
    if i > j:
        return 0
    if i == j:
        return freq[i]

    fSum = getSum(freq, i, j)
    minVal = float('inf')

    for k in range(i, j + 1):
        cache[curr] = treeHelper(frq, i, k - 1, cache) + treeHelper(frq, k + 1, j, cache)
        minVal = min(minVal, cache[curr])

    cache[curr] = minVal + fSum
    return cache[curr]


def getSum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]

    return s


keys = [10, 12, 20, 11, 32]
freq = [34, 8, 50, 3, 4]
n = len(keys)
# print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))
# print(cnt)


'Longest Palindromic Subsequence'


def LPS(s, i, j, cache):
    # print(cache)
    cnt[0] += 1
    curr = (i, j)
    if curr in cache:
        return cache[curr]
    if i == j:
        return 1
    if seq[i] == seq[j] and i + 1 == j:
        return 2

    if seq[i] == seq[j]:
        return LPS(s, i + 1, j - 1, cache) + 2

    cache[curr] = max(LPS(s, i + 1, j, cache), LPS(s, i, j - 1, cache))
    return cache[curr]


seq = "GEEKSFORGEEKS"
n = len(seq)
# print("The length of the LPS is", LPS(seq, 0, n - 1, {}))
# print(cnt)
# [1467]


'Cutting Rod'
# Given a rod of length n inches and an array of prices that contains prices of
# all pieces of size smaller than n. Determine the maximum value obtainable by
# cutting up the rod and selling the pieces. For example, if length of the rod is
# 8 and the values of different pieces are given as following, then the maximum obtainable
# value is 22 (by cutting in two pieces of lengths 2 and 6)


# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# rodPrice    | 1   5   8   9  10  17  17  20


def cutRod(rodPrice, n, cache):
    cnt[0] += 1
    if n in cache:
        return cache[n]

    if n <= 0:
        return 0
    maxVal = float('-inf')
    for i in range(n):
        currVal = rodPrice[i] + cutRod(rodPrice, n - i - 1, cache)
        if currVal > maxVal:
            maxVal = currVal
            cache[n] = maxVal
    print(cache)
    return cache[n]


price = [1, 5, 8, 9, 10, 17, 17, 20]

# print(cutRod(price, len(price), {}))
# print(cnt)


'Egg Dropping'


def eggDropping(nEggs, kFloor, cache):
    cnt[0] += 1
    curr = (nEggs, kFloor)
    if curr in cache:
        return cache[curr]

    if kFloor == 0 or kFloor == 1:
        return kFloor
    if nEggs == 1:
        return kFloor

    minVal = float('inf')
    for i in range(1, kFloor + 1):
        res = max(eggDropping(nEggs - 1, i - 1, cache),
                  eggDropping(nEggs, kFloor - i, cache))
        if res < minVal:
            cache[curr] = res + 1
            minVal = res + 1
    print(cache)
    return minVal


n = 2
k = 10
# print(eggDropping(n, k, {}))
# print(cnt)


"Longest Common Substring"


def LCSs(sOne, sTwo, n, m, count):
    if not n or not m:
        return count
    if sOne[n - 1] == sTwo[m - 1]:
        count = LCSs(sOne, sTwo, n - 1, m - 1, count + 1)

    count = max(count, max(LCSs(sOne, sTwo, n - 1, m, 0),
                           LCSs(sOne, sTwo, n, m - 1, 0)))
    return count


sOne = "GeeksforGeeks"
sTwo = "GeeksQuiz"

# sOne = 'OldSite:GeeksforGeeks.org'
# sTwo = 'NewSite:GeeksQuiz.com'

print(LCSs(sOne, sTwo, len(sOne), len(sTwo), 0))
