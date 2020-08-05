import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Easy')

# O(n) time |O(1) space


def staircase(n):
    a, b = 0, 1
    for i in [1, 3, 5]:
        while n - i >= 0:
            a, b = b, a + b
            n -= 1
    return a

# O(n) time |O(n) space


def staircaseBottumUp(n):
    nums = [0] * (n + 1)
    nums[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in [1, 3, 20]:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total

    return nums[-1]


n = 8
print(staircase(n))
print(staircaseBottumUp(n))
