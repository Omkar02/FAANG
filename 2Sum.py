

# pizza = []
# import math


# def piz(pizza):
#     pizza.sort()
#     n = len(pizza) - 1
#     if (n + 1) % 4 != 0:
#         print(8 % 4)
#         return 0
#     if n == 4 or n == 2 or n == 3:
#         return pizza[1]
#     val = 0

#     i = 0
#     while i <= n:
#         # if i + 4 > n:
#         #     return val
#         val += pizza[i:i + 4][1]
#         print(pizza[i:i + 4])
#         i += 4
#         # print(math.pow(10, 9) + 7)
#     return val if val < math.pow(10, 9) + 7 else math.pow(10, 9) + 7


# pizza = [1, 3, 4, 1, 5, 1, 5, 3]
# from random import shuffle
# pizza = [i for i in range(400)]
# shuffle(pizza)
# # print(pizza)
# print(piz(pizza))
#==============================================================Expedia

def compressString(string):
    res = ""
    count = 1
    res += string[0]
    for i in range(len(string) - 1):
        if(string[i] == string[i + 1]):
            count += 1
        else:
            if(count > 1):
                res += str(count)
            res += string[i + 1]
            count = 1
    if(count > 1):
        res += str(count)
    return res


# print(compress('abaabbbc'))


# Metro Land Festival - HackerRank Problem/Solution - Codingee


def cost(x, y, a, b):
    return (abs(x - a) + abs(y - b))


def metroland(numpeople, x, y):
    ans = 0
    xx, yy = [], []
    nPeo = len(numpeople)
    for i in range(nPeo):
        count = numpeople[i]
        while count != 0:
            xx.append(x[i])
            yy.append(y[i])
            count -= 1

    xx.sort()
    yy.sort()
    mx, my = xx[len(xx) // 2], yy[len(yy) // 2]

    for i in range(nPeo):
        ans += numpeople[i] * cost(mx, my, x[i], y[i])
    return ans


print(metroland([1, 2], [1, 3], [1, 1]))
print(metroland([1, 1, 1], [5, 2, 3], [3, 4, 7]))
# }
#     int greedy(vector < int > numpeople, vector < int > x, vector < int > y){
#     vector < int > xx, yy

#     int ans = 0
#     for(int i=0
#         i < numpeople.size()
#         i + +){
#         int count = numpeople[i]
#         while(count - -){
#             xx.push_back(x[i])
#             yy.push_back(y[i])
#         }
#     }

#     sort(xx.begin(), xx.end())
#     sort(yy.begin(), yy.end())
#     int mx, my

#     mx = xx[xx.size() / 2]
#     my = yy[yy.size() / 2]

#     for(int i=0
#         i < numpeople.size()
#         i + +){
#         ans += numpeople[i] * cost(mx, my, x[i], y[i])
#     }
#     return ans

# ------------------


def uniquedevice(myList):
    dico = {}
    result = []

    for item in myList:
        if item in dico.keys():
            dico[item] += 1
            result.append(f"{item}{dico[item]}")
        else:
            dico[item] = 0
            result.append(f"{item}")
    return result
# ------------------------------


myList = ['lamp', 'lamp', 'tv', 'lamp', 'tv', 'lamp']
print(uniquedevice(myList))


#-----------------------------------
cnt = [0]


def calculate(pos, prev, left, k, cache):
    cnt[0] += 1
    curr = (pos, prev, left)
    if curr in cache:
        return cache[curr]

    if (pos == k):
        if (left == 0):
            return 1
        else:
            return 0

    if (left == 0):
        return 0

    cache[curr] = 0
    for i in range(prev, left + 1):
        cache[curr] += calculate(pos + 1, i, left - i, k, cache)
    return cache[curr]


def countWaystoDivide(n, k):
    return calculate(0, 1, n, k, {})
#-----------------------------------


N = 7
K = 3


print(countWaystoDivide(N, K))
print(cnt)
