# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def removeAdj(s):
    i = 0
    while i + 1 < len(s):
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            if i >= 1:
                i -= 1
        else:
            i += 1
    return s


s = "abbaca"
print(removeAdj(s))
