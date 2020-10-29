# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


"Wildcard Pattern Matching"


def WPM(string, pat, n, m, cache):
    cnt[0] += 1
    curr = (n, m)
    if curr in cache:
        return cache[curr]
    if m < 0 and n < 0:
        return True
    elif m < 0:
        return False
    elif n < 0:
        for i in range(m + 1):
            if pat[i] != '*':
                return False
        return True

    if pat[m - 1] == '*':
        cache[curr] = WPM(string, pat, n - 1, m, cache) or WPM(string, pat, n, m - 1, cache)
    else:
        if pat[m - 1] != '?' and pat[m - 1] != string[n - 1]:
            cache[curr] = False
        else:
            cache[curr] = WPM(string, pat, n - 1, m - 1, cache)
    return cache[curr]


strr = "baaabab"
pat = "*****ba*****ab"
# print(WPM(strr, pat, len(strr), len(pat), {}))
# print(cnt)


"Egg Dropping"


def ED(nEggs, kFloor):
    cnt[0] += 1
    if kFloor == 0 or kFloor == 1:
        return kFloor
    if nEggs == 1:
        return kFloor

    minVal = float("inf")
    for i in range(1, kFloor + 1):
        res = max(ED(nEggs - 1, i - 1),
                  ED(nEggs, kFloor - i))
        if res < minVal:
            minVal = res

    return minVal + 1


nEggs = 4
kFloor = 10
# print(ED(nEggs, kFloor))
# print(cnt)


"Longest Common Substring"


def LCSs(sOne, sTwo, n, m, count, cache):
    cnt[0] += 1
    curr = (n, m)
    if curr in cache:
        return cache[curr]
    if not m or not n:
        return count

    if sOne[n - 1] == sTwo[m - 1]:
        return LCSs(sOne, sTwo, n - 1, m - 1, count + 1, cache)

    cache[curr] = max(LCSs(sOne, sTwo, n - 1, m, 0, cache),
                      LCSs(sOne, sTwo, n, m - 1, 0, cache))
    return cache[curr]


sOne = "GeeksforGeeks"
sTwo = "GeeksQuiz"
# print(LCSs(sOne, sTwo, len(sOne), len(sTwo), 0, {}))
# print(cnt)
