# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def mergeInterval(intervals):
    intervals.sort(key=lambda a: a[0])
    ans = []
    for i in intervals:
        if not ans:
            ans.append(i)

        if ans[-1][1] >= i[0]:
            ans[-1] = [ans[-1][0], i[1]] if ans[-1][1] < i[1] else ans[-1]

        else:
            ans.append(i)
    return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 4], [2, 3]]
intervals = [[2, 3], [9, 11], [1, 5], [14, 18]]
# Output :[[1,4]]

intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]

print(mergeInterval(intervals))
