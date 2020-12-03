# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def backspaceSting(strOne, strTwo):
    r1 = _Backhelper(strOne)
    r2 = _Backhelper(strTwo)
    print(r1, r2)
    return r1 == r2


def _Backhelper(strX):
    remaning = []
    skip = 0
    for i in reversed(strX):
        if i == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            remaning.append(i)
    return remaning


S = "ab#c"
T = "ad#c"

S = "ab##"
T = "c#d#"

S = "a##c"
T = "#a#c"
print(backspaceSting(S, T))
