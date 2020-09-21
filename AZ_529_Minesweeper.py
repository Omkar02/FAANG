import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def updateBoard(board, click):
    ## RC ##
    ## APPROACH : DFS ##

    def adjacent_mines(i, j):
        mines = 0
        for x, y in directions:
            if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "M":
                mines += 1
        return mines

    def dfs(i, j):
        # mark adjacent mine count at click position and return the board
        mines = adjacent_mines(i, j)
        if mines:
            board[i][j] = str(mines)
            return board

        # if no adjacent mines found then, do DFS
        board[i][j] = "B"

        for x, y in directions:
            if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] == "E":
                dfs(i + x, j + y)
        return board
# main ---------------------------------------------------------------------------
    if not board:
        return board
    M = len(board)
    N = len(board[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # if click directly has mine, mark it as X and return
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board

    # if board has 'E' then check neighbors
    if board[click[0]][click[1]] == "E":
        return dfs(click[0], click[1])


board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
Click = [3, 0]

[print(x) for x in updateBoard(board, Click)]
