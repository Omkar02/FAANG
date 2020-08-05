import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

CNT = [0]


def treeTopology(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(0, i):
            CNT[0] += 1
            catlangNumber = i - j - 1
            dp[i] += dp[j] * dp[catlangNumber]
    print(dp)
    return dp[-1]


n = 10
print(treeTopology(n))
print(f'cnt = {CNT}')
CNTC = [0]


def treeTopologyCache(n, cache):

    if n in cache:
        return cache[n]
    total = 0
    for i in range(n):
        CNTC[0] += 1
        j = n - i - 1
        itotal = treeTopologyCache(i, cache)
        jtotal = treeTopologyCache(j, cache)

        total += itotal * jtotal

    cache[n] = total
    return total


print(treeTopologyCache(n, {0: 1}))
print(f'cntc = {CNTC}')
