# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def setMatrix(matrix):
    zeroRows = set()
    zeroCols = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if not matrix[r][c]:
                zeroRows.add(r)
                zeroCols.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in zeroRows or c in zeroCols:
                matrix[r][c] = 0


matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
setMatrix(matrix)
print(matrix)
