import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Dynamic-Programing', Difficult='Hard')

'''Given a knapsack weight W and a set of n items with certain value
vali and weight wti, we need to calculate minimum amount that could
make up this quantity exactly. This is different from classical Knapsack problem,
here we are allowed to use
---------->unlimited number of instances of an item<---------------.

Examples:

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}
Output : 110
We get maximum value with one unit of
weight 5 and one unit of weight 3.'''

totalWeight = 100
values = [10, 30, 20]
weight = [5, 10, 15]


def unboundedKnapsack(totalWeight, value, weight):
    knapSackValues = [0 for i in range(totalWeight + 1)]

    for i in range(totalWeight + 1):
        for j in range(len(value)):
            if weight[j] <= i:
                knapSackValues[i] = max(knapSackValues[i],
                                        knapSackValues[i - weight[j]] + value[j])
    print(knapSackValues)
    print(knapSackValues[-1])


unboundedKnapsack(totalWeight, values, weight)

# def unboundedKnapsack(W, n, val, wt):

#     # dp[i] is going to store maximum
#     # value with knapsack capacity i.
#     dp= [0 for i in range(W + 1)]

#     ans= 0

#     # Fill dp[] using above recursive formula
#     for i in range(W + 1):
#         for j in range(n):
#             if (wt[j] <= i):
#                 dp[i]= max(dp[i], dp[i - wt[j]] + val[j])

#     return dp[W]
