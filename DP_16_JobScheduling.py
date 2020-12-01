# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxProfitjobScheduling(jobList):
    dp = [jobList[i][2] for i in range(len(jobList))]
    pos = [None for i in range(len(jobList))]

    maxPos = 0
    maxVal = 0

    jobList.sort(key=lambda x: x[1])
    dp[0] = jobList[0][2]

    n = len(jobList)
    for i in range(1, n):
        for j in range(0, i):
            if isOverlaped(jobList, i, j):
                if dp[i] < dp[j] + jobList[i][2]:
                    dp[i] = jobList[i][2] + dp[j]
                    pos[i] = j
                    if dp[i] > maxVal:
                        maxVal = dp[i]
                        maxPos = i

    return dp[maxPos], buildSeq(maxPos, pos, jobList)


def buildSeq(maxPos, pos, jobList):
    seq = []
    while maxPos:
        seq.append(jobList[maxPos])
        maxPos = pos[maxPos]
    return seq


def isOverlaped(jobList, i, j):
    return jobList[j][1] <= jobList[i][0]


jobList = [[1, 3, 5],
           [2, 5, 6],
           [4, 6, 5],
           [6, 7, 4],
           [5, 8, 11],
           [7, 9, 2]]

jobList = [[1, 2, 100],
           [2, 1, 10],
           [3, 2, 15],
           [4, 1, 27]]

print(maxProfitjobScheduling(jobList))
