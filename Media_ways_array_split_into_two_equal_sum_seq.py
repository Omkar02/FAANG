# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

def canPartition(arr, idx, currSum, total):
    if currSum * 2 == total:
        return True
    if currSum > total or idx >= len(arr):
        return False

    return canPartition(arr, idx + 1, arr[idx] + currSum, total) or canPartition(arr, idx + 1, currSum, total)


arr = [1, 5, 11, 5]
print(canPartition(arr, 0, 0, sum(arr)))
