import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


'''
Given a time represented in the format "HH:MM", form the next closest
time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are
all valid. "1:34", "12:9" are all invalid.
'''


def nextColsestTime(time):

    totalMin = list(map(int, time.split(':')))

    totalMin = sum([totalMin[0] * 60, totalMin[1]])
    print(f'totalMin = {totalMin}')
    time = time.replace(':', '')
    allDigits = {int(x): True for x in time}
    print(f'allDigits = {allDigits}')
    cnt = 0
    while True:
        totalMin = (totalMin + 1) % (24 * 60)
        print(totalMin)

        theDigits = list(map(int, [totalMin / 60 / 10,
                                   totalMin / 60 % 10,
                                   totalMin % 60 / 10,
                                   totalMin % 60 % 10]))
        isClosest = True
        for i in theDigits:
            if i not in allDigits:
                isClosest = False

            print(theDigits)

        if isClosest:
            return f'{int(totalMin/60)}:{int(totalMin%60)}'
        cnt += 1
        if cnt == 100:
            print('ne')
            break


time = '19:34'
print(nextColsestTime(time))
