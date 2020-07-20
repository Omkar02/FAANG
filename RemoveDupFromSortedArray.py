import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')
'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''


def getCountDup(nums):
    if not nums:
        return 0
    prev_index = 0
    prev = nums[0]
    x = 1

    while(prev != nums[-1]):

        if nums[x] != prev:
            prev = nums[x]
            nums[prev_index + 1] = prev
            prev_index += 1
        x += 1

    return prev_index + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(getCountDup(nums))
