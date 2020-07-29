import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


"""
formula :
    t[i][j]  =  min(t[i][k]+
                    t[k+1][j]+
                    val[i][0]*val[k][1]*val[j][1])

"""


# def chainMultiplication(chain):
#     dp = [[0 for i in range(len(chain))]for j in range(len(chain))]

#     for l in range(2, len(chain)):
#         for i in range(0, len(chain) - l):
#             j = i + l
#             dp[i][j] = float('inf')
#             for k in range(i + 1, j):
#                 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + chain[i] * chain[k] * chain[j])

#     # [print(x) for x in dp]
#     return dp[0][-1]


# chain = [2, 3, 6, 4, 5]
# print(chainMultiplication(chain))


def chainMutiplicatin(chain):
    n = len(chain)
    dp = [[0 for x in range(n)]for y in range(n)]

    for l in range(2, n):
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                # print(chain[i], chain[k], chain[j])
                dp[i][j] = min(dp[i][j],
                               dp[i][k] + dp[k][j] + chain[i] * chain[k] * chain[j])
    return dp[0][-1]


chain = [2, 3, 6, 4, 5]
print(chainMutiplicatin(chain))
