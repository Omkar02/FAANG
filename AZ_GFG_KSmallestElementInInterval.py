# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def kSmallest(intervals, k):
    intervals = sorted(intervals, key=lambda a: a[0])
    merged = []
    for i in intervals:
        for j in range(i[0], i[1]):
            merged.append(j)

    merged.sort()
    print(merged)
    return merged[k - 1] if k - 1 < len(merged) else -1


intervals = [[5, 11], [10, 15], [12, 20]]
k = 12
print(kSmallest(intervals, k))
