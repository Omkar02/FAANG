# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def longestStringWithUnigque(string, k):
    letterPos = {}
    currLen = 0
    maxLen = float('-inf')
    startIdx = temp = 0
    n = len(string)

    for i in range(n):
        print(letterPos)
        if string[i] not in letterPos:
            letterPos[string[i]] = 0
        letterPos[string[i]] += 1
        currLen += 1
        if len(letterPos) > k:
            while letterPos[string[startIdx]] != 0:
                currLen -= 1
                letterPos[string[startIdx]] -= 1
                temp += 1
            del letterPos[string[startIdx]]
            startIdx = temp
            temp = 0

        endIdx = i

        if currLen > maxLen:
            maxLen = currLen
            res = [startIdx, endIdx]
    return maxLen, string[res[0]:res[1] + 1]


# string = "aabbcc"
# k = 1
string = "aabbccddeee"
k = 4

string = "WORLD"
k = 4
print(longestStringWithUnigque(string, k))
