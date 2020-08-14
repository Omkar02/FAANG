import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def LSsDup(string):
    if not string:
        return -1
    lastSeenIdx = {}
    longest = [0, 1]
    startIdx = 0
    for idx, char in enumerate(string):

        if char in lastSeenIdx:
            startIdx = max(startIdx, lastSeenIdx[char] + 1)
        if longest[1] - longest[0] < idx + 1 - startIdx:
            longest = [startIdx, idx + 1]

        lastSeenIdx[char] = idx

    return string[longest[0]:longest[1]]


string = "abcabcbb"
# string = "clementisacap"
# string = ''
print(LSsDup(string))
