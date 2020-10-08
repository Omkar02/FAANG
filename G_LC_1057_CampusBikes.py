# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# pigion-HoleSort
"""
Input:
workers = [[0,0],[1,1],[2,0]],
bikes = [[1,0],[2,2],[2,1]]
Output:
[0,2,1]
Explanation:

Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus
Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].
"""

import heapq


# def assignBike(workers, bikes):
#     distance = []  # storing a tuple (distance,workerNO,bikeNo)
#     for workerIdx, (xW, yW) in enumerate(workers):
#         distance.append([])
#         for bikeIdx, (xB, yB) in enumerate(bikes):
#             calDistance = abs(xW - xB) + abs(yW - yB)
#             distance[-1].append((calDistance, workerIdx, bikeIdx))

#         distance[-1].sort(reverse=True)
#     print(distance)
#     assignedTo = [None for _ in range(len(workers))]
#     assignedBikes = set()

#     queue = [distance[i].pop() for i in range(len(workers))]
#     heapq.heapify(queue)
#     while len(assignedBikes) < len(workers):
#         _, workerIdx, bikeIdx = heapq.heappop(queue)
#         if bikeIdx not in assignedBikes:
#             assignedTo[workerIdx] = bikeIdx
#             assignedBikes.add(bikeIdx)

#         else:
#             heapq.heappush(queue, distance[workerIdx].pop())

#     return assignedTo


def assignedBikes(workers, bikes):
    distance = []
    for workerIdx, (wX, wY) in enumerate(workers):
        distance.append([])
        for bikeIdx, (bX, bY) in enumerate(bikes):
            distanceBetween = abs(wX - bX) + abs(wY - bY)
            distance[-1].append((distanceBetween, workerIdx, bikeIdx))
        distance[-1].sort(reverse=True)

    queue = [distance[i].pop() for i in range(len(workers))]
    heapq.heapify(queue)
    assignedTo = [None for _ in range(len(workers))]
    bikesUsed = set()

    while len(bikesUsed) < len(workers):
        _, workerIdx, bikeIdx = heapq.heappop(queue)
        if bikeIdx not in assignedTo:
            assignedTo[workerIdx] = bikeIdx
            bikesUsed.add(bikeIdx)
        else:
            heapq.heappush(queue, distance[workerIdx].pop())
    return assignedTo


workers = [[0, 0], [1, 1], [2, 0]]
bikes = [[1, 0], [2, 2], [2, 1]]
print(assignedBikes(workers, bikes))
