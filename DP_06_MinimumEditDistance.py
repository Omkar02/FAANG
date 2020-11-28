# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


'''
formula :
    dp[i][j] = 1 + min(dp[i][j-1],
                       dp[i-1][j],
                       dp[i-1[j-1]])
'''


def minEdit(strOne, strTwo):
    dp = [[0 for x in range(len(strOne) + 1)]for y in range(len(strTwo) + 1)]

    for i in range(1, len(strTwo) + 1):
        for j in range(1, len(strOne) + 1):
            if strOne[j - 1] == strTwo[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                # print(i, j)
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j],
                                   dp[i - 1][j - 1])

    [print(x) for x in dp]
    return dp[5][6]  # , buildSeq(dp, strOne, strTwo)


# [0i, 0, 0, 0, 0, 0, 0]
# [0, 0i, 1, 1, 1, 1, 1]
# [0, 1, 1i, 2, 2, 2, 2]
# [0, 1, 2, 1i, 2i, 3, 3]
# [0, 1, 2, 2, 2, 2i, 3]
# [0, 1, 2, 3, 2, 3, 3i]

# f-->d
# b-->z
# d -X-
def buildSeq(dp, strOne, strTwo):
    seq = []
    i, j = len(dp) - 1, len(dp[0]) - 1
    while i > 0:
        if dp[i][j] >= dp[i - 1][j] and dp[i][j] >= dp[i][j - 1]:
            seq.append([strOne[j - 1], '-->', strTwo[i - 1]])
            i -= 1
            j -= 1
        else:
            seq.append([strTwo[i - 1], '-X-'])
            j -= 1
        # if dp[i][j] == dp[i - 1][j - 1]:
        #     print('-------------2')
        #     i -= 1
        #     j -= 1
        # if dp[i][j] - 1 == dp[i - 1][j - 1]:
        #     print('-------------3')

        #     seq.append([strOne[j - 1], '-->', strTwo[i - 1]])
        #     i = i - 1
        #     j = j - 1

        # if dp[i][j] == dp[i][j - 1]:
        #     seq.append([strTwo[i - 1], '-X-'])
        #     j -= 1
        # print(i, j)
    return seq


strOne, strTwo = 'abcdef', 'azced'
print(minEdit(strOne, strTwo))
