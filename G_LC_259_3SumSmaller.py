# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def threeSumMin(nums, target):
    n = len(nums)
    out = 0
    val = []
    for i in range(n - 2):
        j = i + 1
        for k in range(j + 1, n):
            if (nums[i] + nums[j] + nums[k]) < target:
                out += 1
                val.append((nums[i], nums[j], nums[k]))

    return out, val


nums = [-2, 0, 1, 3]
target = 2

print(threeSumMin(nums, target))
