# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def minCoins(denomitaion, length, value, cache):
    cnt[0] += 1
    curr = (length, value)
    if curr in cache:
        return cache[curr]
    if value == 0:
        print(denomitaion[length - 1])
        return 1
    if value < 0:
        return 0
    if length <= 0 and value >= 1:
        return 0

    cache[curr] = minCoins(denomitaion, length - 1, value, cache) + minCoins(denomitaion, length, value - denomitaion[length - 1], cache)
    return cache[curr]


denomitaion = [1, 2, 3]
length = len(denomitaion)
value = 4
print(minCoins(denomitaion, length, value, {}))
print(cnt)
