# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def partition(array, low, high):
    if low > high:
        return -1

    if low == high:
        return low

    mid = (low + high) // 2
    print([mid])

    if array[mid] == 0:
        return partition(array, mid + 1, high)
    elif array[mid] == 1:
        return partition(array, low, mid)


array = [0, 0, 0, 0, 1, 1, 1]
array = [0, 0, 0, 1, 1]
array = [0, 0, 0, 0, 1, 1, 1, 1]

print(f'The partition = {partition(array,0,len(array)-1)}')
