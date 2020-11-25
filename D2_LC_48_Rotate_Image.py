# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def rotateImage(image):
    n = len(image[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            for k in range(4):
                tmp[k] = image[row][col]
                row, col = col, n - 1 - row
            for k in range(4):
                image[row][col] = tmp[k - 1]
                row, col = col, n - 1 - row


def rotateImage(image):
    n = len(image[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            r, c = i, j
            for k in range(4):
                tmp[k] = image[r][c]
                r, c = c, n - 1 - r
            for k in range(4):
                image[r][c] = tmp[k - 1]
                r, c = c, n - 1 - r


image = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Output = [[15, 13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7, 10, 11]]
rotateImage(image)
print(image == Output)
