# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]
'Minimum Edit Distance'


def MED(sOne, sTwo, n, m):
    cnt[0] += 1
    if not n:
        return m
    if not m:
        return n

    if sOne[n - 1] == sTwo[m - 1]:
        return MED(sOne, sTwo, n - 1, m - 1)

    return 1 + min(MED(sOne, sTwo, n - 1, m - 1),
                   MED(sOne, sTwo, n - 1, m),
                   MED(sOne, sTwo, n, m - 1))


sOne = "sunday"
sTwo = "saturday"
# print(MED(sOne, sTwo, len(sOne), len(sTwo)))
# print(cnt)


'Longest Increasing Subsequence'


def LIS(array):
    length = [1 for _ in array]
    n = len(array)
    maxLen = float('-inf')
    for i in range(1, n):
        for j in range(0, i):
            cnt[0] += 1
            if array[i] > array[j] and length[i] < length[j] + 1:
                length[i] = length[j] + 1
                maxLen = max(maxLen, length[i])

    return maxLen


array = [10, 22, 9, 33, 21, 50, 41, 60]
# print(LIS(array))
# print(cnt)


'Optimal Binary Search Tree'


def OBST(freq, i, j):
    cnt[0] += 1
    if i > j:
        return 0
    if i == j:
        return freq[i]

    cost = float('inf')
    fSum = sum(freq[i:j + 1])
    for k in range(i, j + 1):
        currCost = OBST(freq, i, k - 1) + OBST(freq, k + 1, j)
        cost = min(cost, currCost)

    return cost + fSum


freq = [34, 8, 50]
# print(OBST(freq, 0, len(freq) - 1))
# print(cnt)


'Longest Palindromic Subsequence'


def LPS(string, i, j):
    cnt[0] += 1
    if i == j:
        return 1
    if string[i] == string[j] and i + 1 == j:
        return 2

    if string[i] == string[j]:
        return 2 + LPS(string, i + 1, j - 1)

    return max(LPS(string, i + 1, j), LPS(string, i, j - 1))


string = 'GEEKSFORGEEKS'
# print(LPS(string, 0, len(string) - 1))
# print(cnt)


'Cutting Rod'


def CR(rodPrice, n):
    cnt[0] += 1
    if n <= 0:
        return 0

    maxPrice = float('-inf')
    for i in range(n):
        currPrice = rodPrice[i] + CR(rodPrice, n - i - 1)
        if currPrice > maxPrice:
            maxPrice = currPrice

    return maxPrice


# rodPrice = [1, 5, 8, 9, 10, 17, 17, 20]
# print(CR(rodPrice, len(rodPrice)))
# print(cnt)
