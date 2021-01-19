import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def longestIncreaseSeq(arr):
    dp = [1 for _ in arr]
    n = len(arr)
    maxLen = float('-inf')
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = 1 + dp[j]
                maxLen = max(maxLen, dp[i])
    return maxLen


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(longestIncreaseSeq(arr))
