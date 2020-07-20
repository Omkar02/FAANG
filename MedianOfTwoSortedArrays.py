import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]
CodeTimeLogging(Flag='F', filename=fileName, Tag='Array')


'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

'''

nums1 = [3]
nums2 = [-1, -2]


def findMedianSortedArrays(nums1, nums2):
    l = sorted(nums1 + nums2)
    if len(l) % 2 == 0:
        return float((l[len(l) // 2] + l[len(l) // 2 - 1]) / 2)
    else:
        return float(l[len(l) // 2])


print(findMedianSortedArrays(nums1, nums2))
