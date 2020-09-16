# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6


# O(n^2 time|O(1) space)
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])


# O(n) time | O(n) space
def twoSum(nums, target):
    n = len(nums)
    preSum = {}

    for i in range(n):
        if nums[i] in preSum:
            return (nums[i], preSum[nums[i]])
        preSum[target - nums[i]] = nums[i]

    return (-1, -1)


# O(nlogN)  time | O(1) space
def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        currSum = nums[l] + nums[r]
        if target < currSum:
            r -= 1
        elif target > currSum:
            l += 1
        else:
            return (nums[l], nums[r])

    return (-1, -1)


print(twoSum(nums, target))
