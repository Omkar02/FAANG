import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


# Given a string, find length of the longest repeating subseequence such that the two subsequence don't have same string character at same position, i.e., any i'th character in the two subsequences shouldn't have the same index in the original string.

# longest-repeating-subsequence

# Examples:
# Input: str = "abc"
# Output: 0
# There is no repeating subsequence

# Input: str = "aab"
# Output: 1
# The two subssequence are 'a'(first) and 'a'(second).
# Note that 'b' cannot be considered as part of subsequence
# as it would be at same index in both.

# Input: str = "aabb"
# Output: 2

# Input: str = "axxxy"
# Output: 2


def longestCommon(string):
    dp = [[0 for x in range(len(string) + 1)]for y in range(len(string) + 1)]

    for i in range(1, len(string) + 1):
        for j in range(1, len(string) + 1):
            if string[i - 1] == string[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i][j - 1],
                               dp[i - 1][j])
    return dp[-1][-1]


string = "ab"
print(longestCommon(string))
