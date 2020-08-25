# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

def relativeSortArray(arr1, arr2):
    rPos = {}

    for i in arr2:
        rPos[i] = []
    for j in arr1:
        if j in rPos:
            rPos[j].append(j)

    newPos = 0
    res = []
    for numb in arr2:
        if len(rPos[numb]) != 0:
            res += rPos[numb]
            rPos[numb] = []

    res += sorted([val for val in arr1 if val not in arr2])
    # newPos += 1

    return res


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]


print(relativeSortArray(arr1, arr2))
print([2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])
