import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
Input:
The first line of the input contains T denoting the number of testcases. First line of each test case contains two space
separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent
line will be the N space separated array elements.

Output:
For each testcase, in a new line, output the rotated array.

Constraints:
1 <= T <= 200
1 <= N <= 107
1 <= D <= N
0 <= arr[i] <= 105

Example:
Input:
2
5 2
1 2 3 4 5
10 3
2 4 6 8 10 12 14 16 18 20
Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6
'''


def rotateArray(arr, rVal):
    rValNew = rVal % len(arr)
    if rValNew == 0:
        return arr
    if rValNew > 0:
        offset = len(arr) - rValNew
    else:
        offset = rValNew

    while offset != 0:
        val = arr.pop()
        arr.insert(0, val)
        offset -= 1
    return arr


print(rotateArray([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3))
print('8 10 12 14 16 18 20 2 4 6')
