# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


class gboard:
    def __init__(self, board):
        self.board = board
        self.visited = set()
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])
        self.path = [[' ' for _ in range(self.rowLen)] for _ in range(self.colLen)]
        self.ans = None

    def findPath(self, start, destination):
        self.DFS(start, destination, [])

    def DFS(self, node, destination, path):
        if node in self.visited:
            return
        if node == destination:

            self.ans = path

        self.visited.add(node)
        neighbour = self.getNeighbour(node)
        for pathWay in neighbour:
            self.path[pathWay[0]][pathWay[1]] = '/'
            path.append(node)
            self.DFS(pathWay, destination, path)

    def getNeighbour(self, node):
        rowRange = range(self.rowLen)
        colRange = range(self.colLen)
        neighbour = []
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dRow, dCol in direction:
            newR, newC = node[0] + dRow, node[1] + dCol
            if newR in rowRange and newC in colRange and self.board[newR][newC] != 1:
                neighbour.append((newR, newC))

        return neighbour


board = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]


start = (0, 4)
destination = (4, 4)
g = gboard(board)
g.findPath(start, destination)
# print(g.ans)
[print(x) for x in g.path]
