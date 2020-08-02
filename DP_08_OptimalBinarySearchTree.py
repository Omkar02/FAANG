import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Medium')


'''
formula
    dp[i][j] = sum(keyi:keyj) + min(Min(x1,x2....xn))
'''


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
