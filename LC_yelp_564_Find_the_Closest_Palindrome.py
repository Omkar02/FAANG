# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Hard')


def findClosestPali(n):
    if not n:
        return -1
    if isPali(n):
        return n
    i = j = n
    cnt = 0
    while True:
        i += 1
        if isPali(i):
            return i
        j -= 1
        if isPali(j):
            return j
        cnt += 1
        if cnt == 100:
            return 'Ne!'


def isPali(s):
    s = str(s)
    return s == s[::-1]


n = 116
print(findClosestPali(n))
