# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def isValid(s):
    Parentheses = {'}': '{', ']': '[', ')': '('}
    isOpening = "({["
    isCloseing = ")}]"

    stack = []
    for i in s:
        if i in isOpening:
            stack.append(i)
        if i in isCloseing:
            lastVal = stack.pop() if stack else '-1'
            if lastVal != Parentheses[i]:
                return False

    return True if not stack else False


s = "()"

print(isValid(s))
