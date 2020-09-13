# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# def smallerNumbersThanCurrent(nums):
#     sortedNums = sorted(nums)
#     counts = {}
#     sVal = 0
#     n = len(nums)

#     for i in range(n):
#         if sortedNums[i] not in counts:
#             counts[sortedNums[i]] = sVal
#             sVal += 1

#         else:
#             sVal += 1

#     return [counts[i] for i in nums]

def smallerNumbersThanCurrent(nums):
    sortedNums = sorted(nums)
    counts = {}
    val = 0
    n = len(nums)
    for i in range(n):
        if sortedNums[i] not in counts:
            counts[sortedNums[i]] = val
            val += 1
        else:
            val += 1
    return [counts[x] for x in nums]


nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))
