# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]


# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def merge(intervals):
    n = len(intervals) - 1
    ans = []
    for idx, i in enumerate(sorted(intervals)):
        if idx == 0:
            prev = i

        if prev[1] >= i[0]:
            if prev[1] < i[1]:
                prev[1] = i[1]
            if idx == n:
                ans.append(prev)

        else:
            ans.append(prev)
            prev = i
            if idx == n:
                ans.append(i)

    return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 3]]
# Output: [[1,6],[8,10],[15,18]]
# intervals = [[1, 4], [0, 4]]
print(merge(intervals))
