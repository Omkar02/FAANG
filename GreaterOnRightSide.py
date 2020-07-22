
import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Hard')


'''
You are given an array A of size N. Replace every element with the next
greatest element (greatest element on its right side) in the array. Also,
since there is no element next to the last element, replace it with -1.

Input:
The first line of input contains an integer T denoting the number of test cases.
T testcases follow. Each testcase contains two lines of input. The first line is
N, the size of tha array. The second line contains N space separated integers.
'''


def greaterOnRightSide(array):
    # for i in range(len(array) - 1):
    #     currMax = -1
    #     for j in range(i, len(array) - 1):
    #         currMax = max(currMax, array[j + 1])
    #     array[i] = currMax
    # array[len(array) - 1] = -1

    for i in range(len(array)):
        array[i] = max(array[i + 1:len(array)]) if len(array[i + 1:len(array)]) != 0 else -1
    print(array)


array = [16, 17, 4, 3, 5, 2]
greaterOnRightSide(array)
