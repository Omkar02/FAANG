import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')
'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


# class Solution:
def twoSum(nums, target):
    previousVal = {}
    for idx, i in enumerate(nums):
        potentialMatch = target - i
        if potentialMatch in previousVal:
            return [idx, previousVal[potentialMatch]]

        previousVal[i] = idx
    return -1


nums = [2, 7, 11, 15]
target = 9


print(twoSum(nums, target))
