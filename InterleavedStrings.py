import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def interWoven(one, two, three):
    cache = [[None for i in range(len(two) + 1)] for j in range(len(one) + 1)]
    return isWoven(one, two, three, 0, 0, cache)


def isWoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = isWoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = isWoven(one, two, three, i, j + 1, cache)
        return True

    cache[i][j] = False
    return False


three = 'aaafaaa'
one = 'aaa'
two = 'aaaf'


print(interWoven(one, two, three))
