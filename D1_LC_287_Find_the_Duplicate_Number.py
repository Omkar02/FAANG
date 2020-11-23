# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findDuplicate(nums):
    """
    Floyd's Tortoise and Hare (Cycle Detection)
    """
    hare = tortoise = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if hare == tortoise:
            break
    tortoise = nums[0]
    while hare != tortoise:
        hare = nums[hare]
        tortoise = nums[tortoise]

    return hare


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
