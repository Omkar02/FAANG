# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def cuttingRod(rodPrice, n):
    cnt[0] += 1
    if n <= 0:
        return 0
    maxLen = float('-inf')
    for i in range(n):
        curr = rodPrice[i] + cuttingRod(rodPrice, n - i - 1)
        maxLen = max(maxLen, curr)
    return maxLen


rodPrice = [1, 5, 8, 9, 10, 17, 17, 20]
print(cuttingRod(rodPrice, len(rodPrice)))
print(cnt)
