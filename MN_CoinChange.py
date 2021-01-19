# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')


def minCoinChange(denom, target, idx):
    # base condition if 0 the coins will be 0
    if target == 0:
        return 0
    coins = float('inf')
    # compare for all coins
    for i in range(idx):
        if denom[i] <= target:
            currCoin = minCoinChange(denom, target - denom[i], idx)
            coins = min(coins, currCoin + 1)
    return coins


denom = [1, 2, 3]
idx = len(denom)
target = 10
print(minCoinChange(denom, target, idx))
