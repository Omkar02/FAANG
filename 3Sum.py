import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')


'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all 
unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
nums = [-1, 0, 1, 2, -1, -4]
# nums = [12, 3, 1, 2, -6, 5, -8, 6]


def ThreeSum(nums, target):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


print(ThreeSum(nums, 0))
