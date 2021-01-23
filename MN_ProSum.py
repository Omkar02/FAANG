# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def proSum(nums, multiplier=1):
    total = 0
    for val in nums:
        if type(val) is list:
            total += proSum(val, multiplier + 1)
        else:
            total += val
    return total * multiplier


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(proSum(arr))
