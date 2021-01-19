# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def minEditDist(sOne, sTwo, n, m):
    if not n:
        return m
    if not m:
        return n
    if sOne[n - 1] == sTwo[m - 1]:
        return minEditDist(sOne, sTwo, n - 1, m - 1)

    return 1 + min(minEditDist(sOne, sTwo, n - 1, m),
                   minEditDist(sOne, sTwo, n - 1, m - 1),
                   minEditDist(sOne, sTwo, n, m - 1))


sOne = "sunday"
sTwo = "saturday"

print(minEditDist(sOne, sTwo, len(sOne), len(sTwo)))
