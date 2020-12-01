# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def isomorficString(str1, str2):
    if len(str1) != len(str2):
        return False
    has = {}
    n = len(str2)
    for i in range(n):
        if str1[i] not in has:
            has[str1[i]] = str2[i]
        elif has[str1[i]] != str2[i]:
            return False
        else:
            return True
    return False


str1 = "egg"
str2 = "add"

str1 = "foo"
str2 = "bar"

str1 = "paper"
str2 = "title"
print(isomorficString(str1, str2))
