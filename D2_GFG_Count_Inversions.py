# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

invCnt = [0]


def mergeSort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    lHalf = arr[:mid]
    rHalf = arr[mid:]
    mergeSort(lHalf)
    mergeSort(rHalf)

    i, j, k = 0, 0, 0
    while i < len(lHalf) and j < len(rHalf):
        if lHalf[i] <= rHalf[j]:
            arr[k] = lHalf[i]
            i += 1
        else:
            arr[k] = rHalf[j]
            j += 1
            invCnt[0] += (mid - i)
        k += 1
    while i < len(lHalf):
        arr[k] = lHalf[i]
        i += 1
        k += 1
    while j < len(rHalf):
        arr[k] = rHalf[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    lHalf = arr[:mid]
    rHalf = arr[mid:]

    mergeSort(lHalf)
    mergeSort(rHalf)

    i, j, k = 0, 0, 0
    while i < len(lHalf) and j < len(rHalf):
        if lHalf[i] < rHalf[j]:
            arr[k] = lHalf[i]
            i += 1
        else:
            arr[k] = rHalf[j]
            j += 1
            invCnt[0] += (mid - i)
        k += 1
    while i < len(lHalf):
        arr[k] = lHalf[i]
        i += 1
        k += 1
    while j < len(rHalf):
        arr[k] = rHalf[j]
        j += 1
        k += 1


arr = [8, 4, 2, 1]
# arr = [3, 1, 2]
# arr = [1, 20, 6, 4, 5]
mergeSort(arr)
print(f'the inversion = {invCnt[0]}')
print(arr)
