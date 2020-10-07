# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Graphs', Difficult='Medium')


"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall 
since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.
Example:
For the given grid
0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""


class BombEnemy:
    def __init__(self, area):
        self.area = area
        self.rowLen = len(self.area)
        self.colLen = len(self.area[0])
        self.maxEnemy = float('-inf')

    def getDeathCount(self):

        for r in range(self.rowLen):
            for c in range(self.colLen):
                currEnemy = 0
                if self.area[r][c] == '0':
                    for newRow in range(0, self.rowLen):
                        if self.area[newRow][c] == 'W':
                            break
                        if self.area[newRow][c] == 'E':
                            currEnemy += 1

                    for newCol in range(0, self.colLen):
                        if self.area[r][newCol] == 'W':
                            break
                        if self.area[r][newCol] == 'E':
                            currEnemy += 1
                self.maxEnemy = max(self.maxEnemy, currEnemy)


area = [['0', 'E', '0', '0'],
        ['E', '0', 'W', 'E'],
        ['0', 'E', '0', '0']]

b = BombEnemy(area)
b.getDeathCount()
print(b.maxEnemy)
