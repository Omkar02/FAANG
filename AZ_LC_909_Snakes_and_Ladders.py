# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


def snakesAndLadders(board):
    n = len(board)
    visited = set()
    q = [(1, 0)]

    while q:
        lable, steps = q.pop(0)
        row, col = lable_to_position(lable, n)
        if board[row][col] != -1:
            lable = board[row][col]

        if lable == n * n:
            return steps
        for x in range(1, 7):
            newLable = lable + x
            if newLable <= n * n and newLable not in visited:
                visited.add(newLable)
                q.append((newLable, steps + 1))

    return -1


def lable_to_position(lable, n):
    r, c = divmod(lable - 1, n)
    print(r, c)
    if r % 2 == 0:
        return (n - 1 - r, c)
    return (n - 1 - r, n - 1 - c)


board = [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
# Output: 4

print(snakesAndLadders(board))
