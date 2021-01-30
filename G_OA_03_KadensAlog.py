# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# def kadensAlgo(array):
#     maxSoFar = float('-inf')
#     maxEndingHere = 0

#     startIdx, endIdx = 0, 0
#     s = 0
#     for i in range(0, len(array)):
#         maxEndingHere += array[i]

#         if maxEndingHere > maxSoFar:
#             maxSoFar = maxEndingHere
#             startIdx = s
#             endIdx = i

#         if maxEndingHere < 0:
#             s = i + 1
#             maxEndingHere = 0

#     return array[startIdx:endIdx + 1], maxSoFar


array = [-2, -3, 4, -1, -2, 1, 5, -3]
# array = [-2, 1]
# print(kadensAlgo(array))


def kadensAlgo(array):
    maxSoFar = float('-inf')
    maxEndingHere = 0
    startIdx, endIdx = 0, 0
    tempIdx = 0

    for i in range(len(array)):
        maxEndingHere += array[i]
        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            startIdx = tempIdx
            endIdx = i

        if maxEndingHere < 0:
            tempIdx = i + 1
            maxEndingHere = 0

    return array[startIdx:endIdx + 1], maxSoFar


print(kadensAlgo(array))
