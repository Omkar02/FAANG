import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Medium')
'''
# Find the longest substring with k unique characters in a given string
# Given a string you need to print longest possible substring that has exactly M unique characters.
#  If there are more than one substring of longest possible len, then print any one of them.
# Examples:

# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.

# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.

# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with len 6.

# "aaabbb", k = 3
# There are only two unique characters, thus show error message.
# '''

# O(n) time| O(n) space


def longestSubString(string, k):
    stringCount = {x: 0 for x in string}
    stringCount[string[0]] = 1

    if len(stringCount) < k:
        return 'Not eneough Char!'

    maxFramSize = float('-inf')
    endIdx = 0
    startIdx = 0
    cut = [0, 0]
    while endIdx < len(string):
        endIdx += 1
        while not isValid(string[startIdx:endIdx + 1], k):
            startIdx += 1  # leaving the behind one

        if (endIdx - startIdx) > maxFramSize:
            cut = [startIdx, endIdx + 1]
            maxFramSize = endIdx - startIdx

    return string[cut[0]:cut[1]], len(string[cut[0]:cut[1]])


def isValid(string, k):
    stringCount = {x: 0 for x in string}
    print(string, len(stringCount), k)
    return len(stringCount) <= k


string = "aaabbccdddddde"
# string = "aabacbebebe"
k = 2
print(longestSubString(string, k))
