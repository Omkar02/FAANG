# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def letterCasePermutation(s):
    ans = []
    _casePerHelper(s, '', ans)
    return ans


def _casePerHelper(s, tmpStr, ans):
    if not s:
        ans.append(tmpStr)
        return
    currStr = s[0]
    if currStr.isalpha():
        _casePerHelper(s[1:], tmpStr + currStr.lower(), ans)
        _casePerHelper(s[1:], tmpStr + currStr.upper(), ans)
    else:
        _casePerHelper(s[1:], tmpStr + currStr, ans)


s = '1a2b3'
print(letterCasePermutation(s))
