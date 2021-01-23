# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

import sys


def smallDif(arr1, arr2):
    ans = ()
    diff = sys.maxsize
    arr1.sort()
    arr2.sort()
    p1 = p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        v1, v2 = arr1[p1], arr2[p2]
        if v1 == v2:
            return (v1, v2)
        currDiff = abs(v2 - v1)
        if currDiff < diff:
            df = (v1, v2)
            diff = currDiff
            if v1 < v2:
                p1 += 1
            else:
                p2 += 1
        else:
            print(1, currDiff, diff)
            if v1 < v2:
                p1 += 1
            else:
                p2 += 1
    return df


arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 15, 17]
print(smallDif(arr1, arr2))
# arr1.sort()
# arr2.sort()
# diff = sys.maxsize
# p1 = p2 = 0
# df = ()
# while p1 < len(arr1) and p2 < len(arr2):
#     v1, v2 = arr1[p1], arr2[p2]
#     if v1 == v2:
#         df = (v1, v2)
#         break
#     smDiff = abs(v1 - v2)
#     if smDiff < diff:
#         df = (v1, v2)
#         diff = smDiff
#         if v1 < v2:
#             p1 += 1
#         else:
#             p2 += 1
#     else:
#         if v1 < v2:
#             p1 += 1
#         else:
#             p2 += 1
# return df
