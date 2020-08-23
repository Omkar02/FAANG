# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all 
the values in B are the same.

If it cannot be done, return -1.
'''

A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
A = [3, 5, 1, 2, 3]
B = [3, 6, 3, 3, 4]


def dominoRotation(A, B):
    for val in range(1, 7):
        if all(val in domino for domino in zip(A, B)):
            return len(A) - max(A.count(val), B.count(val))
    return -1


print(f'Min Rotation = {dominoRotation(A,B)}')

