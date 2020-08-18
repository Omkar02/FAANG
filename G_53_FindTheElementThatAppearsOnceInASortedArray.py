# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')

cnt = [0]


def nonRepeated(array, low, high):
    cnt[0] += 1
    if low > high:
        return -1

    if low == high:
        return array[low]

    mid = (low + high) // 2

    if mid % 2 == 0:
        if array[mid] == array[mid + 1]:
            return nonRepeated(array, mid + 1, high)
        else:
            return nonRepeated(array, low, mid)

    else:
        if array[mid] == array[mid - 1]:
            return nonRepeated(array, mid + 1, high)
        else:
            return nonRepeated(array, low, mid - 1)


array = [1, 1, 2, 4, 4, 5, 5, 6, 6]
# array = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]
print(f'Non-repeated = {nonRepeated(array,0,len(array)-1)}')
print(cnt)
