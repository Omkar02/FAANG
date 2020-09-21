# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def gameOfLife(board):
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            for dr, dc in neighbors:
                currRow, currCol = r + dr, c + dc
                if currRow < rows and currRow >= 0 and currCol < cols and currCol >= 0 and abs(board[currRow][currCol]) == 1:
                    live_neighbors += 1

            # rule no. 1 or 3
            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[r][c] = -1

            if board[r][c] == 0 and live_neighbors == 3:
                board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0

    [print(x) for x in board]
    return board


board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]

out = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]
print(gameOfLife(board) == out)
