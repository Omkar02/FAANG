import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# Given a string, find out if the string is K-Palindrome or not.
# A k-palindrome string transforms into a palindrome on removing at most k characters from it.

# Examples :

# Input : String - abcdecba, k = 1
# Output : Yes
# String can become palindrome by remo-
# -ving 1 character i.e. either d or e)


# Input  : String - abcdeca, K = 2
# Output : Yes
# Can become palindrome by removing
# 2 characters b and e.

# Input : String - acdcb, K = 1
# Output : No
# String can not become palindrome by
# removing only one character.


def isKPalDP(string, revStr, n, m):

    # Create a table to store
    # results of subproblems
    dp = [[None for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # if sting at i is empty the min operation is j
            if not i:
                dp[i][j] = j
            # if sting at j is empty the min operation is i
            elif not j:
                dp[i][j] = i

            elif string[i - 1] == revStr[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # print(f'+++++++++++++++++++++++++{dp[i][j - 1]}++{dp[i-1][j]}')
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j])
            # [print(x) for x in dp]
            # print()

    return dp[m][n]


def isKPal(string, k):

    revStr = string[::-1]
    l = len(string)

    return (isKPalDP(string, revStr, l, l) <= k * 2)


# Driver program
string = "acdcb"
k = 2
print("Yes" if isKPal(string, k) else "No")
