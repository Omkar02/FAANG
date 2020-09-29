# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def longestCOmmonSubSeq(stringOne, stringTwo, n, m, cache):
    cnt[0] += 1
    current = (n, m)
    if current in cache:
        return cache[current]

    if not n or not m:
        return 0

    elif stringOne[n - 1] == stringTwo[m - 1]:
        cache[current] = 1 + longestCOmmonSubSeq(stringOne, stringTwo, n - 1, m - 1, cache)

    else:
        cache[current] = max(longestCOmmonSubSeq(stringOne, stringTwo, n, m - 1, cache),
                             longestCOmmonSubSeq(stringOne, stringTwo, n - 1, m - 1, cache))

    return cache[current]


stringOne = "AGGTAB"
stringTwo = "GXTXAYB"
print(longestCOmmonSubSeq(stringOne, stringTwo, len(stringOne), len(stringTwo), {}))
print(cnt)
