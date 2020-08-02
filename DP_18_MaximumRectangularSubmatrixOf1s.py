import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxAreaOfRectangle(matrix):
    temp = [0 for i in matrix[0]]
    maxArea = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                temp[j] = 0
            else:
                temp[j] += matrix[i][j]
        print(temp)

        area = getMaxHistogramAlgo(temp)
        maxArea = max(maxArea, area)

    return maxArea


def getMaxHistogramAlgo(array):
    stack = []
    maxArea = 0
    idx = 0
    while idx < len(array):
        if not stack or array[stack[-1]] <= array[idx]:
            stack.append(idx)
            idx += 1
        else:
            topIdx = stack.pop()
            area = (array[topIdx] * ((idx - stack[-1] - 1)if len(stack) != 0 else idx))
            maxArea = max(maxArea, area)
    while stack:
        topIdx = stack.pop()
        area = array[topIdx] * ((idx - stack[-1] - 1)if stack else idx)
        maxArea = max(area, maxArea)
    return maxArea


matrix = [[1, 1, 1, 0],
          [1, 1, 1, 1],
          [0, 1, 1, 0],
          [0, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 1]]
print(maxAreaOfRectangle(matrix))
# print(getMaxHistogramAlgo([6, 2, 5, 4, 5, 1, 6]))
