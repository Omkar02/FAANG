# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='S', filename=fileName, Tag='Array', Difficult='Hard')


def maxSlidingWindow(nums, k):
    ans = []
    n = len(nums) - k + 1
    for i in range(n):

        currSlice = nums[i:i + k]
        print(currSlice)
        ans.append(max(currSlice))
    return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

nums = [1]
k = 1

nums = [9, 11]
k = 2

nums = [4, -2]
k = 2
print(maxSlidingWindow(nums, k))
