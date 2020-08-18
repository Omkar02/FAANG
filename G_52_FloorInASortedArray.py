# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def floorSearch(array, low, high, x):
    if low > high:
        return -1

    if x >= array[high]:
        return array[high]

    mid = (low + high) // 2
    if x == array[mid]:
        return array[mid]

    if x >= array[mid - 1] and x < array[mid]:
        return array[mid - 1]
    if x < array[mid]:
        return floorSearch(array, low, mid - 1, x)
    return floorSearch(array, mid + 1, high, x)


array = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(f'floor = {floorSearch(array,0,len(array)-1,x)}')
