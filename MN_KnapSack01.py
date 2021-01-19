# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programming', Difficult='Medium')

cnt = [0]


def knapSack(bagW, itemWei, itemVal, idx):
    cnt[0] += 1
    if bagW == 0 or idx == 0:
        return 0
    if itemWei[idx - 1] > bagW or idx < 0:
        return knapSack(bagW, itemWei, itemVal, idx - 1)

    return max(itemVal[idx - 1] + knapSack(bagW - itemWei[idx - 1], itemWei, itemVal, idx - 1),
               knapSack(bagW, itemWei, itemVal, idx - 1))


itemVal = [60, 100, 120]
itemWei = [10, 20, 30]

bagW = 50
idx = len(itemWei)

print(knapSack(bagW, itemWei, itemVal, idx))
print(cnt)
