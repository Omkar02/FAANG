# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def editDist(stringOne, stringTwo, n, m, cache):
    cnt[0] += 1
    current = (n, m)
    if current in cache:
        return cache[current]
    if not n or not m:
        return 0

    elif stringOne[n - 1] == stringTwo[m - 1]:
        cache[current] = editDist(stringOne, stringTwo, n - 1, m - 1, cache)

    else:
        cache[current] = 1 + min(editDist(stringOne, stringTwo, n, m - 1, cache),        # Insert
                                 editDist(stringOne, stringTwo, n - 1, m, cache),        # Remove
                                 editDist(stringOne, stringTwo, n - 1, m - 1, cache))    # Replace
    return cache[current]


stringOne = "geek"
stringTwo = "gesek"
print(editDist(stringOne, stringTwo, len(stringOne), len(stringTwo), {}))
print(cnt)
