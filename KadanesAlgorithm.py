import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def KadensALgo(array):
    maxSum = array[0]
    for i in range(1, len(array)):
        maxSum = max(maxSum + array[i], array[i])
    return maxSum


array = [1, 2, 3, -2, 5]
print(KadensALgo(array))
