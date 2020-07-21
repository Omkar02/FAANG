import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Medium')

'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''


def partitionLable(S):
    maxPosCharacter = {letter: index for index, letter in enumerate(S)}
    outlist = []
    count = 0
    currPosition = 0
    for index, letter in enumerate(S):
        count += 1
        currPosition = max(currPosition, maxPosCharacter[letter])
        if index == currPosition:
            outlist.append(count)
            count = 0
    return outlist


S = "ababcbacadefegdehijhklij"

print(partitionLable(S))
