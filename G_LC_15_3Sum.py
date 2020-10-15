# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def threeSum(nums):
    nums.sort()
    n = len(nums)
    target = 0
    triplet = set()
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            totalSum = nums[i] + nums[left] + nums[right]
            if totalSum == target:
                triplet.add((nums[i], nums[left], nums[right]))

                left += 1
                right -= 1
            if target > totalSum:
                left += 1

            elif target < totalSum:
                right -= 1
    return triplet


nums = [-1, 0, 1, 2, -1, -4]
nums = [-2, 0, 1, 1, 2]
print(threeSum(nums))
