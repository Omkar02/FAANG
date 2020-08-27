import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kadensAlgo(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    startIdx = 0
    endIdx = 0
    currMax = 0
    overAllMax = 0

    total = 0
    tempIdx = 0

    for i in range(n):

        currMax += nums[i]

        if currMax > overAllMax:
            endIdx = i
            overAllMax = currMax
            startIdx = tempIdx

        if currMax < 0:
            tempIdx = i + tempIdx
            currMax = 0

    return overAllMax  # nums[startIdx:endIdx + 1]


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1]
nums = [-2, 1]
print(kadensAlgo(nums))
