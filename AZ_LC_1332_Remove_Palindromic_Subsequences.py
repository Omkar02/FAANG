# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Easy')


def minRemoval(string):
    if not string:
        return 0
    if string[::-1] == string:
        return 1
    return 2
s ='abaeba'
print(minRemoval(s))