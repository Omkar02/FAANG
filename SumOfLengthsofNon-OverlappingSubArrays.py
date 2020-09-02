import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

'''
Given an array of N elements, you are required to find the maximum sum of lengths of all
non-overlapping subarrays with K as the maximum element in the subarray.
.
Input:
First line of the input contains an integer T, denoting the number of the total test cases.
Then T test case follows. First line of the test case contains an integer N,
denoting the number of elements in the array. Then next line contains N space separated
integers denoting the elements of the array. The last line of each test case contains an integer K.

Output:
For each test case ouptut a single line denoting the sum of the length of all such subarrays.
'''
arr = [3, 2, 2, 4, 3]


def SumOfLengts(array, k):
    kPosition = getAllKpos(array, k)
    totalLength = 0

    for position in kPosition:
        print(f'=={position}==')
        for rightIdx in range(position + 1, len(array)):
            if k >= array[rightIdx]:
                print(position, '--', k, array[rightIdx], 'R')
                totalLength += 1
            else:
                break

        for leftIdx in reversed(range(0, position + 1)):
            if k >= array[leftIdx]:
                print(position, '--', k, array[leftIdx], 'l')
                totalLength += 1
            else:

                break
    return totalLength


def getAllKpos(array, k):
    allKpos = []
    for i in range(len(array)):
        if array[i] == k:
            allKpos.append(i)
    return allKpos


array = [2, 1, 4, 9, 2, 3, 8, 3, 4]
# array = [4, 5, 7, 1, 2, 9, 8, 4, 3, 1]
array = [4, 3, 2, 6, 2, 3, 4]
array = [3, 2, 2, 4, 3]

k = 2

print(SumOfLengts(array, k))
