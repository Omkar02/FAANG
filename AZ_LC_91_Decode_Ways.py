# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def numDecodeing(s):
    return _decodingHelper(s, {})


def _decodingHelper(s, cache):
    if not s:
        return 1

    if s[0] == '0':
        return 0

    if s in cache:
        return cache[s]

    res = 0
    res += _decodingHelper(s[1:], cache)
    if len(s) >= 2:
        if int(s[:2]) <= 26:
            res += _decodingHelper(s[2:], cache)
    cache[s] = res
    return cache[s]


s = '12'
print(numDecodeing(s))
