# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def meatingRoom(intervals):
    stack = []
    intervals.sort(key=lambda a: a[0])
    n = len(intervals)
    for i in intervals:
        if not stack:
            stack.append(i)
        elif stack[-1][1] > i[0]:
            stack.append(i)
        elif stack[-1][1] <= i[0]:
            stack.pop()
            stack.append(i)
        stack.sort(key=lambda a: a[0])
    return len(stack)


intervals = [(0, 30), (5, 10), (15, 20)]
print(meatingRoom(intervals))
