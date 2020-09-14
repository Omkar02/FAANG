import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


nums = [2, 5, 1, 3, 4, 7]
n = 3
# Output: [2,3,5,4,1,7]


def shuffle(nums, n):
    ans = []
    p1 = 0
    p2 = n
    i = 0
    while i < n:
        ans.append(nums[p1])
        ans.append(nums[p2])
        p1 += 1
        p2 += 1
        i += 1
    return ans


print(shuffle(nums, n))
