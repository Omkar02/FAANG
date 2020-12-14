# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def simpleCalcu(equation):
    stack = []
    current_num = 0
    operator = '+'
    operators = {'+', '-', '*', '/'}
    nums = set(str(x) for x in range(10))
    for idx, char in enumerate(equation):
        if char in nums:
            current_num = current_num * 10 + int(char)
        if char in operators or idx == len(equation) - 1:
            if operator == "+":
                stack.append(current_num)
            elif operator == "-":
                stack.append(-current_num)
            elif operator == "*":
                stack[-1] = int(stack[-1] * current_num)
            else:
                stack[-1] = int(stack[-1] / current_num)
            current_num = 0
            operator = char
    return sum(stack)


s = "3+2*2"
print(simpleCalcu(s))
