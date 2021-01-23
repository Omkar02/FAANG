# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def three_largest_val(nums):
    largArr = [0, 0, 0]
    for n in nums:
        updateLargest(n, largArr)
    return largArr


def updateLargest(val, arr):
    if val > arr[2]:
        helpUpdate(val, arr, 2)
    elif val > arr[1]:
        helpUpdate(val, arr, 1)
    elif val > arr[0]:
        helpUpdate(val, arr, 0)


def helpUpdate(val, arr, index):
    for i in range(index + 1):
        if index == i:
            arr[i] = val
        else:
            arr[i] = arr[i + 1]


arr = [141, 1, 17, -7, -27, 18, 541, 8, 7, 7]
print(three_largest_val(arr))
