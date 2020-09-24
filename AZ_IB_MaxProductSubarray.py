# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxProductArray(array):
    currMax = array[0]
    overAllMax = float('-inf')
    val = [-1, -1]
    start = 0
    for i in range(1, len(array)):
        currMax *= array[i]
        # overAllMax = max(overAllMax, currMax)
        if currMax > overAllMax:
            overAllMax = currMax
            val = [start, i]
            print(1)

        if currMax <= 0:
            currMax = 1
            start = i

    return overAllMax, array[val[0]:val[1] + 1]


array = [2, 3, -2, 4]  # 6
array = [-1, -3, -10, 0, 60]
array = [-2, -3, 0, -2, -40]
print(maxProductArray(array))
