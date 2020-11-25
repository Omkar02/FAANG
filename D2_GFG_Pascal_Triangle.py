# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1


def pascalTri(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end=' ')
            c = c * (line - i) // i
        print()


pascalTri(5)
