# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')

cnt = [0]


def countZeros(array, low, high):
    cnt[0] += 1

    if low >= high:
        return len(array) - 1

    mid = (low + high) // 2
    if array[mid - 1] == 1 and array[mid] == 0:
        return len(array) - mid

    if array[mid] == 1:
        return countZeros(array, mid + 1, high)

    else:
        return countZeros(array, low, mid)


array = [1, 1, 1, 1, 0, 0]
# array = [1, 0, 0, 0]
# array = [0, 0, 0, 0, 0, 0, 0]
print(f'0 Count = {countZeros(array,0,len(array)-1)}')
print(cnt)
