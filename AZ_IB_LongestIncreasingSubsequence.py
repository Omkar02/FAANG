# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def LIS(array):
    n = len(array)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1

    print(dp)

    return dp[-1]


array = [1, 2, 1, 5]
array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(array))


