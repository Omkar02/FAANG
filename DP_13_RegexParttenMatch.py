import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


# formula:
# if string[i - 1] == partten[j - 1] or partten[j - 1] == '.':
#     dp[i][j] = dp[i - 1][j - 1]

# elif partten[j - 1] == '*':
#     dp[i][j] = dp[i][j - 2]
#     if partten[j - 2] == '.' or partten[j - 2] == string[i - 1]:
#         dp[i][j] = dp[i][j] if dp[i][j] else dp[i - 1][j]
#     else:
#         dp[i][j] = False


#------------- * = 0 or more occurance of character befor *
#-------------. = matches any single char

def patternMatcher(string, partten):
    dp = [[False for i in range(len(partten) + 1)]for j in range(len(string) + 1)]
    dp[0][0] = True
    for i in range(1, len(partten)):
        if partten[i - 1] == '*':
            dp[0][i] == dp[0][i - 2]

    for i in range(1, len(string) + 1):
        for j in range(1, len(partten) + 1):
            if string[i - 1] == partten[j - 1] or partten[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]

            elif partten[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if partten[j - 2] == '.' or partten[j - 2] == string[i - 1]:
                    dp[i][j] = dp[i][j] if dp[i][j] else dp[i - 1][j]
                else:
                    dp[i][j] = False
    [print(x) for x in dp]
    print()
    return dp[-1][-1]


string = 'xaabyc'
partten = 'xa.*b.c'

print(f'|{patternMatcher(string, partten)}|')
