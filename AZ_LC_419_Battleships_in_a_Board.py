# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


def countBattelShip(sea):
    count = 0
    rowLen = len(sea)
    colLen = len(sea[0])

    for r in range(rowLen):
        for c in range(colLen):
            if sea[r][c] == '.':
                continue

            if r > 0 and sea[r - 1][c] == 'X':
                continue
            if c > 0 and sea[r][c - 1] == 'X':
                continue
            count += 1

    return count


sea = [['X', '.', '.', 'X'],
       ['.', '.', '.', 'X'],
       ['.', '.', '.', 'X']]
print(countBattelShip(sea))
