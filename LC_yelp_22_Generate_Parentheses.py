# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')
cnt = [0]


def generatePranthesis(n):
    ans = []
    backtrack(n, '', 0, 0, ans)
    return ans


def backtrack(n, s, lo, hi, ans):
    cnt[0] += 1
    if len(s) == 2 * n:
        if isValid(s):
            ans.append(s)
        return
    if lo < n:
        backtrack(n, s + '(', lo + 1, hi, ans)
    if hi < lo:
        backtrack(n, s + ')', lo, hi + 1, ans)


def isValid(brackects):
    balance = 0
    for b in brackects:
        cnt[0] += 1
        balance = balance + 1 if b == '(' else balance - 1
        if balance < 0:
            return False
    return balance == 0


n = 3
print(generatePranthesis(n))
print(cnt)
