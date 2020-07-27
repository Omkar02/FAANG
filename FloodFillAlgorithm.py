import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Graph', Difficult='Hard')

'''
Input:
       screen[M][N] = [{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };
    x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that
should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

'''


screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]


def floadFill(screen, coord, newColor):
  rStart, cStart = coord

  q = []
  q.append([rStart, cStart])
  preVal = screen[rStart][cStart]
  while q:
    cd = q.pop()
    screen[cd[0]][cd[1]] = newColor
    allAdj = getAllAdj(screen, cd, preVal)  # [r,c]

    for adj in allAdj:
      q.append(adj)

  [print(x) for x in screen]


def getAllAdj(screen, coord, preVal):
  allAdj = []
  rStart, cStart = coord

  if rStart < len(screen[0]) - 1 and screen[rStart + 1][cStart] == preVal:
    allAdj.append([rStart + 1, cStart])

  if rStart > 0 and screen[rStart - 1][cStart] == preVal:
    allAdj.append([rStart - 1, cStart])

  if cStart < len(screen) - 1 and screen[rStart][cStart + 1] == preVal:
    allAdj.append([rStart, cStart + 1])

  if cStart > 0 and screen[rStart][cStart - 1] == preVal:
    allAdj.append([rStart, cStart - 1])

  # print('   ', allAdj, coord)
  return allAdj


cod = (4, 5)
newColor = 3
floadFill(screen, cod, newColor)
# getAllAdj(screen, (4, 4), 2)
