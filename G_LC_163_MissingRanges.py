# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99


def missingRange(nums, lower, upper):
    missing = []
    nxt = lower
    for i in range(len(nums)):
        if lower == float('inf'):
            return res

        if nums[i] < nxt:
            continue

        if nums[i] == nxt:
            nxt += 1
            continue

        missing.append((nxt, nums[i] - 1))
        if nums[i] == float('inf'):
            return

        nxt = nums[i] + 1

    if nxt <= upper:
        missing.append((nxt, upper))
    return missing


print(missingRange(nums, lower, upper))
