# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# num = "1432219"
# k = 3


# def minVal(num, k):
#     if len(num) == k:
#         return "0"

#     i = 1
#     while k > 0 and i < len(num):
#         if num[i] < num[i - 1] and i > 0:
#             num = num[:i - 1] + num[i:]
#             print(num)
#             i -= 1
#             k -= 1
#         else:
#             i += 1

#     if k > 0:
#         l = len(num)
#         num = num[:l - k]
#     return num


# print(minVal(num, k))

# from collections import defaultdict
# from functools import reduce

# M = 3
# words = ["cat", "map", "bat", "man", "pen"]
# queries = ["?at", "ma?", "?a?", "??n"]

# sets = defaultdict(set)
# for word in words:
#     for i, c in enumerate(word):
#         sets[i, c].add(word)

# all_words = set(words)
# for q in queries:
#     possible_words = (sets[i, c] for i, c in enumerate(q) if c != "?")
#     w = reduce(set.intersection, possible_words, all_words)
#     print(q, len(w), w)

# def strawberry(num, n, arr):
#     dp = [[False] * (num + 1) for i in range(n + 1)]
#     dp[0][0] = True
#     res = 0
#     for i in range(1, n + 1):
#         dp[i][0] = True
#         dp[i][arr[i - 1]] = True
#         for j in range(1, num + 1):
#             if j - arr[i - 1] >= 0 and i > 1:
#                 dp[i][j] = dp[i - 2][j - arr[i - 1]]
#             dp[i][j] = dp[i][j] or dp[i - 1][j]
#             if dp[i][j]:
#                 res = max(res, j)
#     return res


# print(strawberry(100, 5, [50, 10, 20, 30, 40]))  # 90


def lengthLongestPath(s):
    """
    :type input: str
    :rtype: int
    """
    st, max_l, c_sum = [], 0, 0
    for part in s.split("\n"):
        tabs = part.count('\t')
        part_len = len(part) - tabs

        while tabs < len(st):
            c_sum = c_sum - st.pop()
        if "." in part:
            max_l = max(max_l, c_sum + part_len + len(st))  # len(st) indicates "/"
        else:
            st.append(part_len)
            c_sum = c_sum + part_len
    return max_l


s = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
print(lengthLongestPath(s))
