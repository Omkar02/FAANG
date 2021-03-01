# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def t(n):
    a = '*' * 15
    print(f'{a} {n} { a}')


def KnapSack(bagW, itemWei, itemVal, idx):
    if bagW == 0 or idx == 0:
        return 0

    if itemWei[idx - 1] > bagW:
        return KnapSack(bagW, itemWei, itemVal, idx - 1)

    return max(itemVal[idx - 1] + KnapSack(bagW - itemWei[idx - 1],
                                           itemWei, itemVal, idx - 1),
               KnapSack(bagW, itemWei, itemVal, idx - 1))


itemVal = [60, 100, 120]
itemWei = [10, 20, 30]

bagW = 50
idx = len(itemWei)
# t('KnapSack')
# print(KnapSack(bagW, itemWei, itemVal, idx))


def LCS(sOne, sTwo, n, m):
    if not n or not m:
        return 0

    if sOne[n - 1] == sTwo[m - 1]:
        return 1 + LCS(sOne, sTwo, n - 1, m - 1)

    else:
        return max(LCS(sOne, sTwo, n - 1, m),
                   LCS(sOne, sTwo, n, m - 1))


sOne = 'abcdaf'
sTwo = 'aebgc'
# t('Longest Common Subsequence')
# print(LCS(sOne, sTwo, len(sOne), len(sTwo)))


def coinChage(denom, target, idx):
    if target == 0:
        return 0
    coin = float('inf')
    for i in range(idx):
        if denom[i] <= target:
            currCoin = coinChage(denom, target - denom[i], idx)
            coin = min(coin, currCoin + 1)
    return coin


denom, target = [1, 2, 3], 12
# t('Coin Change')
# print(coinChage(denom, target, len(denom)))


def minEditDist(sOne, sTwo, n, m):
    if not n:
        return m
    if not m:
        return n
    if sOne[n - 1] == sTwo[m - 1]:
        return minEditDist(sOne, sTwo, n - 1, m - 1)

    return 1 + min(minEditDist(sOne, sTwo, n, m - 1),
                   minEditDist(sOne, sTwo, n - 1, m),
                   minEditDist(sOne, sTwo, n - 1, m - 1))


sOne = "sunday"
sTwo = "saturday"
# t('Minimum Edit Distance')
# print(minEditDist(sOne, sTwo, len(sOne), len(sTwo)))


def LIS(array):
    tLength = [1 for _ in array]
    n = len(array)
    maxLen = float('-inf')
    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j] and tLength[i] < tLength[j] + 1:
                tLength[i] = tLength[j] + 1
                maxLen = tLength[j] + 1
    return maxLen


array = [10, 22, 9, 33, 21, 50, 41, 60]
# t('Longest Increasing Subsequence')
# print(LIS(array))


def LPS(string, i, j):
    if i == j:
        return 1
    if string[i] == string[j] and i + 1 == j:
        return 2

    if string[i] == string[j]:
        return 2 + LPS(string, i + 1, j - 1)
    return max(LPS(string, i + 1, j),
               LPS(string, i, j - 1))


string = 'GEEKSFORGEEKS'
# t('Longest Palindromic Subsequence')
# print(LPS(string, 0, len(string) - 1))


def cutRod(rodPrice, n):
    if n <= 0:
        return 0
    maxPrice = float('-inf')
    for i in range(n):
        currPrice = rodPrice[i] + cutRod(rodPrice, n - i - 1)
        if currPrice > maxPrice:
            maxPrice = currPrice
    return maxPrice


rodPrice = [1, 5, 8, 9, 10, 17, 17, 20]
# t('Cutting Rod')
# print(cutRod(rodPrice, len(rodPrice)))


def LongestCommonS(sOne, sTwo, n, m, count):
    if not n or not m:
        return count
    if sOne[n - 1] == sTwo[m - 1]:
        return LongestCommonS(sOne, sTwo, n - 1, m - 1, count + 1)

    return max(LongestCommonS(sOne, sTwo, n - 1, m, 0),
               LongestCommonS(sOne, sTwo, n, m - 1, 0))


sOne = "GeeksforGeeks"
sTwo = "GeeksQuiz"
# t("Longest Common Substring")
# print(LongestCommonS(sOne, sTwo, len(sOne), len(sTwo), 0))


def optimalGame(array, i, j, currSum):
    if j == i + 1:
        return max(array[i], array[j])
    return max(currSum - optimalGame(array, i + 1, j, currSum - array[i]),
               currSum - optimalGame(array, i, j - 1, currSum - array[j]))


array = [20, 30, 2, 2, 2, 10]
# t("Optimal Game Strategy")
# print(optimalGame(array, 0, len(array) - 1, sum(array)))


def isPali(a):
    return a == a[::-1]


def PP(string, i, j):
    if i >= j or isPali(string[i:j + 1]):
        return 0
    mp = float('inf')
    for k in range(i, j):
        count = 1 + PP(string, i, k) + PP(string, k + 1, j)
        mp = min(mp, count)
    return mp


string = 'abcbm'
# t("Palindrome Partition")
# print(PP(string, 0, len(string) - 1))


def SP(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return SP(n - 1) + SP(n - 2)


n = 4
t("Staircase Problem / Fibonacci Series")
print(SP(n))
