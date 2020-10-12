# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Medium')

# arrange in the following
"""nums[0] < nums[1] > nums[2] < nums[3]..."""


def wiggleSort(nums):
    nums.sort()
    mid_index = len(nums[::2]) - 1
    nums[::2], nums[1::2] = nums[mid_index::-1], nums[:mid_index:-1]
    return nums


nums = [1, 5, 1, 1, 6, 4]
nums = [2, 4, 6, 8, 10, 20]

print(wiggleSort(nums))
