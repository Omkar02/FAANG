# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findDup(nums):
    dup = []
    for val in nums:
        idx = abs(val) - 1
        if nums[idx] < 0:
            dup.append(abs(val))
        else:
            nums[idx] *= -1
    return dup


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDup(nums))
