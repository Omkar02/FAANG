# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def revPolishNotation(tockens):
    stack = []
    n = len(tockens)
    number = set(str(x) for x in range(0, 100))
    symbols = {"*", "/", "+", "-"}
    for i in range(n):
        # print(stack)
        if tockens[i] in number:
            stack.append(int(tockens[i]))
            print(stack)

        if tockens[i] in symbols:
            preTockens = stack.pop()
            if tockens[i] == '+':
                stack[-1] = stack[-1] + preTockens

            elif tockens[i] == '-':
                stack[-1] = stack[-1] - preTockens

            elif tockens[i] == '*':
                stack[-1] = stack[-1] * preTockens

            else:
                stack[-1] = stack[-1] / preTockens
    return int(sum(stack))


tockens = ["2", "1", "+", "3", "*"]
tockens = ["4", "13", "5", "/", "+"]
print(revPolishNotation(tockens))
