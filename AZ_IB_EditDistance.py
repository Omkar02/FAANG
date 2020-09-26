# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def minEditDist(s1, s2):
    dp = [[i for i in range(len(s1) + 1)]for j in range(len(s2) + 1)]
    for i in range(1, len(s2) + 1):
        dp[i][0] = dp[i - 1][0] + 1

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[-1][-1]


s1 = 'abad'
s2 = 'abac'

s1 = "Anshuman"
s2 = "Antihuman"

s1 = 'abc'
s2 = 'yabd'
print(minEditDist(s1, s2))
