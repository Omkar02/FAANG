# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def findLongestPali(s):
    return _paliHelper(s, 0, len(s) - 1, {})


def _paliHelper(s, lo, hi, cache):
    cnt[0] += 1
    curr = (lo, hi)
    if curr in cache:
        return cache[curr]
    if lo > hi:
        return 0
    if lo == hi:
        return 1

    if s[hi] == s[lo]:
        cache[curr] = _paliHelper(s, lo + 1, hi - 1, cache) + 2
        return cache[curr]

    cache[curr] = max(_paliHelper(s, lo + 1, hi, cache), _paliHelper(s, lo, hi - 1, cache))
    return cache[curr]


s = 'bbbab'
print(findLongestPali(s))
print(cnt)
