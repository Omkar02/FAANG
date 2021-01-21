# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def optimalStrategy(array, i, j, currSum):
    cnt[0] += 1
    if i + 1 == j:
        return max(array[i], array[j])
    return max(currSum - optimalStrategy(array, i + 1, j, currSum - array[i]),
               currSum - optimalStrategy(array, i, j - 1, currSum - array[j]))


array = [20, 30, 2, 2, 2, 10]

print(optimalStrategy(array, 0, len(array) - 1, sum(array)))
print(cnt)
