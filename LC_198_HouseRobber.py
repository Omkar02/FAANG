# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def rob(nums):
    if not nums:
        return 0

    if len(nums) < 3:
        return max(nums)

    for i in range(2, len(nums)):
        if i == 2:
            nums[i] += nums[i - 2]
        else:
            nums[i] += max(nums[i - 2], nums[i - 3])

    return max(nums[-2:])


nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
nums = [1, 2]
print(rob(nums))
