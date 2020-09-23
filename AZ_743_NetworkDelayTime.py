# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')

import heapq


def networkDelayTime(times, N, K):
    graph = {}
    for u, v, w in times:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    pq = [(0, K)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        if node in graph:
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))

    return max(dist.values()) if len(dist) == N else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2


print(networkDelayTime(times, N, K))
