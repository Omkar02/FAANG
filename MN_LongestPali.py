# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def longestPali(string, n, m, cache):
    cnt[0] += 1
    curr = (n, m)
    if curr in cache:
        return cache[curr]
    if n == m:
        return 1
    if string[n] == string[m] and n + 1 == m:
        return 2

    if string[n] == string[m]:
        cache[curr] = 2 + longestPali(string, n + 1, m - 1, cache)
        return cache[curr]
    cache[curr] = max(longestPali(string, n + 1, m, cache),
                      longestPali(string, n, m - 1, cache))
    return cache[curr]


string = 'GEEKSFORGEEKS'
print(longestPali(string, 0, len(string) - 1, {}))
