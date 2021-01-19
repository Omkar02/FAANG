# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


"Weighted Job Scheduling "


def WJS(jobs, profits):
    jobs.sort(key=lambda a: a[1])
    n = len(jobs)
    dp = [p for p in profits]
    seq = [None for _ in jobs]
    maxPos = 0
    maxVal = float('-inf')
    for i in range(1, n):
        for j in range(0, i):
            cnt[0] += 1
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
# print(WJS(jobs, profits))
# print(cnt)

"Word Break Problem"


def WBP(string, dictionary, out, res):
    cnt[0] += 1
    if not string:
        res.append(out)

    for i in range(1, len(string) + 1):
        prefix = string[:i]
        if prefix in dictionary:
            WBP(string[i:], dictionary, f'{prefix} {out}', res)
    return res


dictionary = ["self", "th", "is", "famous", "Word",
              "break", "b", "r", "e", "a", "k", "br",
              "bre", "brea", "ak", "problem"]

string = "Wordbreakproblem"
# print(WBP(string, dictionary, "", []))
# print(cnt)


"Stock Buy Sell to Maximize Profit"


def MP(price):
    n = len(price)
    if n == 1:
        return
    i = 0
    while i < (n - 1):
        cnt[0] += 1
        while i < (n - 1) and price[i + 1] <= price[i]:
            cnt[0] += 1

            i += 1
        if i == n - 1:
            break

        buy = i
        i += 1
        while i < n and price[i] >= price[i - 1]:
            cnt[0] += 1
            i += 1
        sell = i - 1

        print("Buy on day: ", buy, "\t", "Sell on day: ", sell)


price = [5, 11, 3, 50, 60, 90]
# MP(price)
# print(cnt)
"Buy-Sell Stock With K transactions To Maximize Profit"


def MPWKT(price, k):
    n = len(price)
    dp = [[0 for i in range(n)] for x in range(k + 1)]
    for t in range(1, k + 1):
        maxThusFar = float('-inf')
        for d in range(1, n):
            maxThusFar = max(maxThusFar, dp[t - 1][d - 1] - price[d - 1])
            dp[t][d] = max(dp[t][d - 1], maxThusFar + price[d])
    return dp[-1][-1]


price = [5, 11, 3, 50, 60, 90]
k = 2
# print(MPWKT(price, k))
