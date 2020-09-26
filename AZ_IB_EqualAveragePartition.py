# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def splitArraySameAvg(array):
    array.sort()
    dp = [set() for _ in range(len(array) // 2 + 1)]
    all_sum = sum(array)
    dp[0] = set([0])
    for items in array:
        for count in range(len(dp) - 2, -1, -1):
            if len(dp[count]) > 0:
                for a in dp[count]:
                    dp[count + 1].add(a + items)

    [print(x) for x in dp]
    for size in range(1, len(dp)):
        if all_sum * size / len(array) in dp[size]:
            return True

    return False


array = [1, 2, 3, 4, 5, 6, 7, 8]
print(splitArraySameAvg(array))
