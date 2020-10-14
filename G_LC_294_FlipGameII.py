import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def canwin(s):
    if not s or len(s) == 2:
        return False
    n = len(s) - 1
    for i in range(n):
        if s[i] == "+" and s[i + 1] == "+":
            nextState = s[0:i] + "--" + s[i + 1]

            if not canwin(nextState):
                return False
    return True


s = "++++"
print(canwin(s))
