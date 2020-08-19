# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def missingEle(array1, array2, low, high):
    if low > high:
        return -1
    if low == high:
        return array1[low], low

    mid = (high + low) // 2

    if array1[mid] == array2[mid]:
        return missingEle(array1, array2, mid + 1, high)

    elif array1[mid] != array2[mid]:
        return missingEle(array1, array2, low, mid - 1)


array1 = [2, 4, 6, 8, 9, 10, 12]
array2 = [2, 4, 6, 8, 10, 12]

# array1 = [3, 5, 7, 9, 11, 13]
# array2 = [3, 5, 7, 11, 13]

high = len(array1) if len(array1) < len(array2) else len(array2)

print(f'The missing is = {missingEle(array1,array2,0,high)}')
