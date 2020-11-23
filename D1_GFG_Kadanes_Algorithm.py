# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kadens(nums):
    maxSum = float('-inf')
    currSum = nums[0]
    start = 0
    end = 0

    for i in range(1, len(nums)):
        currSum += nums[i]
        if maxSum < currSum:
            end = i
            maxSum = currSum
        if currSum < 0:
            start = i + 1
            currSum = 0

    return maxSum, nums[start:end + 1]


nums = [-2, -3, 4, -1, -2, 1, 5, -3]


print(kadens(nums))
