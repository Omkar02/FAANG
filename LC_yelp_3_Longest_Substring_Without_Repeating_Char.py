# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def longestSubString(s):
    startIdx = 0
    lastOcc = {}
    ans = float('-inf')
    n = len(s)
    p = [-1, -1]
    for currIdx in range(n):
        if s[currIdx] in lastOcc:
            startIdx = max(startIdx, lastOcc[s[currIdx]])
        currLen = currIdx - startIdx + 1
        if currLen > ans:
            ans = currLen
            p = [startIdx, currIdx]
        lastOcc[s[currIdx]] = currIdx + 1

    return ans, s[p[0]:p[1] + 1]


s = 'abcabcbb'
s = 'bbbbb'
s = 'pwwkew'
print(longestSubString(s))
