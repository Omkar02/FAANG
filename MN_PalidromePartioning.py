# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def isPali(a):
    return a == a[::-1]


def paliPartition(string, i, j):
    if i >= j or isPali(string[i:j + 1]):
        return 0
    minCuts = float('inf')
    for k in range(i, j):
        currCuts = 1 + paliPartition(string, i, k) + paliPartition(string, k + 1, j)
        minCuts = min(minCuts, currCuts)
    return minCuts


string = 'abcba'
print(paliPartition(string, 0, len(string) - 1))
