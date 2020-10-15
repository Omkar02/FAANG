# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def isInterleaved(stringOne, stringTwo, n, m, target, cache):
    curr = (n, m)
    if curr in cache:
        return cache[curr]
    k = n + m
    if k == len(target):
        return True
    if n < len(stringOne) and stringOne[n] == target[k]:
        cache[curr] = isInterleaved(stringOne, stringTwo, n + 1, m, target, cache)
        if cache[curr]:
            return True
    if m < len(stringTwo) and stringTwo[m] == target[k]:
        cache[curr] = isInterleaved(stringOne, stringTwo, n, m + 1, target, cache)
        if cache[curr]:
            return True

    return False


stringOne = "XXY"
stringTwo = "XXZ"
target = "XXXXZY"

print(isInterleaved(stringOne, stringTwo, 0, 0, target, {}))
