# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


from sortedcontainers import SortedDict


def oddEvenJumps(a):

    if len(a) == 0:
        return 0
    if len(a) == 1:
        return 1

    n = len(a)
    isOkEven = [False] * len(a)
    isOkOdd = [False] * len(a)
    isOkEven[n - 1] = True
    isOkOdd[n - 1] = True
    od = SortedDict()
    od[a[n - 1]] = n - 1

    for i in range(n - 2, -1, -1):
        val = a[i]
        if val in od:
            isOkEven[i] = isOkOdd[od[val]]
            isOkOdd[i] = isOkEven[od[val]]
        else:
            smallestP = od.bisect_left(val)
            largestP = od.bisect_left(val) - 1
            isOkOdd[i] = True if smallestP != len(od) and isOkEven[od.peekitem(smallestP)[1]] else False
            isOkEven[i] = True if largestP != -1 and isOkOdd[od.peekitem(largestP)[1]] else False
        od[val] = i
    counter = 0
    for e in isOkOdd:
        if e:
            counter += 1
    return counter


a = [10, 13, 12, 14, 15]
print(oddEvenJumps(a))
