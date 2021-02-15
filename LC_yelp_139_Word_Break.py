# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def wordBreak(s, wordDict):
    return _helpWordBreak(s, wordDict)


def _helpWordBreak(s, wordDict):
    if not s:
        return True
    if s in wordDict:
        return True

    for i in range(1, len(s) + 1):
        if s[:i] in wordDict and _helpWordBreak(s[i:], wordDict):
            return True
    return False


s = "leetcode"
wordDict = ["leet", "code"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

print(wordBreak(s, wordDict))
