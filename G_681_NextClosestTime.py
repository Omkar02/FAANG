# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def nextClosestTime(timeS):
    converted = list(map(int, timeS.split(':')))
    minutes = converted[0] * 60 + converted[1]
    check = set(list(map(int, [i for i in timeS if i != ':'])))

    while True:
        minutes = (minutes + 1) % (24 * 60)
        newTime = list(map(int, [minutes / 60 / 10, minutes / 60 % 10, minutes % 60 / 10, minutes % 60 % 10]))

        if isValid(newTime, check):
            return f'{int(minutes/60 ):02}:{int(minutes%60):02}'


def isValid(newTime, check):
    for i in newTime:
        if i not in check:
            return False
    return True


timeS = "19:34"
timeS = "23:59"
timeS = "01:23"
print(nextClosestTime(timeS))
