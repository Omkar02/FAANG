import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sliding-Window', Difficult='Medium')


def maxSumNonOverlapping(array, k, m):

    kMaxVal = float('-inf')
    kcurrMax = 0
    startK = 0
    for i in range(len(array)):
        kcurrMax = sum(array[i:i + k])
        # print(kcurrMax)
        if kcurrMax > kMaxVal:
            startK = i
            kMaxVal = kcurrMax

    mMaxVal = float('-inf')
    mCurrMax = 0
    startM = 0
    for i in range(len(array)):
        if i in [x for x in range(startK, startK + k)] or i + m in [x for x in range(startK, startK + k)]:
            # print([x for x in range(startK, startK + k)], '===')
            continue
        mCurrMax = sum(array[i:i + m]) if len(array[i:i + m]) == m else float('-inf')
        if mCurrMax > mMaxVal:
            mMaxVal = mCurrMax
            startM = i

    return f'MaxVal = {kMaxVal + mMaxVal} Sub-Array =  {array[startK:startK + k], array[startM:startM + m]}'


array = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L = 1
M = 2
array = [3, 8, 1, 3, 2, 1, 8, 9, 0]
L = 3
M = 2
array = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
L = 4
M = 3

print(maxSumNonOverlapping(array, L, M))
