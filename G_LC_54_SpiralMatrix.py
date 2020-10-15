# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Matrix', Difficult='Medium')


def spiralOrder(mat):
    sR, eR = 0, len(mat) - 1
    sC, eC = 0, len(mat[0]) - 1
    answer = []
    while sR <= eR and sC <= eC:

        for col in range(sC, eC + 1):
            answer.append(mat[sR][col])

        for row in range(sR + 1, eR + 1):
            answer.append(mat[row][eC])

        for col in reversed(range(sC, eC)):
            answer.append(mat[eR][col])

        for row in reversed(range(sR + 1, eR)):
            answer.append(mat[row][sC])

        sR += 1
        eR -= 1
        sC += 1
        eC -= 1
    return answer


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(spiralOrder(mat))
