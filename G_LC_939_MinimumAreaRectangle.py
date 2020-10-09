# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def minAreaRect(points):
    ref = set(map(tuple, points))
    minArea = float('inf')
    curArea = 0
    for i, p2 in enumerate(points):
        for j in range(i):
            p1 = points[j]

            if (p1[0] != p2[0] and p1[1] != p2[1]) and (p1[0], p2[1]) in ref and (p2[0], p1[1]) in ref:
                curArea = abs(p2[0] - p1[0]) * abs(p2[1] - p1[1])
                minArea = min(minArea, curArea)
    return minArea if minArea != float('inf') else 0


points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
points = [[0, 1], [1, 3], [3, 3], [4, 4], [1, 4], [2, 3], [1, 0], [3, 4]]

print(minAreaRect(points))


def minAreaRect(points):
    S = set(map(tuple, points))
    ans = float('inf')
    for j, p2 in enumerate(points):
        for i in range(j):
            p1 = points[i]
            if (p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
    return ans if ans < float('inf') else 0


print(minAreaRect(points))
