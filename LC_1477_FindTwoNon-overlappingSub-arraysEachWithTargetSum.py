# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def SumOfLengts(array, k):
    kPosition = getAllKpos(array, k)
    totalLength = 0

    for position in kPosition:
        print(f'=={position}==')
        for rightIdx in range(position + 1, len(array)):
            if k >= array[rightIdx]:
                print(position, '--', k, array[rightIdx], 'R')
                totalLength += 1
            else:
                break

        for leftIdx in reversed(range(0, position + 1)):
            if k >= array[leftIdx]:
                print(position, '--', k, array[leftIdx], 'l')
                totalLength += 1
            else:

                break
    return totalLength


def getAllKpos(array, k):
    allKpos = []
    for i in range(len(array)):
        if array[i] == k:
            allKpos.append(i)
    return allKpos


arr = [2, 1, 4, 9, 2, 3, 8, 3, 4]
target = 7
print(SumOfLengts(arr, target))
