# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Easy')

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
'''


def RemoveElements(nums, target):
    nums.sort()
    n = nums.count(val)
    for i in range(len(nums)):
        if nums[i] == target:
            del nums[i:i + n]
            break

    return(len(nums))


nums = [3, 2, 2, 3]
val = 3

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(RemoveElements(nums, val)
      )
