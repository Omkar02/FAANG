# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def sortArray(arr, n, A, B, C):
    for i in range(n):
        arr[i] = eval(arr[i], A, B, C)
    # get the maxIndex item
    index = -1
    maxEle = float('-inf')

    for i in range(n):
        if arr[i] > maxEle:
            maxEle = arr[i]
            index = i

    i, j = 0, n - 1
    k = 0
    newArr = [None for _ in range(n)]
    while i < index and j > index:

        if arr[i] < arr[j]:
            newArr[k] = arr[i]
            k += 1
            i += 1
        else:
            newArr[k] = arr[j]
            k += 1
            j -= 1

    while i < index:
        newArr[k] = arr[i]
        i += 1
        k = +1
    while j > index:
        newArr[k] = arr[j]
        j -= 1
        k += 1

    newArr[n - 1] = maxEle
    return newArr


def eval(x, A, B, C):
    return (A * x * x) + (B * x) + C


arr = [-1, 0, 1, 2, 3, 4]
n = len(arr)
A = -1
B = 2
C = -1

print(sortArray(arr, n, A, B, C))
