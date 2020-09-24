# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')


def paliMinCut(string):
    n = len(string)
    dp = [[False for _ in range(n)]for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(0, n - length):
            j = i + length - 1

            if length == 2:
                dp[i][j] = srting[i] == string[j]
            else:
                dp[i][j] = string[i] == srting[j] and dp[i + 1][j - 1]

    cuts = [float('inf') for _ in range(n)]

    for k in range(n):
        if dp[0][k]:
            cuts[k] = 0

        else:
            for j in range(1, k + 1):
                if dp[j][k]:
                    cuts[k] = min(cuts[k], cuts[j - 1] + 1)

    return cuts[-1], cuts


srting = "aaa"
print(paliMinCut(srting))
