# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]


# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def permute(nums):
    ans = []
    phelp(0, nums, ans)
    return ans


def phelp(i, nums, ans):
    if i == len(nums):
        ans.append(nums[:])
        return

    for j in range(i, len(nums)):
        swap(nums, i, j)
        phelp(i + 1, nums, ans)
        swap(nums, i, j)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


nums = [1, 2, 3]
print(permute(nums))
