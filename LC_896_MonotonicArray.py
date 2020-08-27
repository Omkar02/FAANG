# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


arr = [1, 2, 2, 3]
# arr = [1, 3, 2]


def isMonotonic(arr):
    isIncreasing = True
    isDecreasing = True

    n = len(arr)
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            isIncreasing = False

        if arr[i - 1] < arr[i]:
            isDecreasing = False

    return isIncreasing or isDecreasing


print(isMonotonic(arr))
