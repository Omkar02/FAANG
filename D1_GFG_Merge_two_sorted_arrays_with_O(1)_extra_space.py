# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def mergeTwoArra(ar1, ar2):
    m, n = len(arr1), len(arr2)
    for i in range(n - 1, -1, -1):
        last = ar1[m - 1]
        j = m - 2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j + 1] = ar1[j]
            j -= 1

        # If there was a greater element
        if (j != m - 2 or last > ar2[i]):
            ar1[j + 1] = ar2[i]
            ar2[i] = last
    return ar1, ar2


arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
print(mergeTwoArra(arr1, arr2))
