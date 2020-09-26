# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def canPartition(array):
    total = sum(array)
    if total % 2 != 0:
        return False

    return heCanPartition(array, 0, 0, total, {})


def heCanPartition(array, index, CurrSum, total, cache):
    cnt[0] += 1
    current = f'{index} {CurrSum}'
    # print(cache)
    if current in cache:
        return cache[current]
    if CurrSum * 2 == total:
        return True

    if CurrSum > total / 2 or index >= len(array):
        return False

    cache[current] = heCanPartition(array, index + 1, CurrSum + array[index], total, cache) or heCanPartition(array, index + 1, CurrSum, total, cache)

    return cache[current]


array = [1, 5, 11, 5]
print(canPartition(array))

print(cnt)
