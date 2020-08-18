import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def search(matrix, target):
    row = 0
    coll = len(matrix[0]) - 1
    while row < len(matrix) and coll >= 0:
        if matrix[row][coll] > target:
            coll -= 1
        elif matrix[row][coll] < target:
            row += 1
        else:
            return ([row, coll], matrix[row][coll])

    return (None, None)


matrix = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]]

result = search(matrix, 51)

print(f'Index = {result[0]} for target {result[1]}')
