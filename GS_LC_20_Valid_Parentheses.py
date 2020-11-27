# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Stack', Difficult='Medium')


def validPrantenses(string):
    if len(string) % 2 != 0:
        return False
    opning = '{[('
    closing = '}])'
    stack = []
    brackets = {'}': '{', ')': '(', ']': '['}
    n = len(string)
    for i in range(n):
        if string[i] in opning:
            stack.append(string[i])
        elif string[i] in closing:
            if stack[-1] == brackets[string[i]]:
                stack.pop()
            else:
                return False
    return True


s = "()[]{}"
s = "([])"
s = "{[]}"
print(validPrantenses(s))
