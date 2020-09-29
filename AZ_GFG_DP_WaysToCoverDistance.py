# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')
cnt = [0]


def wayTo(n, cache):
    cnt[0] += 1
    if n in cache:
        return cache[n]
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    cache[n] = wayTo(n - 1, cache) + wayTo(n - 2, cache) + wayTo(n - 3, cache)

    return cache[n]


n = 10
print(wayTo(n, {}))
print(cnt)

# 274
# [532]
