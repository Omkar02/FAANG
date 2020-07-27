import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def minDeletion(string, n):
    dp = [[None for x in range(n)]for y in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cOne in range(2, n + 1):
        for i in range(n - cOne + 1):
            j = i + cOne - 1
            print(string[i], string[j], '==============')

            if string[i] == string[j] and cOne == 2:
                print('2222222222222222222222')
                dp[i][j] = 2
            elif string[i] == string[j]:
                print('000000000000000000')
                # print(f'-{i}--{j}---{dp[i+1][j-1]}-----------------------------------++')
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                print('111111111111111111')
                dp[i][j] = max(dp[i][j - 1],
                               dp[i + 1][j])
            [print(x) for x in dp]
            print()
    return dp[0][n - 1]


string = 'geeks'
# string = 'madam'
string = 'agbcba'
revStr = string[::-1]
m = len(string)
n = len(revStr)

print(n - minDeletion(string, n))
# Output : 8
