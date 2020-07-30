import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

"""
Formula 
    if arr[j]<arr[i]:
        dp[i] = max(dp[i],  
                    dp[j]+1)
"""


def longestIncreasingSeq(array):
    dp = [1 for i in array]

    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[-1]


array = [3, 4, -1, 0, 6, 2, 3]
print(longestIncreasingSeq(array))
