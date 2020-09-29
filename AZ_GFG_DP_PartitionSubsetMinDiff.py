# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def minDiffPartition(array):
    total = sum(array)
    return getMinDiff(array, 0, 0, total, {})


def getMinDiff(array, idx, curSum, total, cache):
    cnt[0] += 1
    # print(cache)
    current = (idx, curSum)
    if current in cache:
        return cache[current]

    if idx == len(array) - 1:
        return abs((total - curSum) - curSum)

    cache[current] = min(getMinDiff(array, idx + 1, curSum + array[idx], total, cache),
                         getMinDiff(array, idx + 1, curSum, total, cache))

    return cache[current]


array = [1, 6, 11, 5]

# array = [3, 1, 4, 2, 2, 1]
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11

# 1
# [31]
# [Finished in 0.1s]

print(minDiffPartition(array))
print(cnt)
