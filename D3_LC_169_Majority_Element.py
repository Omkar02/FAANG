# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]


" Boyer-Moore Voting Algorithm "


def majorityElement(nums):
    count = 0
    candidate = None
    for nu in nums:
        if count == 0:
            candidate = nu
        count += (1 if nu == candidate else -1)
    return candidate


nums = [3, 2, 3]
nums = [ 2, 2, 1, 1, 1, 2, 2]
# Output: 3
print(majorityElement(nums))
