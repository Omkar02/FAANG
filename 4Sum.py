import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')


'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:

The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


def fourSum(nums, target):
    allPairSum = {}
    allCombination = []
    for i in range(1, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            currSum = nums[i] + nums[j]
            difference = target - currSum
            if difference in allPairSum:
                for pairs in allPairSum[difference]:
                    allCombination.append(pairs + [nums[i], nums[j]])

        for k in range(0, i):
            currSum = nums[i] + nums[k]
            if currSum not in allPairSum:
                allPairSum[currSum] = [[nums[k], nums[i]]]
            else:
                allPairSum[currSum].append([nums[k], nums[i]])
    return allCombination

    seen, result = collections.defaultdict(list), set()


import collections


def fourNumberSum(nums, target):
    seen, result = collections.defaultdict(list), set()
    for idx, num1 in enumerate(nums):
        for num2 in nums[idx + 1:]:
            rest = target - num1 - num2
            if (rest) in seen:
                result |= {tuple(sorted([num1, num2, pair[0], pair[1]])) for pair in seen[rest]}
        for num2 in nums[:idx]:
            seen[num1 + num2] += [[num1, num2]]

    return result


nums = [1, 0, -1, 0, -2, 2]
nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
print(fourSum(nums, target))
print(fourNumberSum(nums, target))
