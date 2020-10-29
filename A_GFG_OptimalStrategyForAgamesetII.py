# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def strategy(array, i, j, currSum, cache):
    cnt[0] += 1
    curr = (i, j)
    if curr in cache:
        return cache[curr]
    if j == i + 1:
        return max(array[i], array[j])

    cache[curr] = max(currSum - strategy(array, i + 1, j, currSum - array[i], cache), currSum - strategy(array, i, j - 1, currSum - array[j], cache))
    return cache[curr]


import random
array = [8, 15, 3, 7]
array = [5, 3, 7, 10]
array = [20, 30, 2, 2, 2, 10]

# array = [i for i in range(20)]
# random.shuffle(array)
# print(array)
print(strategy(array, 0, len(array) - 1, sum(array), {}))
print(cnt)
# [524287]
# [343]
