# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kMostSortedEle(nums, k):
    nums = {e: nums.count(e) for e in set(nums)}
    return sorted(nums, key=lambda a: nums[a], reverse=True)[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(kMostSortedEle(nums, k))
