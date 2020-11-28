import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def uniquePath(n, m):
    return _findPath(n - 1, m - 1, 0, 0, {})


def _findPath(n, m, i, j, cache):
    cnt[0] += 1
    curr = (i, j)
    if curr in cache:
        return cache[curr]

    if i == n or m == j:
        return 1

    cache[curr] = _findPath(n, m, i + 1, j, cache) + _findPath(n, m, i, j + 1, cache)
    return cache[curr]


n = 3
m = 7
print(uniquePath(n, m))
print(cnt)
