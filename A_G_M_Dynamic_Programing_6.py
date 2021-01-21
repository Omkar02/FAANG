# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


cnt = [0]

"Palindrome Partition"


def isPali(s):
    return s == s[::-1]


def PP(string, i, j):
    cnt[0] += 1
    if i >= j or isPali(string[i:j + 1]):
        return 0
    mp = float('inf')
    for k in range(i, j):
        count = 1 + PP(string, i, k) + PP(string, k + 1, j)
        mp = min(mp, count)

    return mp


string = 'abcbm'
print(PP(string, 0, len(string) - 1))
# print(cnt)


"Maximum Sub Square Matrix"


def MSSM(mat):
    row = len(mat)
    cols = len(mat[0])

    dp = [[0 for _ in range(cols + 1)] for _ in range(row + 1)]
    maxVal = float('-inf')
    for r in range(1, row + 1):
        for c in range(1, cols + 1):
            cnt[0] += 1
            dp[r][c] = mat[r - 1][c - 1] + min(dp[r - 1][c],
                                               dp[r - 1][c - 1],
                                               dp[r][c - 1])
            # dp[r][c] = '8'

            maxVal = max(maxVal, dp[r][c])
    [print(x) for x in dp]
    return maxVal


mat = [[0, 0, 1, 1, 1],
       [1, 0, 1, 1, 1],
       [0, 1, 1, 1, 1],
       [1, 0, 1, 1, 1]]
# print(MSSM(mat))
# print(cnt)


"Box Stacking"


def canBePlaced(c, o):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def BS(box):
    box.sort(key=lambda x: x[2])
    h = [x[2] for x in box]
    seq = [None for _ in box]
    mHIdx = 0
    n = len(box)
    for i in range(1, n):
        curr = box[i]
        for j in range(0, i):
            cnt[0] += 1
            other = box[j]
            if canBePlaced(curr, other):
                newH = curr[2] + h[j]
                if newH > h[i]:
                    h[i] = newH
                    seq[i] = j
        if h[i] >= h[mHIdx]:
            mHIdx = i

    return h[mHIdx]


box = [[2, 2, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
# print(BS(box))
# print(cnt)

"Burst Balloon"


def BB(nums, low, high):
    cnt[0] += 1
    if high - low < 2:
        maxCost = 0
    else:
        maxCost = 0
        for i in range(low + 1, high):
            cost = nums[low] * nums[i] * nums[high]
            maxCost = max(maxCost, cost + BB(nums, low, i) + BB(nums, i, high))
    return maxCost


nums = [3, 1, 5, 8]
nums = [1] + nums + [1]
# print(BB(nums, 0, len(nums) - 1))
# print(cnt)
