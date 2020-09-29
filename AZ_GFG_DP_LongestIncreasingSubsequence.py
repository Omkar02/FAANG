# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')

cnt = [0]


def longestIncreasingSubseq(array):
    n = len(array)
    length = [0 for _ in range(n)]
    length[0] = 1
    seq = [None for _ in range(n)]
    maxlenIdx = 0
    for i in range(1, n):
        currNum = array[i]
        for j in range(0, i):
            otherNum = array[j]

            if otherNum < currNum and length[i] < length[j] + 1:
                length[i] = length[j] + 1
                seq[i] = j
        if length[maxlenIdx] < length[i]:
            maxlenIdx = i

    return length[maxlenIdx], buildSeq(array, seq, maxlenIdx)


def buildSeq(array, seq, maxlenIdx):
    current = maxlenIdx
    seqTOReturn = [array[current]]
    while current:
        current = seq[current]
        seqTOReturn.append(array[current])

    return list(reversed(seqTOReturn))


array = [10, 22, 9, 33, 21, 50, 41, 60]
array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longestIncreasingSubseq(array))
