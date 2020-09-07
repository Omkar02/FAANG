# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Medium')


"""
Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
"""

cnt = [0]


def minKnightMoves(target):
    direction = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    seen = set()

    q = [(0, 0)]
    seen.add((0, 0))
    x, y = abs(target[0]), abs(target[1])

    steps = 0
    # bfs
    while q:
        for _ in range(len(q)):
            curr_x, curr_y = q.pop(0)
            # print(curr_x, curr_y)

            if curr_x == x and curr_y == y:
                return steps

            for d in direction:
                new_x, new_y = curr_x + d[0], curr_y + d[1]

                if (new_x, new_y) not in seen and -2 <= new_x <= x + 2 and -2 <= new_y <= y + 2:
                    cnt[0] += 1
                    seen.add((new_x, new_y))
                    q.append((new_x, new_y))

        steps += 1


target = (2, 1)
target = (5, 5)

print(minKnightMoves(target))
print(cnt)
