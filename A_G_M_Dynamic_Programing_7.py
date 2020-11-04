# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


cnt = [0]


"Staircase Problem / Fibonacci Series"


def SP(n):
    cnt[0] += 1
    if n == 0 or n == 1:
        return n
    return SP(n - 1) + SP(n - 2)


n = 4
# print(SP(n + 1))
# print(cnt)

"Maximum Sum Increasing Subsequence"


def MSIS(nums):
    dp = [i for i in nums]
    seq = [None for _ in nums]
    n = len(nums)
    maxVal = float('-inf')
    for i in range(1, n):
        for j in range(0, i):
            cnt[0] += 1
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])
        maxVal = max(maxVal, dp[i])
    return maxVal


nums = [4, 6, 1, 3, 8, 4, 6]
# 4 -- 6 -- 8
nums = [1, 101, 2, 3, 100, 4, 5]
# print(MSIS(nums))
# print(cnt)


"Maximum Sum Subsequence Non-Adjacent"


def MSsNA(array, i, n, prev=float('-inf')):
    cnt[0] += 1
    if i == n:
        return 0
    exclude = MSsNA(array, i + 1, n, prev)
    include = 0
    if prev + 1 != i:
        include = array[i] + MSsNA(array, i + 1, n, i)
    return max(include, exclude)


array = [1, 2, 9, 4, 5, 0, 4, 11, 6]
# print(MSsNA(array, 0, len(array)))
# print(cnt)


"String Interleaving"


def woven(one, two, three):
    if len(one) + len(two) != len(three):
        return False
    return SI(one, two, three, 0, 0)


def SI(one, two, three, i, j):
    cnt[0] += 1
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        if SI(one, two, three, i + 1, j):
            return True
    if j < len(two) and two[j] == three[k]:
        return SI(one, two, three, i, j + 1)

    return False


one = "XXY"
two = "XXZ"
three = "XXXXZY"

print(woven(one, two, three))
print(cnt)
