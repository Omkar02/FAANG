# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def paliPartition(string, i, j, cache):
    cnt[0] += 1
    curr = (i, j)
    if curr in cache:
        return cache[curr]

    if i >= j or isPali(string[i:j + 1]):
        return 0

    partition = float('inf')

    for k in range(i, j):
        cache[curr] = 1 + paliPartition(string, i, k, cache) + paliPartition(string, k + 1, j, cache)
        partition = min(partition, cache[curr])
    return partition


def isPali(x):
    return x == x[::-1]


'Staircase Problem Fibonacci Series'


def Staircase(n, cache):
    print(cache)
    if n in cache:
        return cache[n]
    cnt[0] += 1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    cache[n] = Staircase(n - 1, cache) + Staircase(n - 2, cache) + Staircase(n - 3, cache)
    return cache[n]


string = 'ababbbabbababa'
# print(paliPartition(string, 0, len(string) - 1, {}))
print(Staircase(10, {}))
print(cnt)
