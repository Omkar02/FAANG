# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findLengthOfLCIS(nums):
    n = len(nums)
    startIdx = 0
    endIdx = 0
    tempIdx = 0

    maxLen = float('-inf')

    currLen = 1

    for i in range(n):
        # print(currLen, maxLen)
        if nums[i - 1] < nums[i]:
            currLen += 1

        elif nums[i - 1] > nums[i]:
            tempIdx = i
            currLen -= 1

        if currLen > maxLen:

            endIdx = i
            startIdx = tempIdx
            maxLen = currLen

    return nums[startIdx:endIdx + 1], maxLen


nums = [1, 3, 5, 4, 7]
nums = [2, 2, 2, 2, 2]
nums = [1, 2, 3, 4, 10, 6, 7]
print(findLengthOfLCIS(nums))
