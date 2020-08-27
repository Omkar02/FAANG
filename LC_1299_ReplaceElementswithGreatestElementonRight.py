# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def replaceElements(arr):
    maxNum = -1
    n = len(arr)
    for i in reversed(range(n)):
        temp = arr[i]
        arr[i] = maxNum
        if temp > maxNum:
            maxNum = temp

    return arr


arr = [17, 18, 5, 4, 6, 1]
output = [18, 6, 6, 6, 1, -1]


va = replaceElements(arr)
print(output)
print(va == output)
