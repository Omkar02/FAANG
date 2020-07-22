import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Hard')
'''
Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in 
an anti-clockwise direction without using any extra space.

Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. The first line of each 
test case consists of an integer N, where N is the size of the square matrix. The second 
line of each test case contains N x N space-separated values of the matrix.

Output:
Corresponding to each test case, in a new line, print the rotated array.

Your Task:
You only need to implement the given function rotate(). Do not read input, instead use the 
arguments given in the function. 

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
'''
'''
During first iteration –
a[i][j] = Element at first index (leftmost corner top)= 1.
a[j][n-1-i]= Rightmost corner top Element = 3.
a[n-1-i][n-1-j] = Righmost corner bottom element = 9.
a[n-1-j][i] = Leftmost corner bottom element = 7.

Move these elements in the clockwise direction.
During second iteration –
a[i][j] = 2.
a[j][n-1-j] = 6.
a[n-1-i][n-1-j] = 8.
a[n-1-j][i] = 4.
Similarly, move these elements in the clockwise direction.
'''


def rotateMatrix(matrix):
    N = len(matrix[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp
    [print(X) for X in matrix]
# def swap(matrix, i, j):
#     matrix[i][j] = matrix[j][i]


def myRotateMatrix(mat):
    n = len(mat[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[n - 1 - j][i]
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]
            mat[j][n - 1 - i] = temp
    [print(X) for X in mat]


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# rotateMatrix(arr)
myRotateMatrix(arr)
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
