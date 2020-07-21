import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Easy')

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''


def MoveZeros(nums):
    left = 0
    while left < len(nums) - nums.count(0):
        if nums[left] == 0:
            nums.append(nums.pop(left))
        else:

            left += 1
    print(nums)


nums = [0, 1, 0, 3, 12]
nums = [0, 0, 1]

MoveZeros(nums)
