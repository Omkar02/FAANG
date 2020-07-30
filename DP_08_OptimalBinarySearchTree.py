import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


'''
formula 
    dp[i][j] = sum(keyi:keyj) + min(Min(x1,x2....xn))
'''


# def optimalBinary(keyOne):
#     dp = [[[0, 0] for i in keyOne] for j in keyOne]
#     for cnt, i in enumerate(keyOne):
#         dp[cnt][cnt] = i

#     for gap in range(2, len(keyOne) + 1):
#         for i in range(len(keyOne) + 1 - gap):
#             j = gap + i - 1
#             totalCostSum = getSum(keyOne, i, j)
#             # print(totalCostSum)
#             minOfAll = float('inf')
#             fromWho = None
#             # print(i, j)
#             for k in range(i, j + 1):

#                 if minOfAll > keyOne[k][0]:
#                     # print('T')
#                     minOfAll = keyOne[k][0]
#                     fromWho = i + 1

#             dp[i][j] = [fromWho, totalCostSum + minOfAll]

#     [print(x) for x in dp]
#     return f'Root = {keyOne[dp[0][-1][0]][0]} | cost = {dp[0][-1][1]}'


# def getSum(array, i, j):
#     tSum = 0
#     for k in range(i, j + 1):
#         tSum += array[k][1]
#     return tSum


# # keyOne = [value,cost]
# keyOne = [[10, 4], [12, 2], [16, 6], [21, 3]]
# # keyOne = [[10, 4], [12, 2], [11, 6], [21, 3]]

# print(optimalBinary(keyOne))
def min_cost_bst(input_array, freq):
    size = rows = cols = len(input_array)
    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for idx in range(rows):
        T[idx][idx] = freq[idx]

    for sub_tree_size in range(2, size + 1):
        for start in range(size + 1 - sub_tree_size):
            end = start + sub_tree_size - 1
            T[start][end] = float("inf")
            total = sum(freq[start:end + 1])
            for k in range(start, end + 1):
                val = total + (0 if k - 1 < 0 else T[start][k - 1]) + (0 if k + 1 > end else T[k + 1][end])
                T[start][end] = min(val, T[start][end])

    return T[0][-1]


input_array = [10, 12, 16, 21]
freq = [4, 2, 6, 3]
print(min_cost_bst(input_array, freq))
