import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

# Consider a row of n coins of values v1 . . . vn, where n is even. We play a game
# against an opponent by alternating turns. In each turn, a player selects either the
# first or last coin from the row, removes it from the row permanently, and receives the
# value of the coin. Determine the maximum possible amount of money we can definitely win
# if we move first.

# Note: The opponent is as clever as the user.

# Let us understand the problem with few examples:

# 5, 3, 7, 10: The user collects maximum value as 15(10 + 5)
# 8, 15, 3, 7: The user collects maximum value as 22(7 + 15)
# Does choosing the best at each move gives an optimal solution? No.
# In the second example, this is how the game can be finished:

# …….User chooses 8.
# …….Opponent chooses 15.
# …….User chooses 7.
# …….Opponent chooses 3.
# Total value collected by user is 15(8 + 7)
# …….User chooses 7.
# …….Opponent chooses 8.
# …….User chooses 15.
# …….Opponent chooses 3.
# Total value collected by user is 22(7 + 15)


def optimalSolution(array):
    moves = [[0 for x in range(len(array))] for y in range(len(array))]
    movesT = [[[x, y] for x in range(len(array))] for y in range(len(array))]
    for gap in range(len(array)):
        for j in range(gap, len(array)):

            i = j - gap
            print('i', 'j', 'gap')
            print(i, j, gap)

            x = 0
            if (i + 2) <= j:
                print('x')
                x = moves[i + 2][j]

            y = 0
            if (i + 1) <= (j - 1):
                y = moves[i + 1][j - 1]
                print('y', y, [i, j], [i + 1, j - 1],'------------')
            z = 0
            if i <= (j - 2):
                print('z')
                z = moves[i][j - 2]

            moves[i][j] = max(array[i] + min(x, y), array[j] + min(y, z))
        [print(x) for x in moves]
        print()

    return moves[0][len(array) - 1]


array = [8, 15, 3, 7]
# array = [3, 9, 1, 2]
print(optimalSolution(array))
