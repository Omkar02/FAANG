import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxSubarray(array, k):
    n = len(array)
    minSum = 0
    for i in range(n):
        if array[i] < k:
            # array[i] = -1
            minSum -= 1
        elif array[i] > k:
            # array[i] = 1
            minSum += 1
        else:
            # array[i] = 0
            continue
    print(array)
    # minSub = sum(array)
    return n - minSum


array = [5, 9, 7, 8, 2, 4]
k = 5
print(f'The max Len = {maxSubarray(array,k)}')
