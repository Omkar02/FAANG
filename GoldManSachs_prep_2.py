# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')
cnt = [0]

"LC_11. Container With Most Water"


def CMW(heights):
    water = [0 for _ in heights]
    n = len(heights)
    leftmax = 0
    for i in range(n):
        water[i] = leftmax
        leftmax = max(leftmax, heights[i])
    rightMax = 0
    for i in reversed(range(n)):
        minHeight = min(rightMax, water[i])
        if heights[i] < minHeight:
            water[i] = minHeight - heights[i]
        else:
            water[i] = 0
        rightMax = max(rightMax, heights[i])

    return sum(water)


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(CMW(heights))


'15. 3Sum'


def threSum(nums, target):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n - 2):
        j = i + 1
        for k in range(j + 1, n):
            currSum = nums[i] + nums[j] + nums[k]
            if currSum == 0:
                ans.append((nums[i], nums[j], nums[k]))
    return ans


nums = [-1, 0, 1, 2, -1, -4]
target = 0
# print(threSum(nums, target))


"16. 3Sum Closest"


def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest = float('inf')
    for i in range(n):
        lo, hi = i + 1, n - 1
        while lo < hi:
            currSum = nums[i] + nums[lo] + nums[hi]
            if abs(currSum - target) < abs(closest):
                closest = target - currSum

            if currSum < target:
                lo += 1
            else:
                hi -= 1
        if currSum == 0:
            break
    return target - closest


nums = [-1, 2, 1, -4]
target = 1
# print(threeSumClosest(nums, target))

"17. Letter Combinations of a Phone Number"


def letterCombination(digits):
    if not digits:
        return []
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    result = []
    _helpCombine('', digits, phone, result)
    return result


def _helpCombine(currString, leftOverdigit, phone, result):
    if not leftOverdigit:
        result.append(currString)
        return

    for char in phone[leftOverdigit[0]]:
        _helpCombine(currString + char, leftOverdigit[1:], phone, result)


digits = '23'
# print(letterCombination(digits))



