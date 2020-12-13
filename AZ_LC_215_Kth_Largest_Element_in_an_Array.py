# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kLargest(nums, k):
    return quick_select(nums, k, 0, len(nums) - 1)


def quick_select(nums, k, start, end):
    if start == end:
        return nums[k - 1]
    l, r = start, end
    mid = l + (r - l) // 2
    pivot = nums[mid]
    while l <= r:
        while l <= r and nums[l] > pivot:
            l += 1
        while l <= r and nums[r] < pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    if r >= k - 1:
        return quick_select(nums, k, start, r)
    if l <= k - 1:
        return quick_select(nums, k, l, end)
    return nums[r + 1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kLargest(nums, k))
