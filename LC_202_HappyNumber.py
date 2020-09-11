# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Easy')


def isHappy(n):
    sums = set()
    while n not in sums:
        if n == 1:
            return True
        sums.add(n)
        n = sum(int(x)**2 for x in str(n))
        # print(n)

    return False


n = 19
print(isHappy(n))
