import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxScore(cardPoints, k):
    start = curIdx = 0
    maxScore = float('-inf')
    ele = []
    cnt = 0
    n = len(cardPoints)
    while cnt < k + 1:
        print(curIdx, '====')
        currSum = 0
        theElement = []
        for i in range(start, start + k):
            curIdx = i
            # print('--->', i)
            theElement.append(cardPoints[i])
            currSum += cardPoints[i]
        print('\t', currSum, theElement)
        if currSum > maxScore:
            maxScore = currSum
            ele = theElement
        start -= 1

        cnt += 1
        if cnt == len(cardPoints):
            break
    return maxScore


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
cardPoints = [1, 1000, 1]
k = 1
cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
k = 3
cardPoints = [11, 49, 100, 20, 86, 29, 72]
k = 4
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))
