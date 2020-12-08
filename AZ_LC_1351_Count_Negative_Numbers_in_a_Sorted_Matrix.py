# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def countNegative(grid):
    res, i = 0, len(grid[0]) - 1
    for rowNum, row in enumerate(grid):
        while row[i] < 0 and i >= 0:
            res += len(grid) - rowNum
            i -= 1
    return res


grid = [[4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]]
print(countNegative(grid))
