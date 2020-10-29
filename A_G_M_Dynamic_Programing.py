# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]

'KnapSack'


def KP(bagW, itemWei, itemVal, idx):
    cnt[0] += 1
    if bagW == 0 or idx == 0:
        return 0
    if itemWei[idx - 1] > bagW:
        return KP(bagW, itemWei, itemVal, idx - 1)
    else:
        return max(itemVal[idx - 1] + KP(bagW - itemWei[idx - 1], itemWei, itemVal, idx - 1),
                   KP(bagW, itemWei, itemVal, idx - 1))


itemVal = [60, 100, 120]
itemWei = [10, 20, 30]
bagW = 50
idx = len(itemWei)

# print(KP(bagW, itemWei, itemVal, idx))
# print(cnt)

'Longest Common Subsequence'


def LCS(sOne, sTwo, n, m):
    cnt[0] += 1
    if not n or not m:
        return 0

    if sOne[n - 1] == sTwo[m - 1]:
        return 1 + LCS(sOne, sTwo, n - 1, m - 1)

    else:
        return max(LCS(sOne, sTwo, n - 1, m),
                   LCS(sOne, sTwo, n, m - 1))


sOne = 'abcdaf'
sTwo = 'aebgc'
# print(LCS(sOne, sTwo, len(sOne), len(sTwo)))
# print(cnt)


'Matrix Chain Multiplication'


def MCM(arr, i, j):
    cnt[0] += 1
    if i == j:
        return 0
    minVal = float('inf')
    for k in range(i, j):
        val = MCM(arr, i, k) + MCM(arr, k + 1, j) + (arr[i - 1] * arr[k] * arr[j])
        minVal = min(minVal, val)
    return minVal


arr = [40, 20, 30, 10, 30]
# print(MCM(arr, 1, len(arr) - 1))
# print(cnt)


'Subset Sum Problem Dynamic Programming'


def SSP(array, currSum, idx):
    cnt[0] += 1
    if currSum == 0:
        return True

    if idx == 0:
        return False

    if array[idx - 1] > currSum:
        return SSP(array, currSum, idx - 1)

    else:
        return SSP(array, currSum - array[idx - 1], idx - 1) or SSP(array, currSum, idx - 1)


array = [3, 34, 4, 12, 5, 2]
target = 9
# print(SSP(array, target, len(array)))
# print(cnt)


'Coin Changing Minimum Number'


def CC(denom, idx, target):
    cnt[0] += 1
    if target == 0:
        return 1
    if target < 0:
        return 0
    if idx <= 0 and target >= 1:
        return 0

    return CC(denom, idx, target - denom[idx - 1]) + CC(denom, idx - 1, target)


denomination = [1, 2, 3]
idx = len(denomination)
target = 4
# print(CC(denomination, idx, target))
# print(cnt)
