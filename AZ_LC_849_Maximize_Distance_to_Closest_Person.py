# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def findTheColsest(seats):
    prev_seat = None
    dist = float('-inf')

    for indx in range(len(seats)):
        if seats[indx] == 1:
            if prev_seat == None:
                dist = indx
            else:
                dist = max(dist, (indx - prev_seat) // 2)
            prev_seat = indx

    dist = max(dist, len(seats) - 1 - prev_seat)
    return dist


seats = [1, 1, 1, 0, 0]
print(findTheColsest(seats))
