# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def isValidate(pushed, popped):
    stack = []
    operationCnt = 0
    for x in range(len(pushed)):
        stack.append(pushed[x])

        while stack and operationCnt < len(popped) and stack[-1] == popped[operationCnt]:
            stack.pop()
            operationCnt += 1

    return len(popped) == operationCnt


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]


pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(isValidate(pushed, popped))
