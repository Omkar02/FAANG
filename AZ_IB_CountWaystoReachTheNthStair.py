# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def nWaysStair(n, cache):
    cnt[0] += 1
    if n in cache:
        return cache[n]

    if n == 0 or n == 1:
        return 1

    cache[n] = nWaysStair(n - 1, cache) + nWaysStair(n - 2, cache)
    # print(cache)
    return cache[n]


n = 100
print(nWaysStair(n, {}))
print(cnt)
