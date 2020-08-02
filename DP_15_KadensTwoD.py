import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxSubRectangleMatrix(matrix):
    maxSum = 0
    boundRight = 0
    boundLeft = 0
    boundUp = 0
    boundDown = 0

    row = len(matrix)
    coll = len(matrix[0])
    temp = [0] * row

    for left in range(coll):
        for i in range(row):
            temp[i] = 0

        for right in range(left, coll):
            for i in range(row):
                temp[i] += matrix[i][right]

            kadensResult = kadensAlgo(temp)
            if kadensResult[0] > maxSum:
                maxSum = kadensResult[0]
                boundLeft = left
                boundRight = right
                boundUp = kadensResult[1]
                boundDown = kadensResult[2]

    return f'maxSum = {maxSum} boundRight = {boundRight} boundLeft = {boundLeft} boundUp = {boundUp} boundDown = {boundDown}'


def kadensAlgo(array):
    theMax = 0
    maxEndingHere = 0
    maxSumSoFar = 0
    maxStart = -1
    maxEnd = -1
    currStart = 0

    for cnt, num in enumerate(array):
        maxSumSoFar += num
        if maxSumSoFar < 0:
            maxSumSoFar = 0
            currStart = cnt + 1
        if theMax < maxSumSoFar:
            maxStart = currStart
            maxEnd = cnt

            theMax = maxSumSoFar
    return (theMax, maxStart, maxEnd)


# print(kadensAlgo([2, 0, 2, -3]))
matrix = [[2, 1, -3, -4, 5],
          [0, 6, 3, 4, 1],
          [2, -2, -1, 4, -5],
          [-3, 3, 1, 0, 3]]


print(maxSubRectangleMatrix(matrix))
