# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def searchRange(nums, target):
    finalRange = [-1, -1]
    n = len(nums) - 1
    bHelper(nums, target, 0, n, finalRange, True)
    bHelper(nums, target, 0, n, finalRange, False)

    return finalRange


def bHelper(nums, target, lo, hi, f, goLeft):
    cnt[0] += 1
    if lo > hi:
        return
    mid = (lo + hi) // 2
    if nums[mid] < target:
        bHelper(nums, target, mid + 1, hi, f, goLeft)
    elif nums[mid] > target:
        bHelper(nums, target, lo, mid + 1, f, goLeft)
    else:
        if goLeft:
            if mid == 0 or nums[mid - 1] != target:
                f[0] = mid
            else:
                bHelper(nums, target, lo, mid - 1, f, goLeft)
        else:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                f[1] = mid
            else:
                bHelper(nums, target, mid + 1, hi, f, goLeft)


nums = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
print(searchRange(nums, target))
print(cnt[0] / len(nums))
