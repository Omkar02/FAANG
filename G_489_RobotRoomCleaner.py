# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Hard')


class robo:
    def __init__(self, room):
        self.room = room
        self.visited = set()
        self.lenRow = len(self.room)
        self.lenCol = len(self.room[0])

    def move(self, start):
        self._moveHelper(start)

    def _moveHelper(self, node):
        if node[0] > self.lenRow:
            return
        if node[1] > self.lenCol:
            return
        if node in self.visited:
            return

        self.visited.add(node)
        self.room[node[0]][node[1]] = ''
        neighbour = self.getNeghibour(node)

        for place in neighbour:
            self._moveHelper(place)

    def getNeghibour(self, node):
        # print(node,end=' --> ')
        rowRange = range(self.lenRow)
        colRange = range(self.lenCol)
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        allNeighbour = []
        for point in direction:
            newRow, newCol = node[0] + point[0], node[1] + point[1]
            if newRow in rowRange and newCol in colRange and (newRow, newCol) not in self.visited and self.room[newRow][newCol] != 0:
                allNeighbour.append((newRow, newCol))

        return allNeighbour


room = [[1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1]]
start = (1, 3)
[print(x) for x in room]

r = robo(room)
r.move(start)
print()
[print(x) for x in r.room]
