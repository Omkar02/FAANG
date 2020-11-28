# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Hard')


def wildCardMatch(string, partten):
    n = len(partten)
    m = len(string)
    dp = [[False for i in range(n + 1)] for j in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string[i - 1] == partten[j - 1] or partten[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]

            elif partten[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if partten[j - 2] == '?' or partten[j - 2] == string[i - 1]:
                    dp[i][j] = dp[i][j] if dp[i][j] else dp[i - 1][j]
                else:
                    dp[i][j] = False
    return dp[-1][-1]


s = 'xaabyc'
p = 'xa?*b?c'
print(wildCardMatch(s, p))
