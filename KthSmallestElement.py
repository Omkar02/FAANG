import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

'''
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element
in the given array. It is given that all array elements are distinct.
Input:
The first line of input contains an integer T, denoting the number of testcases.
Then T test cases follow. Each test case consists of three lines. First line of
each testcase contains an integer N denoting size of the array. Second line contains N space separated
integer denoting elements of the array. Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''


def kSmallest(array, k):
    return kSmallestHelper(array, 0, len(array) - 1, k)


def kSmallestHelper(array, startIdx, endIdx, k):
    while True:

        piviot = startIdx
        l = startIdx + 1
        r = endIdx
        while l <= r:
            print(array)
            if array[l] > array[r] and array[r] < array[piviot]:
                swap(array, l, r)
            if array[l] <= array[piviot]:
                l += 1
            if array[r] >= array[piviot]:
                r -= 1
        swap(array, r, piviot)

        if r == k:
            return array[r]
        elif r < k:
            startIdx = r + 1
        else:
            endIdx = r - 1


def swap(array, l, r):
    array[l], array[r] = array[r], array[l]


array = [7, 10, 4, 3, 20, 15]
array = [7, 10, 4, 20, 15]
print(kSmallest(array, 3))
