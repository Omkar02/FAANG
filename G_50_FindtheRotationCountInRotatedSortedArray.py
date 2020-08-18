# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def findRotation(array, low, high):
    if low > high:
        return None
    if low == high:
        return low

    mid = (low + high) // 2

    if array[mid] > array[mid + 1]:
        return mid + 1
    if array[mid - 1] > array[mid]:
        return mid

    if array[high] > array[mid]:
        return findRotation(array, low, mid - 1)
    return findRotation(array, mid + 1, high)


array = [15, 18, 2, 3, 6, 12]
# array = [7, 9, 11, 12, 5]
array = [7, 9, 11, 12, 15]

print(f'Rotation Index = {findRotation(array,0,len(array)-1)}')
