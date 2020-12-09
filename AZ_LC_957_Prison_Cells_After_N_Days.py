# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
    -- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    -- Otherwise, it becomes vacant.
'''


def prisonCell(cells, N):

    id_cells, cells_id = {}, {}
    prev = cells[:]
    loop = None
    for k in range(N):
        for i in range(1, len(cells) - 1):
            cells[i] = 1 if prev[i - 1] == prev[i + 1] else 0
        cells[0] = cells[-1] = 0
        if tuple(cells) in cells_id:
            loop = k - cells_id[tuple(cells)]
            break
        id_cells[k] = cells[:]
        cells_id[tuple(cells)] = k
        prev = cells[:]
    return id_cells[(N - k - 1) % loop]if loop else cells


cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 20

print(prisonCell(cells, N))
