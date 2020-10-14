# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def lengthOfLongestSubstring(s):
    count = []
    startIdx = 0
    endIdx = 0
    maxLen = float("-inf")
    currLen = 0
    p = [-1, -1]
    n = len(s)
    for i in range(n):
        count.append(s[i])
        currLen += 1
        if len(set(count)) != len(count):
            startIdx += 1
            currLen -= 1
            count.pop(0)

        if currLen > maxLen:
            maxLen = currLen
            endIdx = startIdx + currLen
            p = [startIdx, endIdx]

    return s[p[0]:p[1]], p[1] - p[0]


s = "abcabcbb"
s = "pwwkew"
# s = ""
# s = "bbb"
print(lengthOfLongestSubstring(s))
