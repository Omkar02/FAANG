# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def minCostTicket(days, costs):
    dayset = set(days)
    durations = [1, 7, 30]
    return dp(dayset, costs, durations, 1, {})


def dp(dayset, costs, durations, currDay, cache):
    cnt[0] += 1
    if currDay in cache:
        return cache[currDay]
    if currDay > 365:
        return 0
    elif currDay in dayset:
        cache[currDay] = min(dp(dayset, costs, durations, currDay + d, cache) + c for c, d in zip(costs, durations))
        return cache[currDay]
    else:
        cache[currDay] = dp(dayset, costs, durations, currDay + 1, cache)
        return cache[currDay]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(minCostTicket(days, costs))
print(cnt)
