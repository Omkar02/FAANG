import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
Monu lives in a society which is having high rise buildings. This is the time of sunrise 
and monu wants see the buildings receiving the sunlight. Help him in counting the number of buildings recieving the sunlight.
Given an array H representing heights of buildings. You have to count the buildings which 
will see the sunrise (Assume : Sun rise on the side of array starting point).

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test 
case is N, N is the number of buildings. The second line of each test case contains N input H[i], height of ith building.

Output:
print the total number of buildings which will see the sunset.
'''

array = [7, 4, 8, 2, 9]
array = [2, 3, 4, 5]


def faceTheSun(array):
    buildingsCount = 0
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            buildingsCount += 1
    return buildingsCount + 1


print(faceTheSun(array))
