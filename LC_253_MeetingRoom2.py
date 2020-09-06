# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Heap', Difficult='Medium')

import heapq


def meetingRoomReq(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []
    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            # room is already used in last meeting and continue to use the same room for this meeting
            heapq.heapreplace(heap, interval[1])

        else:
            heapq.heappush(heap, interval[1])
    print(heap)
    return len(heap)


intervals = [[0, 30], [5, 10], [15, 20]]
print(meetingRoomReq(intervals))
