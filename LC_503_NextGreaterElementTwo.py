# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def nextGreaterElements(nums):
    maxNum = -1
    n = len(nums)
    for i in reversed(range(n)):
        temp = nums[i]
        nums[i] = maxNum
        maxNum = max(maxNum, temp)

    return nums
    #     maxNum = -1
    # n = len(arr)
    # for i in reversed(range(n)):
    #     temp = arr[i]
    #     arr[i] = maxNum
    #     if temp > maxNum:
    #         maxNum = temp

    # return arr


nums = [17, 18, 5, 4, 6, 1]

nums = [3, 6, 1]
print(nextGreaterElements(nums))
