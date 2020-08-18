import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')

cnt = [0]


def maxInBitonic(array, low, high):
    cnt[0] += 1
    if low > high:
        return None
    # if low == high:
    #     return array[low]
    mid = (low + high) // 2
    # print(array[mid])

    if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
        return array[mid]

    if array[mid] > array[mid + 1] and array[mid] < array[mid - 1]:
        print(array[mid + 1], array[mid], array[mid - 1])
        return maxInBitonic(array, low, mid - 1)
    return maxInBitonic(array, mid + 1, high)


array = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
# output = 500
print(f'MaxElement = {maxInBitonic(array,0,len(array)-1)}')
print(cnt)
