import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


cnt = [0]

"Count Number of Binary Search Tree Possible"


def BSTP(n):
    cnt[0] += 1
    if n == 0:
        return 1

    numTrees = 0
    for left in range(n):
        right = n - 1 - left
        lNode = BSTP(left)
        rNode = BSTP(right)

        numTrees += lNode * rNode
    return numTrees


# print(BSTP(3))
# print(cnt)

"Total Ways in Matrix"


def TWM(board):
    dp = [[1 for x in r] for r in board]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            cnt[0] += 1
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


board = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

# print(TWM(board))
# print(cnt)

"Longest Bitonic Subsequence"


def LBS(num):
    left = [1 for _ in num]
    right = [1 for _ in num]

    n = len(num)

    for i in range(1, n):
        for j in range(0, i):
            cnt[0] += 1
            if num[i] > num[j]:
                left[i] = max(left[i], left[j] + 1)
    print(left)

    for i in reversed(range(0, n)):
        for j in reversed(range(i, n)):
            cnt[0] += 1
            if num[i] > num[j]:
                right[i] = max(right[i], right[j] + 1)
    print(right)
    maxVal = float('-inf')
    for k in range(n):
        cnt[0] += 1
        curr = (left[k] + right[k]) - 1
        maxVal = max(maxVal, curr)

    return maxVal


num = [2, -1, 4, 3, 5, -1, 3, 2]
# print(LBS(num))
# print(cnt)

"Numbers WIthout Consecutive 1s in Binary Representation"


def NWCBR(n, lastDigit):
    cnt[0] += 1
    if n == 0:
        return 0
    if n == 1:
        return 1 if lastDigit == 1 else 2

    if lastDigit == 0:
        return NWCBR(n - 1, 0) + NWCBR(n - 1, 1)
    else:
        return NWCBR(n - 1, 0)


# print(NWCBR(5, 0))
# print(cnt)
