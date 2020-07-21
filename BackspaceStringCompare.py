import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Easy')

'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
'''


def BackspaceStringCompare(S, T):
    def BackspaceToString(s):
        idx = 0
        lengtsOfString = len(s)
        s = list(s)
        while idx < lengtsOfString - 1:
            if s[0] == '#':
                s.pop(0)
                lengtsOfString -= 1
            elif s[idx + 1] == '#':
                s.pop(idx + 1)
                s.pop(i)
                idx -= 2
                idx = idxif idx >= 0 else 0
                lengtsOfString -= 2
            else:
                idx += 1
        return s
    return BackspaceToString(S) == BackspaceToString(T)


S = "ab#c"
T = "a#c"


print(BackspaceStringCompare(S, T))
