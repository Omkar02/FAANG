# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxSumMinProduct(nums):
    currVal = 0
    maxVal = float('-inf')
    startIdx = endIdx = 0
    prevProduct = 1
    for i in range(1, len(nums)):
        procuct = min(nums[startIdx:i]) * sum(nums[startIdx:i])

        # print(procuct, nums[startIdx:i + 1], '|', min(nums[startIdx:i + 1]))

        if procuct > maxVal:
            maxVal = procuct
            endIdx = i
        if procuct < maxVal:
            startIdx = i
            currVal = 0

    return maxVal


nums = [3, 1, 6, 4, 5, 2]
# nums = [4, 1, 2, 9, 3]
# Output: 60
print(maxSumMinProduct(nums))
