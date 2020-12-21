# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

cnt = [0]


def calShortestPath(triangle, row, col, cache):
    cnt[0] += 1
    curr = (row, col)
    if curr in cache:
        return cache[curr]
    if row == len(triangle):
        return 0

    cache[curr] = triangle[row][col] + min(calShortestPath(triangle, row + 1, col, cache),
                                           calShortestPath(triangle, row + 1, col + 1, cache))
    return cache[curr]


triangle = [[2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]]


print(calShortestPath(triangle, 0, 0, {}))
print(cnt)
