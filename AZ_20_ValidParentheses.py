# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def isValid(string):
    isOpenening = '({['
    isCloseing = ')}]'

    baracketMap = {'}': '{',
                   ')': '(',
                   ']': '['}

    stack = []
    for i in string:
        if i in isOpenening:
            stack.append(i)
        elif stack and i in isCloseing and stack[-1] == baracketMap[i]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


string = '{{{'
print(isValid(string))
