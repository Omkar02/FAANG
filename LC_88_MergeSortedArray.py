# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def merge(nums1, m, nums2, n):
    for i in nums1:
        if i == 0:
            del nums1[m:len(nums1)]
    for i in nums2:
        nums1.append(i)
    x = sorted(nums1)
    for i in range(len(x)):
        nums1[i] = x[i]

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


print(f'The Merged Array = {merge(nums1,m,nums2,n)}')
