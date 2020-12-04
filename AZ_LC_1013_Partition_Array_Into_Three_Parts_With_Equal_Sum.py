# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def equalPartition(arr):
    finalSum = sum(arr) // 3
    partition = 0
    currSum = 0
    n = len(arr)
    for i in range(n):
        currSum += arr[i]
        if currSum == finalSum:
            currSum = 0
            partition += 1

        if partition == 2:
            return True

    return False


arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
print(equalPartition(arr))
