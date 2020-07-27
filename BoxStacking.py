import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def boxStack(array):
    array.sort(key=lambda x: x[2])

    heights = [x[2] for x in array]
    seq = [None for x in array]
    maxheight = 0

    for i in range(1, len(array)):
        currBox = array[i]
        for j in range(0, i):
            newBox = array[j]
            if isValidated(newBox, currBox):
                newHeight = currBox[2] + heights[j]
                if newHeight > heights[i]:
                    heights[i] = newHeight
                    seq[i] = j

        if heights[i] >= heights[maxheight]:
            maxheight = i

    return heights[maxheight], buildSeq(seq, maxheight, array)


def buildSeq(seq, idx, array):
    sequence = []
    while idx is not None:
        sequence.append(array[idx])
        idx = seq[idx]
    return sequence


def isValidated(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

    # (length, width, height)
array = [[12, 32, 10], [10, 12, 32], [6, 7, 4], [5, 6, 4], [4, 5, 6], [2, 3, 1], [1, 2, 3]]

print(boxStack(array))
