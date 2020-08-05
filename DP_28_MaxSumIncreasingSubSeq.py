import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxIncreaseingSunSeq(array):
    dp = [i for i in array]
    pos = [None for i in array]
    maxPos = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i]:
                newSum = array[i] + dp[j]
                if newSum > dp[i]:
                    dp[i] = newSum
                    pos[i] = j
                else:
                    dp[i] = dp[i]

        if dp[i] > dp[maxPos]:
            maxPos = i
    # print(dp)
    # print(pos)
    return dp[maxPos], buildSeq(maxPos, pos, array)


def buildSeq(maxPos, pos, array):
    seq = [array[maxPos]]
    cnt = 0
    while maxPos:
        maxPos = pos[maxPos]
        seq.append(array[maxPos])
        if cnt == 30:
            print('nee!')
            break
        cnt += 1
    return list(reversed(seq))


array = [4, 6, 1, 3, 8, 4, 6]
print(maxIncreaseingSunSeq(array))
