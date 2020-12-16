# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def subSet(nums):
    out = [[]]
    n = len(nums)
    for num in nums:
        out += [curr + [num] for curr in out]

    return out


nums = [1, 2, 3]
print(subSet(nums))
