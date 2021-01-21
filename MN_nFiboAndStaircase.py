# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def fib(n, cache):
    cnt[0] += 1
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]


print(fib(20, {}))
print(cnt)
