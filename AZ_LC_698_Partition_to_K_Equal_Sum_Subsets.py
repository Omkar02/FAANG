# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4


def canPartitionKSubsets(nums, k) -> bool:
    if not nums or int(sum(nums) / k) != sum(nums) / k:
        return False
    nums.sort(reverse=True)
    parts = [sum(nums) / k] * k

    return dfs(parts, nums, 0)


def dfs(parts, nums, idx):
    if idx == len(nums):
        return True
    for i in range(len(parts)):
        if parts[i] >= nums[idx]:
            parts[i] -= nums[idx]
            if dfs(parts, nums, idx + 1):
                return True
            parts[i] += nums[idx]
    return False


print(canPartitionKSubsets(nums, k))
