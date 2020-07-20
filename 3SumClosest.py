import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')
'''
Given an array nums of n integers and an integer target, find three integers in 
nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each 
input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

# nums = [-1, 2, 1, -4]
nums = [0, 0, 0]
target = 1


def threeSumCloset(nums, target):
    nums.sort()
    n = len(nums)
    closest_diff = float('Inf')
    out = []
    #
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            temp_list = [nums[i], nums[l], nums[r]]
            temp_sum = sum(temp_list)
            curr_diff = temp_sum - target
            if abs(curr_diff) < closest_diff:
                out = temp_list
                closest_diff = abs(curr_diff)
            if curr_diff == 0:
                return(sum(out))
            elif curr_diff > 0:
                r -= 1
            elif curr_diff < 0:
                l += 1

    return(sum(out))


print(threeSumCloset(nums, target))
