# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


"""
Problem:
Given a 01 matrix M, find the longest line of consecutive one in the matrix. 
The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
"""


qcnt = [0]


def longestLine(matrix):
    if not len(matrix):
        return -1

    ones = 0

    dp = [[0] * len(matrix[0])] * 4
    [print(x) for x in dp]

    for i in range(len(matrix)):
        old = 0
        for j in range(len(matrix[0])):
            qcnt[0] += 1
            if matrix[i][j]:
                dp[j][0] = dp[j - 1][0] + 1 if j > 0 else 1
                dp[j][1] = dp[j][1] + 1 if i > 0 else 1
                prev = dp[j][2]
                dp[j][2] = old + 1 if i > 0 and j > 0 else 1
                old = prev
                dp[j][3] = dp[j + 1][3] + 1 if i > 0 and j < len(matrix[0]) - 1 else 1

                ones = max(ones, max(max(dp[j][0], dp[j][1]), max(dp[j][2], dp[j][3])))
            else:
                old = dp[j][2]
                dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0
    return ones


matrix = [[0, 1, 1, 0],
          [0, 1, 1, 0],
          [0, 0, 0, 1]]
print(longestLine(matrix))
print(qcnt)
