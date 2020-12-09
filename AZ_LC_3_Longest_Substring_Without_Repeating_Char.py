import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def LSWRC(s):
    startIdx = 0
    lastOcc = {}
    ans = float('-inf')
    for currIdx in range(len(s)):
        if s[currIdx] in lastOcc:
            startIdx = max(startIdx, lastOcc[s[currIdx]])
        ans = max(ans, currIdx - startIdx + 1)
        lastOcc[s[currIdx]] = currIdx + 1
    return ans


s = 'abcabcbb'
print(LSWRC(s))
