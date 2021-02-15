# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Hard')

import sortedcontainers


def getSkyline(buildings):
    # buildings[i] = [lefti, righti, heighti]

    events = [[x, b[2], enter] for b in buildings for x, enter in zip(b[:2], [1, -1])]
    # events[i] = [[lefti, heighti], [righti, heighti],......]

    events.sort(key=lambda x: (x[0], -x[1] * x[2]))
    ans = []
    heights = sortedcontainers.SortedList()

    for i, eve in enumerate(events):
        start_x, height_h, status = eve[0], eve[1], eve[2]

        if status == 1:
            if not heights or height_h > heights[-1]:
                ans.append([start_x, height_h])
            heights.add(height_h)
        else:
            heights.discard(height_h)
            if not heights:
                ans.append([start_x, 0])
            elif height_h > heights[-1]:
                ans.append([start_x, heights[-1]])
    return ans


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(getSkyline(buildings))
