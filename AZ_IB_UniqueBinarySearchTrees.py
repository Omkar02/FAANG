# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def uniqueBST(n, cache={0: 1}):
    if n in cache:
        return cache[n]
    total = 0
    for left in range(n):
        right = n - 1 - left
        lN = uniqueBST(left, cache)
        rN = uniqueBST(right, cache)

        total += (lN * rN)
    cache[n] = total
    return total


n = 3
print(uniqueBST(n))
