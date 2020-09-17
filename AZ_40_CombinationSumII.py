# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]


# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def combinationSum2(candidates, target):
    candidates.sort()
    results = []
    combinationSumHelper(candidates, 0, [], target, results)
    return results


def combinationSumHelper(candidates, idx, current, target, results):

    if target == 0:
        print(current, end=' ')
        results.append(current)
        return
    if target < 0:
        return

    for i in range(idx, len(candidates)):
        if i == idx or candidates[i] != candidates[i - 1]:
            cnt[0] += 1
            current.append(candidates[i])
            combinationSumHelper(candidates, i + 1, current, target - candidates[i], results)
            current.pop()


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

combinationSum2(candidates, target)
print()
print(cnt)
# [1, 7],
# [1, 2, 5],
# [2, 6],
# [1, 1, 6]
