# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def jobScheduling(jobs, profits):
    jobs.sort(key=lambda a: a[1])
    n = len(jobs)
    dp = [p for p in profits]
    seq = [None for _ in jobs]

    maxPos = 0
    maxVal = 0

    for i in range(1, n):
        for j in range(0, i):
            if jobs[j][1] <= jobs[i][0]:
                if dp[j] + profits[i] > dp[i]:
                    dp[i] = dp[j] + profits[i]
                    seq[i] = j
                    if dp[i] > maxVal:
                        maxVal = dp[i]
                        maxPos = i
    return dp[maxPos], buildSeq(seq, jobs, maxPos)


def buildSeq(seq, jobs, maxPos):
    s = []
    while maxPos:
        s.append(jobs[maxPos])
        maxPos = seq[maxPos]
    return s


jobs = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
profits = [5, 6, 5, 4, 11, 2]
print(jobScheduling(jobs, profits))
