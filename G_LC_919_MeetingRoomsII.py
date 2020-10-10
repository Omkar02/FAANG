# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

import heapq


def meetingRoomTwo(intervals):
    intervals.sort(key=lambda x: x[0])
    minheap = []
    for meetHours in intervals:
        # room is already used in last meeting and continue to use the same room for this meeting
        if minheap and meetHours[0] > minheap[0]:
            heapq.heappop(minheap)
            heapq.heappush(minheap, meetHours[-1])
        else:
            heapq.heappush(minheap, meetHours[-1])

    return len(minheap)


intervals = [(0, 30), (5, 10), (15, 20)]
# intervals = [[7, 10], [2, 4]]
print(meetingRoomTwo(intervals))
