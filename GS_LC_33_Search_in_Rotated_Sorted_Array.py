# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def shiftedSearch(nums, lo, hi, target):
    if lo > hi:
        return-1
    mid = (lo + hi) // 2
    pMatch = nums[mid]

    if pMatch == target:
        return mid
    elif nums[lo] <= pMatch:
        if target < pMatch and target >= nums[lo]:
            return shiftedSearch(nums, lo, mid - 1, target)
        else:
            return shiftedSearch(nums, mid + 1, hi, target)
    else:
        if target > pMatch and target <= nums[hi]:
            return shiftedSearch(nums, mid + 1, hi, target)
        else:
            return shiftedSearch(nums, lo, mid - 1, target)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# nums = [4, 5, 6, 7, 8, 9, 1, 2, 3]
# target = 6
print(shiftedSearch(nums, 0, len(nums) - 1, target))
