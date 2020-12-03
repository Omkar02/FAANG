# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def relativeSortArray(arr1, arr2):
    arr1.sort()
    ans = []
    n = len(arr1)
    temp = []
    count = {x: arr1.count(x) for x in set(arr1)}
    for i in arr2:
        while count[i] != 0:
            ans.append(i)
            count[i] -= 1

    for i in range(n):

        while arr1[i] in count and count[arr1[i]] != 0:
            ans.append(arr1[i])
            count[arr1[i]] -= 1
    return ans


arr = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
# out = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
# arr = [28, 6, 22, 8, 44, 17]
# arr2 = [22, 28, 8, 6]
print(relativeSortArray(arr, arr2))
