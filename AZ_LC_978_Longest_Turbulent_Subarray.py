# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def turbulentArray(nums):
    curr_len = 0
    max_len = float('-inf')
    n = len(nums)
    for i in range(n):
        if i >= 2 and (nums[i - 2] > nums[i - 1] < nums[i] or nums[i - 2] < nums[i - 1] > nums[i]):
            curr_len += 1
        elif i > 1 and nums[i - 1] != nums[i]:
            print(1)
            curr_len = 2
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)
    return max_len


nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(turbulentArray(nums))
