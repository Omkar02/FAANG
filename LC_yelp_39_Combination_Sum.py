# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')
cnt = [0]


def combinationSum(candidates, target):
    ans = []
    _comboHelper(candidates, target, [], ans, 0)
    return ans


def _comboHelper(candidates, target, temp, ans, idx):
    cnt[0] += 1
    if target < 0:
        return
    if target == 0:
        ans.append(temp)
        return
    for i in range(idx, len(candidates)):
        _comboHelper(candidates, target - candidates[i], temp + [candidates[i]], ans, i)


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
print(cnt)
