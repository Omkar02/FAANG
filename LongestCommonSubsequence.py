import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def longestCommonSeq(stringOne, stringTwo):
    lcs = [[[None, 0, None, None] for x in range(len(stringOne) + 1)] for y in range(len(stringTwo) + 1)]
    print(stringOne, stringTwo)
    for i in range(len(stringTwo) + 1):
        for j in range(len(stringOne) + 1):

            if stringTwo[i - 1] == stringOne[j - 1]:
                lcs[i][j] = [stringTwo[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]

            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]

                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
        # [print(x) for x in lcs]
        # print()

    return buildSeq(lcs)


def buildSeq(lcs):
    seq = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        curEntry = lcs[i][j]
        if curEntry[0] is not None:
            seq.append(curEntry[0])
        i = curEntry[2]
        j = curEntry[3]

    return list(reversed(seq))


X = "AGGTAB"
Y = "GXTXAYB"
print(longestCommonSeq(X, Y))
