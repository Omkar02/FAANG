# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')

cnt = [0]


def premutation(nums, idx, ans):

    cnt[0] += 1
    if idx == len(nums) - 1:
        ans.append(nums[:])
    else:
        for i in range(idx, len(nums)):
            swap(nums, i, idx)
            premutation(nums, idx + 1, ans)
            swap(nums, i, idx)


def swap(a, s, o):
    a[s], a[o] = a[o], a[s]


nums = [1, 2, 3]
ans = []

premutation(nums, 0, ans)
print(ans)
print(cnt)
