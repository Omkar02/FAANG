import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


def maxProfit(prices, k):
    dp = [[0 for i in range(len(prices))]for j in range(k + 1)]

    for i in range(1, k + 1):
        maxDiff = -prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j - 1],
                           prices[j] + maxDiff)
            maxDiff = max(maxDiff,
                          dp[i - 1][j] - prices[j])
    [print(x) for x in dp]

    return dp[-1][-1]#, print_actual_solution(dp, prices)


# def print_actual_solution(T, prices):
#     transaction = len(T) - 1
#     day = len(T[0]) - 1
#     stack = []

#     while True:
#         if transaction == 0 or day == 0:
#             break

#         if T[transaction][day] == T[transaction][day - 1]:  # Didn't sell
#             day -= 1
#         else:
#             stack.append(day)          # sold
#             max_diff = T[transaction][day] - prices[day]
#             for k in range(day - 1, -1, -1):
#                 if T[transaction - 1][k] - prices[k] == max_diff:
#                     stack.append(k)  # bought
#                     transaction -= 1
#                     break
#     print(stack)
#     for entry in range(len(stack) - 1, -1, -2):
#         print(f"Buy on day {stack[entry]} at price {prices[stack[transaction]]}")
#         print(f"Sell on day {stack[entry]} at price {prices[stack[transaction - 1]]}")
#         transaction -=2


prices = [2, 5, 7, 1, 4, 3, 1, 3]
k = 3

print(maxProfit(prices, k))
