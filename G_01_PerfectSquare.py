import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


# Given a positive integer n, find the least number of perfect square
# numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

'''
formula:
    dp[i][j] = min(dp[i], dp[i - j * j] + 1)
'''

import math


def perfectSquare(n):
    if n < 4:
        return n
    dp = [i for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            # print(int(math.sqrt(i)) + 1, '--', dp[i - j * j], i - j * j)
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[-1]


n = 12
print(perfectSquare(n))
