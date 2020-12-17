# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def summaryRange(nums):
    lo = nums[0]
    hi = nums[0]
    n = len(nums)
    ans = []
    for i in range(1, n):
        if nums[i - 1] + 1 == nums[i]:
            hi = nums[i]
        else:
            ans.append(f'{lo}-->{hi}' if lo != hi else f'{lo}')
            hi = nums[i]
            lo = nums[i]

    ans.append(f'{lo}-->{hi}' if lo != hi else f'{lo}')
    return ans


nums = [0, 1, 2, 4, 5, 7]
print(summaryRange(nums))
