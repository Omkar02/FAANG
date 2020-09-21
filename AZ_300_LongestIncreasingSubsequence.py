# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


arr = [10, 9, 2, 5, 3, 7, 101, 18]


def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [-1] * n
    dp[0] = 1
    maxans = 1
    for i in range(1, n):
        maxval = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                maxval = max(maxval, dp[j])

        dp[i] = maxval + 1
        maxans = max(maxans, dp[i])
    return maxans


print(lengthOfLIS(arr))
