import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Binary-Search', Difficult='Medium')


'''
Given two sorted arrays of distinct elements. There is only 1 difference between the arrays.
First array has one element extra added in between. Find the index of the extra element.

Input:
The first line of input contains an integer T, denoting the no of test cases.
Then T test cases follow. The first line of each test case contains an integer N, denoting the number
of elements in array. The second line of each test case contains N space separated values of the array A[].
The Third line of each test case contains N-1 space separated values of the array B[].

Output:
Return the index (0 based indexing) of the corresponding extra element in array A[].(starting index 0).

'''


arrayOne = [2, 4, 6, 8, 9, 10, 12]
arrayTwo = [2, 4, 6, 8, 10, 12]

# arrayOne = [3, 5, 7, 9, 11, 13]
# arrayTwo = [3, 5, 7, 11, 13]


def extraElement(arrayOne, arrayTwo):
    # if len(arrayOne) == len(arrayTwo):
    #     return -1
    mid = len(arrayOne) // 2

    while mid > 0:
        if arrayOne[mid] != arrayTwo[mid]:
            return mid
        print(arrayOne[mid], arrayTwo[mid], 'L')
        mid = (mid) // 2

    mid = len(arrayOne) // 2

    while mid < len(arrayOne) - 1 and mid < len(arrayTwo) - 1:
        if arrayOne[mid] != arrayTwo[mid]:
            print(arrayOne[mid], arrayTwo[mid], 'R')
            return mid
        print(arrayOne[mid], arrayTwo[mid], 'R')
        mid = ((mid) + len(arrayOne) - 1) // 2
    return -1


print(extraElement(arrayOne, arrayTwo))
