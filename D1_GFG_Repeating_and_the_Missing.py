# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findMissAndRep(nums):
    n = len(nums)
    for i in range(n):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        else:
            print(f'the Repeating num  = {abs(nums[i])}')

    """for the missing"""
    for i in range(n):
        if nums[i] > 0:
            print(f'the missing num = {i+1}')


nums = [7, 3, 4, 5, 5, 6, 2]

findMissAndRep(nums)
