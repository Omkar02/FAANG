# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


# only one transaction

def profitWithOneCycle(price):
    n = len(price)
    if n == 1:
        return
    i = 0
    while i < (n - 1):
        while i < (n - 1) and price[i] >= price[i + 1]:
            i += 1
        if i == (n - 1):
            break
        buy = i

        i += 1
        while i < n and price[i] >= price[i - 1]:
            i += 1
        sell = i - 1
        print(f"Buy @ --> {buy}'th day | Sell @ --> {sell}'th")


price = [5, 11, 3, 50, 60, 90]
# print(profitWithOneCycle(price))


def profitWithK(price, k):
    print("Buy-Sell Stock With K transactions To Maximize Profit")
    n = len(price)
    dp = [[0 for x in range(n)] for y in range(k + 1)]
    for t in range(1, k + 1):
        maxThusFar = float('-inf')
        for p in range(n):
            maxThusFar = max(maxThusFar, dp[t - 1][p - 1] - price[p - 1])
            dp[t][p] = max(dp[t][p - 1], maxThusFar + price[p])
    return dp[-1][-1], [print(x) for x in dp]


price = [5, 11, 3, 50, 60, 90]
k = 2
print(profitWithK(price, k)[0])
