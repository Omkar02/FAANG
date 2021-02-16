# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

import random


def pickRandom(weights):
    nums = [weights[0]]
    for i in range(1, len(weights)):
        nums.append(nums[-1] + weights[i])

    val = random.randrange(1, nums[-1] + 1)
    print(val)

    return getPos(val, nums)


def getPos(val, nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l


weights = [1, 3]
print(pickRandom(weights))
