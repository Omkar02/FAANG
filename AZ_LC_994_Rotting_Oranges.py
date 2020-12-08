# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class oranges:
    def orangesRotting(self, grid):
        timer = 0
        fresh_queue = []
        rotten_queue = []
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x_bound = len(grid)
        y_bound = len(grid[0])
        for row in range(x_bound):
            for col in range(y_bound):
                if grid[row][col] == 1:
                    fresh_queue.append((row, col))
                if grid[row][col] == 2:
                    rotten_queue.append((row, col))
        if not fresh_queue:
            return 0
        while rotten_queue:
            if self.check(grid):
                return timer
            timer += 1
            nxt = []
            for x, y in rotten_queue:
                for off_x, off_y in neighbors:
                    new_x, new_y = x + off_x, y + off_y
                    if (new_x, new_y) in fresh_queue and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        nxt.append((new_x, new_y))
            rotten_queue = nxt
        return -1

    def check(self, grid):
        for row in grid:
            if 1 in row:
                return False
        return True


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid = [[0, 2]]
o = oranges()

print(o.orangesRotting(grid))
