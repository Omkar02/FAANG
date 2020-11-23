# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def mergeIntervals(intervals):
    intervals.sort(key=lambda a: a[0])
    merged = []
    maxInterval = float('-inf')
    start = float('-inf')
    for i in range(len(intervals)):
        curr = intervals[i]
        if curr[0] > maxInterval:
            if i != 0:
                print(1)
                merged.append([start, maxInterval])
            maxInterval = curr[1]
            start = curr[0]
        else:
            if curr[1] >= maxInterval:
                maxInterval = curr[1]
    if maxInterval != float('-inf') and [start, maxInterval] not in merged:
        merged.append([start, maxInterval])
    return merged


intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
print(mergeIntervals(intervals))
