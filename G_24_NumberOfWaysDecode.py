import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def decodeWays(msg):
    n = len(msg)
    dp = [0] * (n + 1)

    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        if msg[i - 1] > '0':
            dp[i] = dp[i - 1]
        if msg[i - 2] == '1' or msg[i - 2] == '2' and msg[i - 1] <= 7:
            dp[i] += dp[i - 2]

    return dp[n]


print(decodeWays('1117'))
