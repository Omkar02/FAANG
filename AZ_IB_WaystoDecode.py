# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def waysTodecode(num):
    n = len(num)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if num[0] == '0' else 1
    for i in range(2, n + 1):
        if int(num[i - 1]) >= 1:
            dp[i] += dp[i - 1]

        if int(num[i - 2:i]) < 27 and int(num[i - 2:i]) > 10:
            dp[i] += dp[i - 2]
    return dp[-1], dp


num = "1231"
print(waysTodecode(num))
