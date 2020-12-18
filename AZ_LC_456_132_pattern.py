# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findPartten(nums):
    n = len(nums)
    if n < 3:
        return False
    stack = []
    right = float('-inf')
    for i in reversed(range(n)):
        if nums[i] < right:
            return True
        else:
            while stack and nums[i] > stack[-1]:
                right = stack.pop()
        stack.append(nums[i])
    return False


nums = [1, 2, 3, 4]
print(findPartten(nums))
