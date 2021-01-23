# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def getThreeSum(arr, target):
    arr.sort()
    triplet = []
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            tSum = arr[i] + arr[left] + arr[right]
            if tSum == target:
                triplet.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif target > tSum:
                left += 1
            elif target < tSum:
                right -= 1
    return triplet


arr = [-1, 0, 1, 2, -1, -4]
target = 0
print(getThreeSum(arr, target))
