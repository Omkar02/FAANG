# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def combSum(digits, temp, ans, target, idx):
    cnt[0] += 1
    if target < 0:
        return
    if target == 0:
        ans.append(temp)

    for i in range(idx, len(digits)):
        combSum(digits, temp + [digits[i]], ans, target - digits[i], i)


digits = [2, 3, 6, 7]
target = 7
ans = []
combSum(digits, [], ans, target, 0)
print(ans)
print(cnt)
