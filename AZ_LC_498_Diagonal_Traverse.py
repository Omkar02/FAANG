# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def diag_traverse(mat):
    if not mat:
        return
    rowLen, colLen = len(mat), len(mat[0])
    ans = []
    index_val = {}
    for r in range(rowLen):
        for c in range(colLen):
            curr_idx = r + c
            if curr_idx not in index_val:
                index_val[curr_idx] = []
            index_val[curr_idx].append(mat[r][c])

    for idx, data in enumerate(index_val.values()):
        if idx % 2 == 0:
            ans.extend(list(reversed(data)))
        else:
            ans.extend(data)
    return ans


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(diag_traverse(mat))
