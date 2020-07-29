import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


'''
formula 
    items[i][j] = max(value[i]+item[i-1][j-weight[i]],
                      item[i-1][j])

backtracking formula 
    i,j = -1,-1
    if the curr val(i,j) == val(i-1,j):
        means the cur row val is not consider
    if the curr val(i,j) != val(i-1,j):
        concider in the final weight 

    i,j = i-1,j-weight[i]
'''


def Knapsack(items, bagWeight):
    bag = [[0 for x in range(bagWeight + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        curWeight = items[i - 1][0]
        currVal = items[i - 1][1]
        for j in range(bagWeight + 1):
            if curWeight > j:
                bag[i][j] = bag[i - 1][j]
            else:
                bag[i][j] = max(currVal + bag[i - 1][j - curWeight],
                                bag[i - 1][j])
    # [print(x) for x in bag]
    return buidItemBag(bag, items), bag[-1][-1]


def buidItemBag(bag, items):
    seq = []
    i, j = len(bag) - 1, len(bag[0]) - 1

    while i > 0:
        if bag[i][j] == bag[i - 1][j]:
            i -= 1
        else:
            seq.append(items[i - 1])
            j -= items[i - 1][0]
            i -= 1
    return list(reversed(seq))



#items = [weight,values]
items = [[1, 1], [3, 4], [4, 5], [5, 7]]
bagWeight = 7
print(Knapsack(items, bagWeight))
