import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')


'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


def SearchRange(nums, target):
    finalRange = [-1, -1]

    SearchRangeHelper(nums, target, 0, len(nums) - 1, finalRange, True)
    SearchRangeHelper(nums, target, 0, len(nums) - 1, finalRange, False)

    return finalRange


def SearchRangeHelper(nums, target, left, right, finalRange, isLeft):
    if left > right:
        return
    mid = (left + right) // 2
    if nums[mid] < target:
        SearchRangeHelper(nums, target, mid + 1, right, finalRange, isLeft)
    elif nums[mid] > target:
        SearchRangeHelper(nums, target, left, mid - 1, finalRange, isLeft)
    else:
        if isLeft:
            if mid == 0 or nums[mid - 1] != target:
                finalRange[0] = mid
            else:
                SearchRangeHelper(nums, target, left, mid - 1, finalRange, isLeft)
        else:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                finalRange[1] = mid
            else:
                SearchRangeHelper(nums, target, mid + 1, right, finalRange, isLeft)


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(SearchRange(nums, target))
