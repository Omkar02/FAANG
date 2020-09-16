# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')

nums1 = [1, 3]
nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]

nums1 = []
nums2 = [1]


def findMedianSortedArrays(nums1, nums2):
    sort = sorted(nums1 + nums2)
    n = len(sort)
    m = n // 2
    if n % 2 == 0:
        median = (sort[m] + sort[m - 1]) / 2
    else:
        median = sort[m]
    return median


print(findMedianSortedArrays(nums1, nums2))
