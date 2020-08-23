import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


s = "input"
t = "ouput"
k = 9


s = 'abc'
t = 'bcd'
k = 10


def canBeMorfed(s, t, k):
    if len(s) != len(t):
        return False

    shift = [0 for _ in range(1, 27)]

    for i in range(len(s)):
        print(shift)
        if s[i] == t[i]:
            continue

        diff = (ord(t[i]) - ord(s[i])) % 26
        print(shift[diff] * 26)
        if shift[diff] * 26 + diff > k:
            return False
        shift[diff] += 1

    return True


print(canBeMorfed(s, t, k))
