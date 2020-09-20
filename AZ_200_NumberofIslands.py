# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def numIslands(grid):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    visited = set()
    island = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c)not in visited:
                island += 1
                depthFirstSearch(grid, visited, rows, cols, r, c)

    return island


def depthFirstSearch(grid, visited, rows, cols, r, c):
    if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == '0':
        return
    visited.add((r, c))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in directions:
        depthFirstSearch(grid, visited, rows, cols, r + dr, c + dc)


grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

# grid = [["1", "1", "0", "0", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "0", "1", "0", "0"],
#         ["0", "0", "0", "1", "1"]]

print(numIslands(grid))
