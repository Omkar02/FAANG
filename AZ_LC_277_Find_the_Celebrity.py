# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findCelebrity(guestList):
    a, b = 0, len(guestList) - 1
    while a < b:
        if guestList[a][b]:
            a += 1
        else:
            b -= 1

    for i in range(len(guestList)):
        if i != a and (guestList[a][i] or not guestList[i][a]):
            return -1
    return a


guestList = [[0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 0]]
print(findCelebrity(guestList))
