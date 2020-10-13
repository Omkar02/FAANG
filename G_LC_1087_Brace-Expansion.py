# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')

import itertools


def expand(S):
    stack = []
    level = 0
    for idx, c in enumerate(S):
        if c == "{":
            level += 1
            stack.append([])
        elif c == "}":
            level -= 1
        elif c != ",":
            if level == 0:
                stack.append([c])
            else:
                stack[-1].append(c)

    return list(map("".join, itertools.product(*stack)))


S = "{a,b,c}d{e,f}"
print(expand(S))
