# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def minInsertion(s):
    n = len(s)
    dp = [[0 for _ in s] for _ in s]

    for gap in range(1, n):
        l = 0
        for h in range(gap, n):
            if s[l] == s[h]:
                dp[l][h] = dp[l + 1][h - 1]

            else:
                dp[l][h] = min(dp[l][h - 1], dp[l + 1][h]) + 1

            l += 1
    return dp[0][n - 1]


s = "geeks"
print(minInsertion(s))
