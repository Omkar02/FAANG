# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxCountSubArr(arr, k):
    ans = 0
    n = len(arr)
    runningSum = 0
    preCalSum = set()
    preCalSum.add(0)

    for i in range(n):
        runningSum += arr[i]
        if runningSum - k in preCalSum:
            ans += 1
            runningSum = 0
            preCalSum.clear()
            preCalSum.add(0)

        preCalSum.add(runningSum)

    return ans


arr = [-2, 6, 6, 3, 5, 4, 1, 2, 8]
K = 10
# Output: 3
print(maxCountSubArr(arr, K))
