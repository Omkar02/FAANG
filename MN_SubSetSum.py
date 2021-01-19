# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def subSetSum(arr, currSum, idx):
    if currSum == 0:
        return True
    if idx == 0:
        return False
    if arr[idx - 1] > currSum:
        return subSetSum(arr, currSum, idx - 1)

    return (subSetSum(arr, currSum - arr[idx - 1], idx - 1) or
            subSetSum(arr, currSum, idx - 1))


arr = [3, 34, 4, 12, 5, 2]
target = 50

print(subSetSum(arr, target, len(arr)))
