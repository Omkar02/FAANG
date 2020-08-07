import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def productPuzzel(array):
    dp = [1 for i in array]
    left = 1
    right = 1

    for i in range(len(dp)):
        dp[i] *= left
        left *= array[i]

    for j in reversed(range(len(array))):
        dp[j] *= right
        right *= array[j]

    return dp


array = [1, 2, 3, 4, 5]
#[120, 60, 40, 30, 24]
print(productPuzzel(array))
