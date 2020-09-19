# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    n = len(prices)
    for i in range(n):
        if prices[i] < minPrice:
            minPrice = prices[i]

        elif (prices[i] - minPrice) > maxProfit:
            maxProfit = prices[i] - minPrice

    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
