# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def LCS(sOne, sTwo, n, m):
    if not n or not m:
        return 0
    if sOne[n - 1] == sTwo[m - 1]:
        return 1 + LCS(sOne, sTwo, n - 1, m - 1)

    return max(LCS(sOne, sTwo, n - 1, m),
               LCS(sOne, sTwo, n, m - 1))


sOne = 'abcdaf'
sTwo = 'aebgc'
print(LCS(sOne, sTwo, len(sOne), len(sTwo)))
