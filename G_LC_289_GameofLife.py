# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


""" Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction."""

import time


class life:
    def __init__(self, board):
        self.board = board
        self.visited = set()
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])

    def gameOfLife(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                self.check(r, c)
        self.finalBoard()
        return self.board

    def check(self, r, c):
        rowRange = range(0, self.rowLen)
        colRange = range(0, self.colLen)
        direction = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        aliveFour = 0
        for p1, p2 in direction:
            newR, newC = r + p1, c + p2
            if newR in rowRange and newC in colRange and abs(self.board[newR][newC]) == 1:
                aliveFour += 1

        # Rule 1 or Rule 3
        if self.board[r][c] == 1 and (aliveFour < 2 or aliveFour > 3):
            self.board[r][c] = -1
        # Rule 4
        if self.board[r][c] == 0 and aliveFour == 3:
            self.board[r][c] = 2

    def finalBoard(self):
        for r in range(self.rowLen):
            for c in range(self.colLen):
                if self.board[r][c] > 0:
                    self.board[r][c] = 1
                else:
                    self.board[r][c] = 0


board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]


Output = [[0, 0, 0],
          [1, 0, 1],
          [0, 1, 1],
          [0, 1, 0]]
l = life(board)
firstUpdate = l.gameOfLife()
print(firstUpdate)
print(firstUpdate == Output)
